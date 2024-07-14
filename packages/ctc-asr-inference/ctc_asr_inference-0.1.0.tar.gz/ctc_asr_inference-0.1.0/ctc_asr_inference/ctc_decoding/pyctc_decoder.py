import itertools
import logging
from dataclasses import dataclass, field
from typing import Annotated

from beartype.vale import Is
from misc_python_utils.beartypes import NumpyFloat2DArray, nobeartype
from misc_python_utils.file_utils.readwrite_files import read_lines
from pyctcdecode.constants import DEFAULT_UNK_LOGP_OFFSET
from pyctcdecode.decoder import (
    BeamSearchDecoderCTC,
    LMState,
    WordFrames,
    build_ctcdecoder,
)

from ctc_asr_inference.ctc_decoding.ctc_decoding import AlignedBeams
from ctc_asr_inference.ctc_decoding.huggingface_ctc_decoding import HFCTCDecoder
from ctc_asr_inference.ctc_decoding.lm_model_for_pyctcdecode import (
    NgramLmAndUnigrams,
)
from ctc_asr_inference.ctc_decoding.logit_aligned_transcript import (
    LogitAlignedTranscript,
)

logger = logging.getLogger(__name__)

LmModelFile = Annotated[
    str,
    Is[lambda s: any(s.endswith(suffix) for suffix in [".bin", ".arpa"])],
]


@nobeartype  # TODO: beartype panics! maybe because of LMState
@dataclass
class OutputBeamDc:
    """
    just to bring order into pyctcdecode's mess
    """

    text: str
    last_lm_state: LMState
    text_frames: list[WordFrames]
    logit_score: float
    lm_score: float

    def __post_init__(self) -> None:
        if len(self.text) == 0:
            self.text = " "
            assert len(self.text_frames) == 0
            self.text_frames = [(" ", (0, 0))]

        assert self.text == " ".join([token for token, _ in self.text_frames])


#
# def build_alphabet(labels: list[str], is_bpe: bool):
#     """
#     based on : Alphabet.build_alphabet -method
#     only difference: does not attempt to infer "is_bpe" but takes it as argument
#     """
#     _verify_alphabet(labels, is_bpe)
#     if is_bpe:
#         normalized_labels = _normalize_bpe_alphabet(labels)
#     else:
#         normalized_labels = _normalize_regular_alphabet(labels)
#     alphabet = Alphabet(normalized_labels, is_bpe)
#     return alphabet
#
#
# def build_ctcdecoder(
#     labels: list[str],
#     kenlm_model_path: Optional[str] = None,
#     unigrams: Optional[Collection[str]] = None,
#     alpha: float = DEFAULT_ALPHA,
#     beta: float = DEFAULT_BETA,
#     unk_score_offset: float = DEFAULT_UNK_LOGP_OFFSET,
#     lm_score_boundary: bool = DEFAULT_SCORE_LM_BOUNDARY,
#     is_bpe: bool = False,
# ) -> BeamSearchDecoderCTC:
#     """
#     based on: build_ctcdecoder method in pyctcdecode/decoder.py
#     Build a BeamSearchDecoderCTC instance with main functionality.
#
#
#     Args:
#         labels: class containing the labels for input logit matrices
#         kenlm_model_path: path to kenlm n-gram language model
#         unigrams: list of known word unigrams
#         alpha: weight for language model during shallow fusion
#         beta: weight for length score adjustment of during scoring
#         unk_score_offset: amount of log score offset for unknown tokens
#         lm_score_boundary: whether to have kenlm respect boundaries when scoring
#
#     Returns:
#         instance of BeamSearchDecoderCTC
#     """
#     kenlm_model = None if kenlm_model_path is None else kenlm.Model(kenlm_model_path)
#     if kenlm_model_path is not None and kenlm_model_path.endswith(".arpa"):
#         print(
#             "Using arpa instead of binary LM file, decoder instantiation might be slow."
#         )
#     if unigrams is None and kenlm_model_path is not None:
#         if kenlm_model_path.endswith(".arpa"):
#             unigrams = load_unigram_set_from_arpa(kenlm_model_path)
#         else:
#             print(
#                 "Unigrams not provided and cannot be automatically determined from LM file (only "
#                 "arpa format). Decoding accuracy might be reduced."
#             )
#
#     alphabet = build_alphabet(labels, is_bpe)
#     if unigrams is not None:
#         verify_alphabet_coverage(alphabet, unigrams)
#     if kenlm_model is not None:
#         language_model: Optional[AbstractLanguageModel] = LanguageModel(
#             kenlm_model,
#             unigrams,
#             alpha=alpha,
#             beta=beta,
#             unk_score_offset=unk_score_offset,
#             score_boundary=lm_score_boundary,
#         )
#     else:
#         language_model = None
#     return BeamSearchDecoderCTC(alphabet, language_model)


