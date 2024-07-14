import logging
import operator
from dataclasses import dataclass, field
from functools import cached_property
from typing import ClassVar

import torch
from misc_python_utils.beartypes import NeNpFloatDim1, TorchTensor2D
from misc_python_utils.slugification import CasedNameSlug
from python_text_cleaning.asr_text_cleaning import Casing, Letters, determine_casing
from transformers import Wav2Vec2CTCTokenizer, Wav2Vec2ForCTC, Wav2Vec2Processor
from typing_extensions import Self

from ctc_asr_inference.ctc_logits_inferencer.asr_logits_inferencer import (
    ASRLogitsInferencer,
)
from ctc_asr_inference.ctc_logits_inferencer.huggingface_checkpoints import (
    HfModelFromCheckpoint,
)

logger = logging.getLogger(__name__)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


@dataclass
class HFWav2Vec2LogitsInferencer(ASRLogitsInferencer):
    checkpoint: HfModelFromCheckpoint
    do_normalize: bool = True  # TODO: not sure yet what is better at inference time
    is_bpe: ClassVar[bool] = False

    _processor: Wav2Vec2Processor | None = field(
        init=False,
        repr=False,
        default=None,
    )
    _model: torch.nn.Module | None = field(init=False, repr=False, default=None)
    name: CasedNameSlug = field(init=False)

    def __post_init__(self):
        self.name = f"hf-inferencer-{self.checkpoint.name}"

    def _build_self(self) -> Self:
        self._processor = self._load_prepare_processor()
        self._model = Wav2Vec2ForCTC.from_pretrained(self.checkpoint.model_path)
        self._model = self._model.to(DEVICE)
        casing = determine_casing(self.letter_vocab)
        fix_hf_ctc_tokenizers_casing(casing, self._processor.tokenizer)
        return self

    def _load_prepare_processor(self) -> Wav2Vec2Processor:
        pr = Wav2Vec2Processor.from_pretrained(self.checkpoint.model_path)
        pr.feature_extractor.do_normalize = self.do_normalize
        pr.feature_extractor.return_attention_mask = True
        return pr

    @property
    def letter_vocab(self) -> Letters:
        return "".join([l for l in self.vocab if len(l) == 1])

    @cached_property
    def vocab(self) -> list[str]:
        return [
            k
            for k, i in sorted(
                self._processor.tokenizer.get_vocab().items(),
                key=operator.itemgetter(1),
            )
        ]

    def calc_logits(self, audio: NeNpFloatDim1) -> TorchTensor2D:
        features = self._processor(
            audio,
            sampling_rate=self.asr_model_sample_rate,
            return_tensors="pt",
            # padding=True, #TODO why was this set to true?
            # return_attention_mask=True,
        )
        device = next(self._model.parameters()).device
        with torch.no_grad():
            logits = (
                self._model(
                    features.input_values.to(device),
                    attention_mask=features.attention_mask.to(device),
                )
                .logits.cpu()
                .squeeze()
            )
        assert logits.shape[1] == len(self.vocab), f"{logits.shape=},{len(self.vocab)=}"
        return logits


def fix_hf_ctc_tokenizers_casing(
    casing: Casing,
    tokenizer: Wav2Vec2CTCTokenizer,
) -> None:
    """
    do_lower_case means .upper() in huggingface/transformers!! see: https://github.com/huggingface/transformers/blob/870ff9e1dab249e4ffd8363ce132aa5145c94604/src/transformers/models/wav2vec2/tokenization_wav2vec2.py#L240
    """
    if casing is Casing.UPPER:
        if not tokenizer.do_lower_case:
            tokenizer.do_lower_case = True
            # maybe this happens for having finetuned an old model?

        logger.info(f"{tokenizer.do_lower_case=} is upper-cased")
    else:
        assert not tokenizer.do_lower_case
        logger.info(f"{tokenizer.do_lower_case=} is lower-cased")


#
# @dataclass
# class OnnxHFWav2Vec2LogitsInferencer(HFWav2Vec2LogitsInferencer):
#     checkpoint: OnnxedHFCheckpoint = UNDEFINED
#
#     def _build_self(self) -> "OnnxHFWav2Vec2LogitsInferencer":
#         self._processor = self._load_prepare_processor()
#
#         import onnx
#
#         onnx_model = onnx.load(self.checkpoint.onnx_model)
#         onnx.checker.check_model(onnx_model)
#
#         import onnxruntime as rt
#
#         sess_options = rt.SessionOptions()
#         sess_options.graph_optimization_level = rt.GraphOptimizationLevel.ORT_ENABLE_ALL
#         self._session = rt.InferenceSession(self.checkpoint.onnx_model, sess_options)
#         return self
#
#
#     def _infer_logits(self, features: BatchFeature) -> TorchTensor2D:
#         input_values = features.input_values
#         onnx_outputs = self._session.run(
#             None, {self._session.get_inputs()[0].name: input_values.numpy()}
#         )[0]
#         return torch.from_numpy(onnx_outputs.squeeze())
