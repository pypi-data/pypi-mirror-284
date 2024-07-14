"""
1. buffer audio-arrays -> buffering
2. transcribe -> stateful but NOT buffering
3. glue transcripts -> buffering
"""

import itertools
import logging
from dataclasses import dataclass, field
from typing import ClassVar

from buildable_dataclasses.buildable import Buildable
from misc_python_utils.beartypes import NeList
from misc_python_utils.slugification import CasedNameSlug
from speech_utils.asr_utils.accumulating_longform_asr_inferencer import (
    AccumulatingLongformASRInferencer,
)
from speech_utils.asr_utils.streaming_asr_utils import StreamingASRMessage
from speech_utils.audio_segmentation_utils.non_overlapping_segments_variations import (
    TextNeNoSeg,
)
from speech_utils.signal_chunking.audio_chunking import AudioChunker
from speech_utils.signal_chunking.audio_signal_chunk import AudioSignalChunk
from speech_utils.signal_chunking.signal_chunker import FLUSH_AND_RESET_CHUNKER

from ctc_asr_inference.chunked_inference.asr_infer_decode import (
    BatchedASRInferDecoder,
)
from ctc_asr_inference.chunked_inference.transcript_glueing import NO_NEW_SUFFIX
from ctc_asr_inference.chunked_inference.transcript_gluer import TranscriptGluer
from ctc_asr_inference.ctc_decoding.pyctc_decoder import PyCTCKenLMDecoder
from ctc_asr_inference.timestamped_letters import TimestampedLetters

logger = logging.getLogger(__name__)


@dataclass(kw_only=True)
class LongformCtcASRInferencer(Buildable, AccumulatingLongformASRInferencer):
    audio_chunker: AudioChunker | None = field(
        init=True,
        repr=True,
        default=None,
    )
    hf_asr_decoding_inferencer: BatchedASRInferDecoder
    transcript_gluer: TranscriptGluer
    enter_lock: bool = field(
        init=False,
        repr=False,
        default=False,  # noqa: COM812
    )  # TODO: how can I enforce __enter__ otherwise?
    input_sample_rate: int | None = field(init=False, repr=False, default=None)
    __serialize_anyhow__: ClassVar[set[str]] = {"name"}

    name: CasedNameSlug = field(init=False)

    def __post_init__(self):
        self.name = (
            f"longform-ctc-asr-{self.hf_asr_decoding_inferencer.logits_inferencer.name}"
        )

    def _longform_infer(
        self,
        audio_chunks: NeList[AudioSignalChunk],
    ) -> list[StreamingASRMessage]:
        assert self.enter_lock
        self.input_sample_rate = audio_chunks[0].sample_rate
        self.audio_chunker._set_sample_rate(self.input_sample_rate)  # noqa: SLF001
        # logger.warning(
        #     f"{audio_message.frame_idx=},{audio_message.end_of_signal=},input-audio-dur: {audio_message.end - audio_message.start}")
        # if len(chunks)>1:
        #     logger.warning(f"{len(chunks)=},input-audio-dur: {audio_message.end-audio_message.start}")
        chunks = [
            chunk
            for audio_chunk in [*audio_chunks, FLUSH_AND_RESET_CHUNKER]
            for chunk in self.audio_chunker.buffer_chunk_flush(
                audio_chunk,
            )
        ]
        arrays = [ch.array for ch in chunks]
        batch_letters = self.hf_asr_decoding_inferencer.batch_transcribe_audio_arrays(
            arrays,
        )
        for letters, chunk in zip(batch_letters, chunks, strict=True):
            letters.timestamps += (chunk.frame_idx) / self.input_sample_rate
        return self._glue_transcripts(batch_letters)

    def _glue_transcripts(
        self,
        transcripts: NeList[TimestampedLetters],
    ) -> list[StreamingASRMessage]:
        glued_suffixes = []
        for letters in transcripts:
            if (
                new_suffix := self.transcript_gluer.calc_transcript_suffix(letters)
            ) is not NO_NEW_SUFFIX:
                segments = timestamped_letters_to_segments(new_suffix)
                glued_suffixes.append(
                    StreamingASRMessage(
                        id_="foo",
                        segments=segments,
                        # end_of_message=chunk.end_of_signal,
                    ),
                )
        self.transcript_gluer.reset()
        return glued_suffixes

    def __enter__(self):
        self.audio_chunker.reset_chunker()
        self.transcript_gluer.reset()
        self.enter_lock = True

    def __exit__(
        self,
        exc_type=None,  # noqa: ANN001
        exc_val=None,  # noqa: ANN001
        exc_tb=None,  # noqa: ANN001
    ) -> None:
        self.enter_lock = False
        decoder = self.hf_asr_decoding_inferencer.decoder
        if isinstance(decoder, PyCTCKenLMDecoder):
            decoder._pyctc_decoder.cleanup()  # one has to manually cleanup!  # noqa: SLF001

    @property
    def vocab(self) -> list[str]:
        return self.hf_asr_decoding_inferencer.vocab


def timestamped_letters_to_segments(
    letters: TimestampedLetters,
) -> TextNeNoSeg:
    ONE_MS = 0.001
    letter_start_ends = itertools.pairwise(
        [
            *letters.timestamps.tolist(),
            letters.timestamps[-1] + ONE_MS,
        ],
    )
    return TextNeNoSeg(
        [
            StartEndText(s, e, t)  # noqa: F821
            for (s, e), t in zip(
                letter_start_ends,
                letters.letters,
                strict=True,
            )
        ],
    )
