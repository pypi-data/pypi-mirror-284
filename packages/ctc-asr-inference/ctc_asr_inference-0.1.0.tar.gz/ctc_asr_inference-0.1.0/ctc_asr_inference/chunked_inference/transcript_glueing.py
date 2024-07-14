import difflib
import logging
from dataclasses import dataclass

import numpy as np
from misc_python_utils.beartypes import NeList
from misc_python_utils.utils import Singleton

from ctc_asr_inference.timestamped_letters import TimestampedLetters

logger = logging.getLogger(
    __name__,
)

"""
───▄▄▄
─▄▀░▄░▀▄
─█░█▄▀░█
─█░▀▄▄▀█▄█▄▀
▄▄█▄▄▄▄███▀

"""


@dataclass
class _NO_NEW_SUFFIX(metaclass=Singleton):  # noqa: N801
    """
    I guess this is a dataclass to enable serialization?
    """


@dataclass(frozen=True, slots=True)
class GluePoint:
    left: int
    right: int


NO_NEW_SUFFIX = _NO_NEW_SUFFIX()


def calc_new_suffix(
    left: TimestampedLetters,
    right: TimestampedLetters,
    sm: difflib.SequenceMatcher,
) -> TimestampedLetters | _NO_NEW_SUFFIX:
    """
    two overlapping sequences

    left:_____----:-
    right:_______-:----

    colon is glue-point which is to be found

    return new suffix
    """
    min_left_len = 3
    is_overlapping = (
        left.timestamps[-1] > right.timestamps[0] and len(left.letters) >= min_left_len
    )
    if not is_overlapping:
        if left.letters[-1] != " " and right.letters[0] != " ":
            one_ms_before_start = np.array([right.timestamps[0] - 0.001])
            new_suffix = TimestampedLetters(
                " " + right.letters,
                np.concatenate([one_ms_before_start, right.timestamps]),
            )
        else:
            new_suffix = right

    else:
        left_cut = _cut_left(left, right, sm)
        matches = [m for m in sm.get_matching_blocks() if m.size > 0]

        if len(matches) > 0:
            gp: GluePoint = _calc_glue_points(
                left_cut.letters,
                matches,
            )
            logger.debug(
                f"{left_cut.letters[:gp.left]}---{right.letters[gp.right:]}",
            )
            assert left_cut.letters[gp.left] == right.letters[gp.right]
            new_suffix = TimestampedLetters(
                right.letters[(gp.right) :],
                right.timestamps[(gp.right) :],
            )
            _fix_new_suffixs_start_timestamps(
                new_suffix,
                left_end=float(left_cut.timestamps[gp.left]),
            )
            assert left_cut.timestamps[gp.left] == new_suffix.timestamps[0]

        else:
            new_suffix = NO_NEW_SUFFIX
            logger.warning(f"no matches for: '{left.letters}' <and> '{right.letters}'")

    return new_suffix


ONE_MS = 0.001


def _fix_new_suffixs_start_timestamps(
    new_suffix: TimestampedLetters,
    left_end: float,
) -> None:
    ts = new_suffix.timestamps
    time_diff = left_end - ts[0]
    ts[0] += time_diff
    for k in range(len(ts)):
        if ts[k] >= ts[k + 1]:
            ts[k + 1] = ts[k] + ONE_MS
        else:
            break
    # if k > 5:  # noqa: PLR2004
    #     logger.warning(f"needed to correct {k} following timestamps!")
    new_suffix._validate_data()  # noqa: SLF001


def _calc_glue_points(
    left_cut_text: str,
    matches: list[difflib.Match],
) -> GluePoint:
    aligned_idx = [(m.a + k, m.b + k) for m in matches for k in range(m.size)]
    dist_to_middle = [np.abs(i - round(len(left_cut_text) / 2)) for i, _ in aligned_idx]
    match_idx_closest_to_middle = np.argmin(dist_to_middle)
    glue_point_left, glue_point_right = aligned_idx[match_idx_closest_to_middle]
    return GluePoint(glue_point_left, glue_point_right)


def _cut_left(
    left: TimestampedLetters,
    right: TimestampedLetters,
    sm: difflib.SequenceMatcher,
) -> TimestampedLetters:
    """
    1. from left cut away what reaches too far into past
        left:________-:-
    2. from right cut away what reaches too far into future -> just for alignmend-method
        right:_______-:--
    3. find matches
    """
    tol = 0.5  # seconds:  for some reason I wanted half a second "space" to the left

    left_cut = left.slice_(
        np.argwhere(left.timestamps > right.timestamps[0] - tol).squeeze(1),
    )
    assert len(left_cut.letters) > 0
    cut_right_just_to_help_alingment = right.slice_(
        np.argwhere(right.timestamps < left.timestamps[-1]).squeeze(1),
    )

    assert len(cut_right_just_to_help_alingment.letters) > 0
    sm.set_seqs(left_cut.letters, cut_right_just_to_help_alingment.letters)
    return left_cut


def accumulate_transcript_suffixes(
    suffixes: NeList[TimestampedLetters],
) -> TimestampedLetters:
    prefix = (
        None  # just to calm-down pycharm, no real need for it cause suffixes is NeList!
    )
    for suffix in suffixes:
        prefix = remove_and_append(prefix, suffix) if prefix is not None else suffix
    return prefix


def remove_and_append(
    prefix: TimestampedLetters,
    suffix: TimestampedLetters,
) -> TimestampedLetters:
    prefix = prefix.slice_(
        np.argwhere(prefix.timestamps < suffix.timestamps[0]).squeeze(1),
    )
    return TimestampedLetters(
        prefix.letters + suffix.letters,
        np.concatenate([prefix.timestamps, suffix.timestamps]),
    )
