from abc import abstractmethod
from dataclasses import dataclass
from typing import ClassVar

import torch
from buildable_dataclasses.buildable import Buildable
from misc_python_utils.beartypes import (
    NeList,
    NeNpFloatDim1,
    NumpyFloat2DArray,
    TorchTensor2D,
)
from misc_python_utils.slugification import CasedNameSlug
from python_text_cleaning.asr_text_cleaning import Letters
from transformers import set_seed

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
set_seed(42)


@dataclass
class ASRLogitsInferencer(Buildable):
    """
        Asr Connectionis temporal classification (CTC) Logits Inference

    ──────────────────────────────────────────────
    ──────│─────│───────│─────│───────│────────│──
    ──────│─────│───────│─────│───────│────────│──
    ──────│──┌───┬────┬───┐──┌┐───────│┌┐──────│──
    ──────│──│┌─┐│┌┐┌┐│┌─┐│──││───────┌┘└┐─────│──
    ──────│──││─└┴┘││└┤││└┘──││┌──┬──┬┼┐┌┼──┐──│──
    ──────│──││─┌┐─││─│││┌┬──┤││┌┐│┌┐├┤│││──┤──│──
    ──────│──│└─┘│─││─│└─┘├──┤└┤└┘│└┘│││└┼──│──│──
    ──────│──└───┘─└┘─└───┘──└─┴──┴─┐├┘└─┴──┘──│──
    ──────│─────│───────│─────│───┌─┘││────────│──
    ──────│─────│───────│─────│───└──┘│────────│──
    ──────│─────│───────│─────│───────│────────│──
    ──────│─────│───────│─────│───────│────────│──

    """

    name: CasedNameSlug
    asr_model_sample_rate: ClassVar[int] = 16000

    @property
    def is_bpe(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def vocab(self) -> NeList[str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def letter_vocab(self) -> Letters:
        raise NotImplementedError

    @abstractmethod
    def calc_logits(self, audio: NeNpFloatDim1) -> TorchTensor2D:
        raise NotImplementedError


@dataclass
class BatchedASRLogitsInferencer(ASRLogitsInferencer):
    @abstractmethod
    def batched_calc_logits(
        self,
        audio: list[NeNpFloatDim1],
    ) -> list[NumpyFloat2DArray]:
        raise NotImplementedError
