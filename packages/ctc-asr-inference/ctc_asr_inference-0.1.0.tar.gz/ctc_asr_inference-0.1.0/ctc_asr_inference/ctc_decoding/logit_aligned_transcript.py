from dataclasses import dataclass
from typing import Annotated

import numpy as np
from beartype.vale import Is
from misc_python_utils.beartypes import NeList, NeStr
from typing_extensions import Self

TokenSpans = list[tuple[str, tuple[int, int]]]


def is_weakly_monoton_increasing(seq: list[float | int]) -> bool:
    return bool(
        np.all(np.diff(seq) >= 0),
    )  # numpy.bool_ is not same as bool! even though it has the very same meaning!


@dataclass
class LogitAlignedTranscript:
    """
    Text is character-wise aligned to logits, no time-stamps here.
        logits == ctc-matrix
    """

    text: NeStr
    logit_ids: Annotated[
        NeList[int],
        Is[is_weakly_monoton_increasing],  # pyright: ignore [reportArgumentType]
    ]  # TODO: not too strict?

    logits_score: float | None = None
    lm_score: float | None = None

    def __post_init__(self) -> None:
        """Validate data."""
        have_same_len = len(self.text) == len(self.logit_ids)
        assert have_same_len, (
            f"{self.text=} and {self.logit_ids=} have different length! "  # noqa: ISC003
            + f"{len(self.text)=}!={len(self.logit_ids)=}"
        )

    @classmethod
    def create_from_token_spans(
        cls,
        token_spans: TokenSpans,
        lm_score: float,
        logits_score: float,
    ) -> Self:
        text = " ".join([tok for tok, _ in token_spans])
        return cls(
            text=text,
            logit_ids=charwise_idx_for_tokenspans_via_linear_interpolation(token_spans),
            lm_score=lm_score,
            logits_score=logits_score,
        )


def charwise_idx_for_tokenspans_via_linear_interpolation(
    token_spans: TokenSpans,
) -> list[int]:
    seq_idx = [
        round(start + (end - start) * k / len(word))  # interpolate
        for word, (start, end) in token_spans
        for k in range(len(word) + 1)
    ]
    return seq_idx[:-1]  # all but the last one, which is a space
