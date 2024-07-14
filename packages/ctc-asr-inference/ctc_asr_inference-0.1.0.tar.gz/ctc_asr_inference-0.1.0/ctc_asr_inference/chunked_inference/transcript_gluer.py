import difflib
import logging
import os
from dataclasses import dataclass, field

import numpy as np
from beartype.roar import BeartypeCallHintParamViolation
from buildable_dataclasses.buildable import Buildable
from misc_python_utils.utils import just_try

from ctc_asr_inference.chunked_inference.transcript_glueing import (
    _NO_NEW_SUFFIX,
    NO_NEW_SUFFIX,
    calc_new_suffix,
)
from ctc_asr_inference.timestamped_letters import TimestampedLetters

logger = logging.getLogger(__name__)
DEBUG = os.environ.get("DEBUG", "False").lower() != "false"

Seconds = float


@dataclass
class TranscriptGluer(Buildable):
    """
    ───▄▄▄
    ─▄▀░▄░▀▄
    ─█░█▄▀░█
    ─█░▀▄▄▀█▄█▄▀
    ▄▄█▄▄▄▄███▀

    """

    _prefix: TimestampedLetters | None = field(init=False, repr=False, default=None)
    max_buffer_duration: Seconds = 100.123
    seqmatcher: difflib.SequenceMatcher | None = field(
        init=False,
        repr=False,
        default=None,
    )

    def reset(self) -> None:
        self._prefix: TimestampedLetters | None = None

    def _build_self(self) -> None:
        self.reset()
        self.seqmatcher = difflib.SequenceMatcher()

    def calc_transcript_suffix(
        self,
        inp: TimestampedLetters,
    ) -> TimestampedLetters | _NO_NEW_SUFFIX:
        if self._prefix is None:
            self._prefix, new_suffix = inp, inp
        else:
            new_suffix = just_try(
                lambda: calc_new_suffix(
                    left=self._prefix,
                    right=inp,
                    sm=self.seqmatcher,
                ),
                default=NO_NEW_SUFFIX,
                # a failed glue does not add anything! In the hope that overlap is big enough so that it can be recovered by next glue!
                verbose=DEBUG,
                print_stacktrace=True,
                reraise=False,
            )
            if new_suffix is not NO_NEW_SUFFIX:
                try:
                    self._prefix = self._glue_and_trim(self._prefix, new_suffix)
                except BeartypeCallHintParamViolation:
                    logger.warning(
                        f"glueing failed with: {self._prefix=},{new_suffix=}",
                    )
        return new_suffix

    def _glue_and_trim(
        self,
        prefix: TimestampedLetters,
        new_suffix: TimestampedLetters,
    ) -> TimestampedLetters:
        prefix_to_keep = prefix.slice_(
            np.argwhere(prefix.timestamps < new_suffix.timestamps[0]).squeeze(1),
        )
        glued = TimestampedLetters(
            prefix_to_keep.letters + new_suffix.letters,
            np.concatenate([prefix_to_keep.timestamps, new_suffix.timestamps]),
        )
        return glued.slice_(
            np.argwhere(
                glued.timestamps > glued.timestamps[-1] - self.max_buffer_duration,
            ).squeeze(1),
        )
