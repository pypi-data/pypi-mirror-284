"""
1. buffer audio-arrays -> buffering
2. transcribe -> stateful but NOT buffering
3. glue transcripts -> buffering
"""

import logging
from collections.abc import Iterator
from dataclasses import dataclass, field
from itertools import pairwise
from typing import ClassVar

from buildable_dataclasses.buildable import Buildable
from misc_python_utils.slugification import CasedNameSlug, slugify_en_only
from speech_utils.asr_utils.accumulating_asr_streamer import (
    AccumulatingASRStreamInferencer,
)
from speech_utils.asr_utils.streaming_asr_utils import (
    END_OF_AUDIO_STREAM,
    EndOfAudioStream,
    StreamingASRMessage,
)
from speech_utils.audio_segmentation_utils.non_overlapping_segments_variations import (
    MsTimeSpanNeTextNeNoSeg,
)
from speech_utils.data_models.misc_data_types import EmptySeq
from speech_utils.data_models.timespans_with_text import MsTimeSpanNeText
from speech_utils.signal_chunking.audio_chunking import AudioChunker
from speech_utils.signal_chunking.audio_signal_chunk import AudioSignalChunk

from ctc_asr_inference.chunked_inference.asr_infer_decode import ASRInferDecoder
from ctc_asr_inference.chunked_inference.transcript_glueing import NO_NEW_SUFFIX
from ctc_asr_inference.chunked_inference.transcript_gluer import TranscriptGluer
from ctc_asr_inference.ctc_decoding.pyctc_decoder import PyCTCKenLMDecoder
from ctc_asr_inference.timestamped_letters import NeTimestampedLetters

logger = logging.getLogger(__name__)


@dataclass(slots=True, kw_only=True)
class Aschinglupi(Buildable, AccumulatingASRStreamInferencer[MsTimeSpanNeText]):
    """

        naming: Aschinglupi == ASR Chunking Inference Gluing Pipeline
        does:
        1. chunking
        2. asr-inference = inference + decoding
        3. transcript glueing
        TODO: split it into pieces!

    ─────▀▀▌───────▐▀▀
    ─────▄▀░◌░░░░░░░▀▄
    ────▐░░◌░▄▀██▄█░░░▌
    ────▐░░░▀████▀▄░░░▌
    ────═▀▄▄▄▄▄▄▄▄▄▄▄▀═

    """

    audio_chunker: AudioChunker = field(
        init=True,
        repr=True,
    )
    hf_asr_decoding_inferencer: ASRInferDecoder
    transcript_gluer: TranscriptGluer
    input_sample_rate: int = field(init=False, repr=False, default=16_000)

    enter_lock: bool = field(
        init=False,
        repr=False,
        default=False,  # noqa: COM812
    )  # TODO: how can I enforce __enter__ otherwise?
    __serialize_anyhow__: ClassVar[set[str]] = {"name"}
    name: CasedNameSlug = field(init=False)

    def __post_init__(self):
        self.name = slugify_en_only(
            f"aschinglupi-{self.hf_asr_decoding_inferencer.name}",
        )

    def _stream_infer(
        self,
        audio_chunk: AudioSignalChunk | EndOfAudioStream,
    ) -> Iterator[StreamingASRMessage[MsTimeSpanNeText]]:
        assert self.enter_lock
        # logger.warning(
        #     f"{audio_message.frame_idx=},{audio_message.end_of_signal=},input-audio-dur: {audio_message.end - audio_message.start}")
        # if len(chunks)>1:
        #     logger.warning(f"{len(chunks)=},input-audio-dur: {audio_message.end-audio_message.start}")

        if (
            isinstance(audio_chunk, AudioSignalChunk)
            and self.input_sample_rate != audio_chunk.sample_rate
        ):
            self._reset_aschinglupi()
            self.input_sample_rate = audio_chunk.sample_rate
            logger.info(f"SETTING SAMPLERATE TO {self.input_sample_rate}")

        chunks = (
            self.audio_chunker.flush_reset_chunker()
            if isinstance(audio_chunk, EndOfAudioStream)
            else self.audio_chunker.buffer_and_chunk(audio_chunk)
        )
        for chunk in chunks:
            chunk: AudioSignalChunk
            letters = self.hf_asr_decoding_inferencer.audio_to_segmented_transcripts(
                chunk,
            )
            if not isinstance(letters, EmptySeq):
                letters.timestamps += (chunk.frame_idx) / self.input_sample_rate
                if (  # TODO: instead of nested ifs use early return pattern here
                    new_suffix := self.transcript_gluer.calc_transcript_suffix(letters)
                ) is not NO_NEW_SUFFIX:
                    assert isinstance(new_suffix, NeTimestampedLetters)
                    x = [
                        *new_suffix.timestamps.tolist(),
                        new_suffix.timestamps[-1] + 0.001,
                    ]
                    letter_start_ends: list[tuple[float, float]] = list(pairwise(x))
                    yield StreamingASRMessage(
                        id_=chunk.signal_id,
                        segments=MsTimeSpanNeTextNeNoSeg(
                            [
                                MsTimeSpanNeText(start=s, end=e, text=t)
                                for (s, e), t in zip(
                                    letter_start_ends,
                                    new_suffix.letters,
                                    strict=True,
                                )
                            ],
                        ),
                    )
        if audio_chunk is END_OF_AUDIO_STREAM:
            self.transcript_gluer.reset()
            assert (
                self.audio_chunker.fxd_chkr._buffer is None  # noqa: SLF001
            )  # no need to reset chunker here, cause it is already reset!

    def _enter_streaming_service(self) -> None:
        self._reset_aschinglupi()
        self.enter_lock = True

    def _reset_aschinglupi(self) -> None:
        self.audio_chunker.reset_chunker()
        self.transcript_gluer.reset()

    def _exit_streaming_service(
        self,
    ) -> None:
        self.enter_lock = False
        decoder = self.hf_asr_decoding_inferencer.decoder
        if isinstance(decoder, PyCTCKenLMDecoder):
            logger.warning(f"cleaning up {decoder=}")
            decoder._pyctc_decoder.cleanup()  # one has to manually cleanup!  # noqa: SLF001

    @property
    def vocab(self) -> list[str]:
        return self.hf_asr_decoding_inferencer.vocab