@dataclass
class PyCTCKenLMDecoder(HFCTCDecoder):
    """
    here is huggingface's decode method: https://github.com/huggingface/transformers/blob/f275e593bfeb41b31ac8a124a9314cbd6088bfd1/src/transformers/models/wav2vec2_with_lm/processing_wav2vec2_with_lm.py#L346
    """

    lm_weight: float
    beta: float
    # cannot do this with beartype NeList[str] for vocab, cause it might be a CachedList
    # vocab: Union[_UNDEFINED, list[str]] = UNDEFINED

    ngram_lm_model: NgramLmAndUnigrams
    num_best: int = 1  # number of beams to return
    beam_size: int = 100
    unk_offset: float = DEFAULT_UNK_LOGP_OFFSET

    _pyctc_decoder: BeamSearchDecoderCTC = field(
        init=False,
        repr=False,
    )

    def _build_self(self) -> None:
        if self.ngram_lm_model.unigrams_filepath:
            unigrams = list(read_lines(self.ngram_lm_model.unigrams_filepath))
            small_vocab = 10_000
            if len(unigrams) < small_vocab:
                logger.warning(
                    f"{self.ngram_lm_model.name} only got {len(unigrams)} unigrams",
                )

            logger.debug(f"{len(unigrams)=}")
        else:
            unigrams = None
        self._pyctc_decoder = build_ctcdecoder(
            labels=self.vocab,
            kenlm_model_path=self.ngram_lm_model.ngramlm_filepath,
            unigrams=unigrams,
            alpha=self.lm_weight,  # tuned on a val set
            beta=self.beta,  # tuned on a val set
            unk_score_offset=self.unk_offset,
        )
        logger.info(f"{BeamSearchDecoderCTC.model_container.keys()=}")
        assert (
            len(BeamSearchDecoderCTC.model_container.keys()) > 0
        ), f"{BeamSearchDecoderCTC.model_container.keys()=}"

    def ctc_decode(
        self,
        logits: NumpyFloat2DArray,
    ) -> AlignedBeams:
        beams = [
            OutputBeamDc(*b)
            for b in self._pyctc_decoder.decode_beams(
                logits,
                beam_width=self.beam_size,
            )
        ]
        # logger.warning(f"decoded: {logits.shape}")
        return [
            LogitAlignedTranscript.create_from_token_spans(
                b.text_frames,
                b.logit_score,
                b.lm_score,
            )
            for b in itertools.islice(beams, self.num_best)
        ]

    # def __del__(self) -> None:
    #     # for __del__ vs __delete__ see: https://stackoverflow.com/questions/59508235/what-is-the-difference-between-del-and-delete
    #     if hasattr(self,"_pyctc_decoder"):
    #         self._pyctc_decoder.cleanup()  # one has to manually cleanup!


PyCTCBinKenLMDecoder = PyCTCKenLMDecoder
"""
old stuff:


def build_unigrams_from_lexicon_file(
    lexicon_file: str, transcript_normalizer: TranscriptNormalizer
) -> NeList[str]:
    def parse_lexicon_file(l: str) -> str:
        s = "".join(l.split("\t")[1].split(" "))
        unigram = s.replace("|", "").strip(" ")
        assert " " not in unigram
        unigram = transcript_normalizer.apply(unigram)
        return unigram

    return list({parse_lexicon_file(l) for l in read_lines(lexicon_file)})
"""
