from dataclasses import dataclass, field
from typing import Any

import torch
from buildable_dataclasses.buildable import Buildable
from misc_python_utils.beartypes import NumpyFloat2DArray
from misc_python_utils.prefix_suffix import PrefixSuffix
from transformers import AutoTokenizer, PreTrainedTokenizer
from transformers.models.wav2vec2.tokenization_wav2vec2 import (
    Wav2Vec2CTCTokenizer,
    Wav2Vec2CTCTokenizerOutput,
)

from ctc_asr_inference.ctc_decoding.ctc_decoding import (
    AlignedBeams,
    BaseCTCDecoder,
)
from ctc_asr_inference.ctc_decoding.logit_aligned_transcript import (
    LogitAlignedTranscript,
)


@dataclass
class VocabFromHFTokenizer(Buildable, list[str]):
    tokenizer_name_or_path: str | (PrefixSuffix | Wav2Vec2CTCTokenizer)

    def _build_self(self) -> None:
        assert len(self) == 0
        self._tokenizer = take_or_load_hfctc_tokenizer(self.tokenizer_name_or_path)
        vocab: list[str] = list(self._tokenizer.get_vocab().keys())

        self.extend(vocab)


def take_or_load_hfctc_tokenizer(
    tokenizer: str | (PrefixSuffix | Wav2Vec2CTCTokenizer),
) -> Wav2Vec2CTCTokenizer:
    return (  # pyright: ignore [reportUnknownVariableType]
        tokenizer
        if isinstance(tokenizer, Wav2Vec2CTCTokenizer)
        else AutoTokenizer.from_pretrained(str(tokenizer))  # pyright: ignore [reportUnknownMemberType]
    )


@dataclass
class HFCTCDecoder(BaseCTCDecoder, Buildable):
    # TODO: remove this?
    vocab: list[str]  # if its a buildable it might seem empty
    # tokenizer_name_or_path: Union[str, PrefixSuffix]
    # _tokenizer: PreTrainedTokenizer = field(init=False)  # default=UNDEFINED ?

    # def _build_self(self) -> Any:
    #     self._tokenizer = AutoTokenizer.from_pretrained(
    #         str(self.tokenizer_name_or_path)
    #     )
    #     return self
    #
    # @property
    # def vocab(self):
    #     return list(self._tokenizer.get_vocab().keys())


@dataclass
class HFCTCGreedyDecoder(BaseCTCDecoder, Buildable):
    """
    huggingface does not have a "proper" greedy decoder, but does argmax somewhere in the asr-pipeline
    see: https://github.com/huggingface/transformers/blob/7999ec125fc31428ed6879bf01bb013483daf704/src/transformers/pipelines/automatic_speech_recognition.py#L323

    method called: convert_tokens_to_string in tokenization_wav2vec2
    see: https://github.com/huggingface/transformers/blob/7999ec125fc31428ed6879bf01bb013483daf704/src/transformers/models/wav2vec2/tokenization_wav2vec2.py#L254
    does ctc to text conversion (collapsing the sequence)
    """

    tokenizer_name_or_path: str | (PrefixSuffix | Wav2Vec2CTCTokenizer)
    _tokenizer: PreTrainedTokenizer | None = field(init=False, default=None)

    def _build_self(self) -> Any:
        self._tokenizer = take_or_load_hfctc_tokenizer(self.tokenizer_name_or_path)

    @property
    def vocab(self) -> list[str]:
        return list(self._tokenizer.get_vocab().keys())

    def ctc_decode(self, logits: NumpyFloat2DArray) -> AlignedBeams:
        greedy_path = torch.argmax(torch.from_numpy(logits), dim=-1).squeeze()
        out: Wav2Vec2CTCTokenizerOutput = (  # noqa: ANN hugginface got wrong type hint!
            self._tokenizer.decode(
                token_ids=greedy_path,
                output_char_offsets=True,
                skip_special_tokens=False,  # for ctc (see huggingface/transformers)
            )
        )
        char_offsets: list[dict] = out.char_offsets
        vocab_space = [" ", *self.vocab]
        vocab_space = [
            c for c in vocab_space if c not in {"<pad>", "<s>", "</s>", "<unk>", "|"}
        ]

        char_offsets = list(filter(lambda d: d["char"] in vocab_space, char_offsets))
        if len(char_offsets) == 0:
            char_offsets = [{"char": " ", "start_offset": 0}]

        return [
            LogitAlignedTranscript(
                text="".join([d["char"] for d in char_offsets]),
                logit_ids=[int(d["start_offset"]) for d in char_offsets],
            ),
        ]