# TODO: who wanted this?
# def is_end_of_signal(am: AudioSignalChunk) -> bool:
#     return am.end_of_signal
#
#
# CompleteMessage = Annotated[
#     NeList[AudioSignalChunk],
#     Is[lambda ams: is_end_of_signal(ams[-1])],
# ]

NO_TRANSCRIPT = "..."


# def aschinglupi_transcribe_chunks(
#     inferencer: Aschinglupi,
#     chunks: Iterable[NeNpFloatDim1],
# ) -> TimestampedLetters:
#     audio_messages = list(
#         audio_messages_from_chunks(
#             signal_id="nobody_cares",
#             chunks=chunks,
#             sample_rate=inferencer.input_sample_rate,
#         ),
#     )
#     inferencer.reset()
#
#     outputs: list[ASRStreamInferenceOutput] = [
#         t for inpt in audio_messages for t in inferencer.handle_inference_input(inpt)
#     ]
#     if len(outputs) == 0:
#         print("\ngot empty transcript!\n")  # noqa: T201
#         transcript = TimestampedLetters(
#             NO_TRANSCRIPT,
#             timestamps=np.array([audio_messages[0].frame_idx] * 3),
#         )
#     else:
#         transcript = accumulate_transcript_suffixes(
#             [tr.aligned_transcript for tr in outputs],
#         )
#     inferencer.reset()
#     return transcript


#
# def transcribe_audio_array(
#     inferencer: Aschinglupi, array: Numpy1D, chunk_dur: float = 4.0
# ) -> TimestampedLetters:
#     if array.dtype is not np.int16:
#         array = convert_to_16bit_array(array)
#     chunks = break_array_into_chunks(array, int(inferencer.sample_rate * chunk_dur))
#     last_response = aschinglupi_transcribe_chunks(inferencer, chunks)
#     return last_response


"""
if __name__ == "__main__":
    die_if_unbearable(
        [
            AudioMessageChunk(
                "foo", 0, np.zeros((9,), dtype=np.int16), end_of_signal=True
            )
        ],
        CompleteMessage,
    )
"""
