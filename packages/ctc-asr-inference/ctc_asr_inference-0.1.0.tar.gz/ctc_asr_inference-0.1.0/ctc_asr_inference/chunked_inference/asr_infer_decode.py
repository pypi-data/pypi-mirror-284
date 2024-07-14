from dataclasses import dataclass, field

import numpy as np
import torch
from buildable_dataclasses.buildable import Buildable
from misc_python_utils.beartypes import (
    NeList,
    NeNpFloatDim1,
    NumpyFloat2DArray,
    TorchTensor2D,
)
from misc_python_utils.slugification import CasedNameSlug
from speech_utils.audio_io_utils.torchaudio_resampling import torchaudio_resample
from speech_utils.data_models.audio_array_models import AudioArray
from speech_utils.data_models.misc_data_types import EMPTY_SEQ, EmptyObject, EmptySeq

from ctc_asr_inference.ctc_decoding.ctc_decoding import BaseCTCDecoder
from ctc_asr_inference.ctc_decoding.logit_aligned_transcript import (
    LogitAlignedTranscript,
)
from ctc_asr_inference.ctc_logits_inferencer.asr_logits_inferencer import (
    ASRLogitsInferencer,
    BatchedASRLogitsInferencer,
)
from ctc_asr_inference.timestamped_letters import (
    AudioArray2TimestampledLetters,
    NeTimestampedLetters,
    TimestampedLetters,
)


@dataclass(kw_only=True)
class ASRInferDecoder(Buildable, AudioArray2TimestampledLetters):
    """
    does asr-inference WITH decoding greedy/lm-based
    TODO:
        also does preprocessing of the audio-array (conversion+resampling)!
        split into logits-inferencer and decoder
        well seems huggingface's "src/transformers/pipelines/automatic_speech_recognition.py" cannot yet do streaming! just "long audio-files"

    """

    logits_inferencer: ASRLogitsInferencer
    decoder: BaseCTCDecoder
    name: CasedNameSlug = field(init=False)
    input_sample_rate: int = field(init=False, default=16000)

    def __post_init__(self):
        self.name = f"{self.logits_inferencer.name}-{self.decoder.__class__.__name__}"

    @property
    def vocab(self) -> list[str]:
        return self.logits_inferencer.vocab

    def audio_to_segmented_transcripts(
        self,
        audio_array: AudioArray,
    ) -> NeTimestampedLetters | EmptySeq[object]:
        if self.input_sample_rate != audio_array.sample_rate:
            self.input_sample_rate = audio_array.sample_rate

        array = torchaudio_resample(
            signal=torch.from_numpy(audio_array.array.astype(np.float32)),
            sample_rate=audio_array.sample_rate,
            target_sample_rate=self.logits_inferencer.asr_model_sample_rate,
        ).numpy()
        logits = self.logits_inferencer.calc_logits(array)
        return _aligned_decode(
            self.decoder,
            logits,
            len(array),
            audio_array.sample_rate,
        )


@dataclass
class BatchedASRInferDecoder(ASRInferDecoder):
    logits_inferencer: BatchedASRLogitsInferencer

    def batch_transcribe_audio_arrays(
        self,
        audio_arrays: NeList[NeNpFloatDim1],
    ) -> list[TimestampedLetters]:
        if self.input_sample_rate != self.logits_inferencer.asr_model_sample_rate:
            audio_arrays = [
                torchaudio_resample(
                    signal=torch.from_numpy(  # pyright: ignore [reportUnknownMemberType] # TODO how to suppress this false-positive everywhere?
                        audio_array.astype(np.float32),
                    ),
                    sample_rate=self.input_sample_rate,
                    target_sample_rate=self.logits_inferencer.asr_model_sample_rate,
                ).numpy()
                for audio_array in audio_arrays
            ]
        logits_batch = self.logits_inferencer.batched_calc_logits(audio_arrays)
        out = [
            _aligned_decode(
                self.decoder,
                logits,
                len(audio_array),
                self.logits_inferencer.asr_model_sample_rate,
            )
            for logits, audio_array in zip(logits_batch, audio_arrays, strict=False)
        ]
        return [x for x in out if not isinstance(x, EmptySeq)]


def _aligned_decode(
    decoder: BaseCTCDecoder,
    logits: TorchTensor2D | NumpyFloat2DArray,
    audio_array_seq_len: int,
    sample_rate: int,
) -> NeTimestampedLetters | EmptyObject:
    """
    letters aligned to audio-frames

    """
    logits = logits.numpy() if isinstance(logits, torch.Tensor) else logits
    dec_out: LogitAlignedTranscript = decoder.ctc_decode(logits)[0]

    logits_seq_len = logits.shape[0]
    audio_to_logits_ratio = audio_array_seq_len / logits_seq_len
    timestamps = [audio_to_logits_ratio * i / sample_rate for i in dec_out.logit_ids]
    _push_timestamps_to_future_to_ensure_strict_monotone_increasing(timestamps)

    return (
        NeTimestampedLetters(
            dec_out.text,
            np.array(timestamps),
        )
        if len(dec_out.text) > 0
        else EMPTY_SEQ
    )  # ,dec_out.logits_score,dec_out.lm_score


def _push_timestamps_to_future_to_ensure_strict_monotone_increasing(
    timestamps: list[float],
) -> None:
    """
    this is necessary cause nemo-conformer leads to successive letters with same timestamps!
    """
    small_value = 0.001
    for k in range(len(timestamps) - 1):
        ts, next_ts = timestamps[k], timestamps[k + 1]
        if next_ts <= ts:
            timestamps[k + 1] = ts + small_value
            # print(f"corrected {k+1}")
