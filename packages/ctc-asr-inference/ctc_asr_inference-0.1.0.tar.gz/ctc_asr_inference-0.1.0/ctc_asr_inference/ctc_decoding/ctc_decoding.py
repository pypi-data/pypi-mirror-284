from abc import abstractmethod
from dataclasses import dataclass

from misc_python_utils.beartypes import NumpyFloat2DArray

from ctc_asr_inference.ctc_decoding.logit_aligned_transcript import (
    LogitAlignedTranscript,
)

NoneType = type(None)

AlignedBeams = list[LogitAlignedTranscript]
BatchOfAlignedBeams = list[AlignedBeams]


@dataclass
class BaseCTCDecoder:
    @abstractmethod
    def ctc_decode(self, logits: NumpyFloat2DArray) -> AlignedBeams:
        raise NotImplementedError

    # @property # TODO: needed?
    # def vocab(self):
    #     return list(self._tokenizer.get_vocab().keys())
