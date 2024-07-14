import logging
from dataclasses import dataclass, field
from tempfile import TemporaryDirectory
from typing import ClassVar

import nemo.collections.asr as nemo_asr
import numpy as np
import soundfile
import torch
from misc_python_utils.beartypes import (
    NeList,
    NeNpFloatDim1,
    NumpyFloat2DArray,
    TorchTensor2D,
)
from misc_python_utils.slugification import CasedNameSlug
from nemo.collections.asr.models import EncDecCTCModel
from python_text_cleaning.asr_text_cleaning import Letters
from speech_utils.audio_io_utils.audio_utils import MAX_16_BIT_PCM

from ctc_asr_inference.ctc_logits_inferencer.asr_logits_inferencer import (
    BatchedASRLogitsInferencer,
)
from ctc_asr_inference.ctc_logits_inferencer.nemo_checkpoints import (
    NemoCheckpoint,
)

logger = logging.getLogger(__name__)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
logger.info(f"DEVICE: {DEVICE}")


@dataclass
class NemoASRLogitsInferencer(BatchedASRLogitsInferencer):
    checkpoint: NemoCheckpoint
    is_bpe: ClassVar[bool] = True
    batch_size: int = 10

    _model: EncDecCTCModel = field(init=False)
    name: CasedNameSlug = field(init=False)

    def __post_init__(self):
        self.name = self.checkpoint.name.replace("_", "-")

    def _build_self(self) -> None:
        self._model = nemo_asr.models.EncDecCTCModel.restore_from(
            self.checkpoint.model_file,
        )
        self._model.eval()
        self._model = self._model.to(DEVICE)

    @property
    def vocab(self) -> NeList[str]:
        return list(self._model.cfg.decoder.vocabulary)  # noqa: WPS219 -> TODO!

    @property
    def letter_vocab(self) -> Letters:
        bad_letters = ["<", ">", "▁"]
        return "".join(
            [l for l in dict.fromkeys("".join(self.vocab)) if l not in bad_letters],
        )

    def calc_logits(self, audio: NeNpFloatDim1) -> TorchTensor2D:
        device = next(self._model.parameters()).device
        audio_signal = torch.as_tensor(audio.reshape(1, -1), dtype=torch.float32)
        audio_signal_len = torch.as_tensor([audio.size], dtype=torch.int64)

        with torch.no_grad():
            log_probs, _encoded_len, _greedy_predictions = self._model(
                input_signal=audio_signal.to(device),
                input_signal_length=audio_signal_len.to(device),
            )
            return log_probs.cpu().squeeze()

    def batched_calc_logits(
        self,
        audio: NeList[NeNpFloatDim1],
    ) -> list[NumpyFloat2DArray]:
        # device = next(self.model.parameters()).device

        with torch.no_grad():  # noqa: SIM117
            with TemporaryDirectory(prefix="/tmp/nemo_tmp_dir") as tmpdir:
                audio_files = [
                    self._write_audio(f"{tmpdir}/{k}.wav", a)
                    for k, a in enumerate(audio)
                ]

                log_probs = self._model.transcribe(
                    paths2audio_files=audio_files,
                    batch_size=self.batch_size,
                    logprobs=True,
                    verbose=False,
                )
        return log_probs

    def _write_audio(self, file: str, audio: NeNpFloatDim1) -> str:  # noqa: PLR6301
        """
        TODO: nemo only accepts audio-files as input
        """
        audio = audio / np.max(np.abs(audio)) * (MAX_16_BIT_PCM - 1)
        audio = audio.astype(np.int16)
        soundfile.write(file, audio, samplerate=16000)
        return file


# TODO: what about these?
#
#
#     def calc_logsoftmaxed_logits(self, audio: NpFloatDim1) -> NumpyFloat2DArray:
#         device = next(self._model.parameters()).device
#         audio_signal = torch.as_tensor(audio.reshape(1, -1), dtype=torch.float32)
#         audio_signal_len = torch.as_tensor([audio.size], dtype=torch.int64)
#
#         with torch.no_grad():
#             log_probs, encoded_len, greedy_predictions = self._model(
#                 input_signal=audio_signal.to(device),
#                 input_signal_length=audio_signal_len.to(device),
#             )
#             log_probs = log_probs.cpu().squeeze()
#
#         log_probs = self._post_process_for_ctc_alignment(log_probs)
#         assert log_probs.shape[1] == len(
#             self.vocab
#         ), f"{log_probs.shape=},{len(self.vocab)}"
#         return log_probs
#
#
#     def _post_process_for_ctc_alignment(
#         self, log_probs: NumpyFloat2DArray
#     ) -> NumpyFloat2DArray:
#         """
#         see:nvidia-nemo-code:  tools/ctc_segmentation/scripts/run_ctc_segmentation.py
#         """
#         blank_col = log_probs[:, -1].reshape((log_probs.shape[0], 1))
#         log_probs = np.concatenate((blank_col, log_probs[:, :-1]), axis=1)
#         return log_probs
