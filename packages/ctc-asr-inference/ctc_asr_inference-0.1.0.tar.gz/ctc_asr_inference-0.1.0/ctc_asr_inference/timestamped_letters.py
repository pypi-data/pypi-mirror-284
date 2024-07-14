from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np
from misc_python_utils.beartypes import NeNpFloatDim1, NeNpIntDim1, NeStr
from misc_python_utils.slugification import CasedNameSlug
from speech_utils.data_models.audio_array_models import AudioArray
from speech_utils.data_models.enter_exit_service import EnterExitService
from speech_utils.data_models.misc_data_types import EmptySeq
from typing_extensions import Self


@dataclass
class NeTimestampedLetters:
    letters: NeStr  # TODO: why did I allow this to be empty?
    timestamps: NeNpFloatDim1

    def __post_init__(self) -> None:
        self._validate_data()

    def _validate_data(self) -> None:
        strictly_increasing = np.all(
            np.diff(self.timestamps) > 0,
        )  # this must not be relaxed!
        assert (
            strictly_increasing
        ), f"{self.timestamps=}\n{np.argwhere(np.diff(self.timestamps) <= 0)}"
        assert len(self.letters) == len(self.timestamps)

    def __len__(self) -> int:
        return len(self.letters)

    def slice_(self, those: NeNpIntDim1) -> Self:
        return NeTimestampedLetters(  # pyright: ignore [reportReturnType]
            "".join([self.letters[i] for i in those]),
            self.timestamps[those],
        )


TimestampedLetters = NeTimestampedLetters


@dataclass
class AudioArray2TimestampledLetters(EnterExitService, ABC):
    name: CasedNameSlug

    @abstractmethod
    def audio_to_segmented_transcripts(
        self,
        audio_array: AudioArray,
    ) -> NeTimestampedLetters | EmptySeq[object]:  # either non-empty or nothing (None)!
        # TODO: Result[NeTimestampedLetters, str]
        ...
