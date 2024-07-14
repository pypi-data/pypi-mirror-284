import os  # noqa: F401
import shutil
import subprocess  # noqa: S404
import sys
from dataclasses import dataclass, field
from typing import Any

from misc_python_utils.slugification import CasedNameSlug

from ctc_asr_inference.ctc_decoding.lm_model_for_pyctcdecode import (
    GzippedArpaAndUnigramsForPyCTCDecode,
    NgramLmAndUnigrams,
)


@dataclass(kw_only=True)
class KenLMBinaryUnigramsFromArpa(NgramLmAndUnigrams):
    arpa_unigrams: GzippedArpaAndUnigramsForPyCTCDecode
    name: CasedNameSlug = field(init=False)

    def __post_init__(self):
        self.name = f"binary-{self.arpa_unigrams.name}"

    @property
    def ngramlm_filepath(self) -> str:
        return f"{self.data_dir}/kenlm.bin"

    @property
    def unigrams_filepath(self) -> str:
        return f"{self.data_dir}/unigrams.txt.gz"

    def _build_data(self) -> Any:
        build_binary_kenlm(
            "/opt/kenlm/bin",
            self.arpa_unigrams.ngramlm_filepath,
            self.ngramlm_filepath,
        )
        shutil.copy(str(self.arpa_unigrams.unigrams_filepath), self.unigrams_filepath)


def build_binary_kenlm(
    kenlm_bin_path: str,
    arpa_file: str,
    kenlm_binary_file: str,
) -> subprocess.CompletedProcess:
    """
    based on: "make_kenlm" method from https://github.com/NVIDIA/NeMo/blob/e859e43ef85cc6bcdde697f634bb3b16ee16bc6b/scripts/asr_language_modeling/ngram_lm/ngram_merge.py#L286
    Builds a language model from an ARPA format file using the KenLM toolkit.
    """
    sh_args = [
        f"{kenlm_bin_path}/build_binary",
        "trie",
        "-i",
        arpa_file,
        kenlm_binary_file,
    ]
    return subprocess.run(  # noqa: PLW1510, S603
        sh_args,  # noqa: S603
        capture_output=False,
        text=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
