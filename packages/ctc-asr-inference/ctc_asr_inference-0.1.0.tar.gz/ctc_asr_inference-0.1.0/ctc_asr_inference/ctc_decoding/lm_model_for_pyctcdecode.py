import logging
import shutil
from abc import abstractmethod
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from buildable_dataclasses.hashcached_data.hashcached_data import HashCachedData
from building_kenlms.kenlm_arpa import ArpaFile, GotArpaFile
from misc_python_utils.beartypes import NeList
from misc_python_utils.file_utils.readwrite_files import read_lines, write_lines
from misc_python_utils.prefix_suffix import PrefixSuffix
from misc_python_utils.processing_utils.processing_utils import exec_command
from misc_python_utils.slugification import CasedNameSlug
from python_text_cleaning.character_mappings.text_cleaning import TextCleaner
from tqdm import tqdm

Model_Unigrams_File = tuple[str, str]

logger = logging.getLogger(__name__)


@dataclass
class NgramLmAndUnigrams(HashCachedData):
    cache_base: (
        PrefixSuffix  # = field(default_factory=lambda: BASE_PATHES["lm_models"])
    )

    @property
    @abstractmethod
    def ngramlm_filepath(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def unigrams_filepath(self) -> str | None:
        """
        pyctcdecode can also decode without a unigrams-file, even though it throws some warnings
        """
        raise NotImplementedError

    @property
    def data_dir(self) -> PrefixSuffix:
        return self.cache_dir  # pyright: ignore [reportReturnType]

    def _build_cache(self) -> None:
        """
        just because I am not sure yet whether it should be CachedData or BuildableData
        """
        self._build_data()

    @abstractmethod
    def _build_data(self) -> None:
        raise NotImplementedError

    # @property
    # def _is_data_valid(self) -> bool:
    #     no_need = not self.unigrams_filepath
    #     need_and_got_unigrams = no_need or Path.is_file(self.unigrams_filepath)
    #     return Path.is_file(self.ngramlm_filepath) and need_and_got_unigrams


@dataclass(kw_only=True)
class GzippedArpaAndUnigramsForPyCTCDecode(NgramLmAndUnigrams):
    raw_arpa: GotArpaFile
    transcript_cleaner: TextCleaner
    name: CasedNameSlug = field(init=False)

    def __post_init__(self):
        self.name = f"gzipped_arpa_unigrams-{self.raw_arpa.name}"

    @property
    def ngramlm_filepath(self) -> str:
        return f"{self.data_dir}/lm.arpa.gz"

    @property
    def unigrams_filepath(self) -> str:
        return f"{self.data_dir}/unigrams.txt.gz"

    def _build_data(self) -> Any:
        self._gzip_or_copy_arpa()
        unigrams = build_unigrams_from_arpa(
            self.ngramlm_filepath,
            transcript_cleaner=self.transcript_cleaner,
        )
        write_lines(self.unigrams_filepath, unigrams)

    def _gzip_or_copy_arpa(self) -> None:
        raw_arpa_file = self.raw_arpa.arpa_filepath
        assert Path(raw_arpa_file).is_file(), f"could not find {self.raw_arpa=}"
        if not raw_arpa_file.endswith(".gz"):
            out, err = exec_command(
                f"gzip -c {raw_arpa_file} > {self.ngramlm_filepath}",
            )
            if len(out) > 0:
                logger.info(f"{out=}")
            if len(err) > 0:
                logger.error(f"{err=}")
        else:
            shutil.copy(raw_arpa_file, self.ngramlm_filepath)
        assert Path(self.ngramlm_filepath).is_file()


def build_unigrams_from_arpa(
    arpa_file: ArpaFile,
    transcript_cleaner: TextCleaner,
) -> NeList[str]:
    unigrams = list(
        {
            l
            for raw in tqdm(
                gen_parse_arpa_file(arpa_file),
                desc="building unigrams, the LMs vocabulary",
            )
            for l in transcript_cleaner(raw).split(" ")
        },
    )

    if len(unigrams) < 10_000:  # noqa: PLR2004
        logger.warning(f"only got {len(unigrams)} unigrams!")  # noqa: T201
    assert all(" " not in s for s in unigrams)
    return unigrams


def gen_parse_arpa_file(arpa_file: str) -> Iterator[str]:
    TWO_COLUMS = 2  # see arpa-file

    for line in read_lines(arpa_file):
        if "2-grams:" in line:
            break
        elif len(line.split("\t")) >= TWO_COLUMS:
            yield line.split("\t")[1]


@dataclass(kw_only=True)
class KenLMBinaryUnigramsFile(NgramLmAndUnigrams):
    name: str
    kenlm_binary_file: PrefixSuffix
    unigrams_file: PrefixSuffix | None = None

    @property
    def ngramlm_filepath(self) -> str:
        return f"{self.data_dir}/{Path(str(self.kenlm_binary_file)).name}"

    @property
    def unigrams_filepath(self) -> str | None:
        return (
            f"{self.data_dir}/{Path(str(self.unigrams_file)).name}"
            if self.unigrams_file is not None
            else None
        )

    def _build_data(self) -> Any:
        shutil.copy(str(self.kenlm_binary_file), self.ngramlm_filepath)
        if self.unigrams_filepath:
            shutil.copy(str(self.unigrams_file), self.unigrams_filepath)
