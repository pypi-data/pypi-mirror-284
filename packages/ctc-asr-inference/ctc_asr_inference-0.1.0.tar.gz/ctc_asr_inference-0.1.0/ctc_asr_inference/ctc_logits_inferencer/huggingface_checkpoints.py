import importlib
import logging
import os
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from beartype.door import is_bearable
from buildable_dataclasses.buildable_data import BuildableData
from huggingface_hub.utils import LocalEntryNotFoundError
from misc_python_utils.beartypes import NeStr
from misc_python_utils.prefix_suffix import PrefixSuffix
from misc_python_utils.slugification import SlugStr, slugify_with_underscores
from transformers import AutoProcessor

HfPretrainedModelType = str

logger = logging.getLogger(
    __name__,
)  # "The name is potentially a period-separated hierarchical", see: https://docs.python.org/3.10/library/logging.html

SAME_AS_NAME = "<SAME_AS_NAME>"


@dataclass
class HfModelFromCheckpoint(BuildableData):
    name: NeStr
    # hf_model_type is necessary cause sometimes model-names are ambiguous, for "facebook/wav2vec2-base-960h" AutoModel resolves to the pretrained wav2vec2 without ctc-finetuning
    hf_model_type: HfPretrainedModelType
    base_dir: PrefixSuffix  # = field(default_factory=lambda: BASE_PATHES["am_models"])
    model_name_or_path: NeStr = SAME_AS_NAME

    def __post_init__(self) -> None:
        if self.model_name_or_path == SAME_AS_NAME:
            self.model_name_or_path = self.name
        self.name = slugify_with_underscores(self.name)
        is_bearable(self.name, SlugStr)
        assert len(self.name) > 0

    @property
    def model_path(self) -> str:
        model_folder = self.data_dir
        if not Path(model_folder).is_dir():
            model_folder = self.model_name_or_path
        return model_folder

    @property
    def _is_data_valid(self) -> bool:
        clazz = getattr(importlib.import_module("transformers"), self.hf_model_type)
        try:
            clazz.from_pretrained(self.data_dir, local_files_only=True)
            return True  # noqa: TRY300
        except (OSError, LocalEntryNotFoundError):
            return False

    def _build_data(self) -> Any:
        if Path(self.model_name_or_path).is_dir():
            _export_model_files_from_checkpoint_dir(
                self.model_name_or_path,
                self.data_dir,
            )
            logger.info(f"exported {self.model_name_or_path=} to {self.data_dir=}")
        else:
            clazz = getattr(importlib.import_module("transformers"), self.hf_model_type)
            clazz.from_pretrained(self.model_name_or_path).save_pretrained(
                self.data_dir,
            )
            AutoProcessor.from_pretrained(self.model_name_or_path).save_pretrained(
                self.data_dir,
            )
            logger.info(f"downloaded {self.model_name_or_path=} to {self.data_dir=}")


def _export_model_files_from_checkpoint_dir(
    model_name_or_path: str,
    model_dir: str,
) -> None:
    os.makedirs(model_dir, exist_ok=True)  # noqa: PTH103
    needed_files = [
        "config.json",
        "pytorch_model.bin",
    ]
    for f in needed_files:
        file = f"{model_name_or_path}/{f}"
        assert Path(file).is_file(), f"cannot find {file}"
        shutil.copy(file, f"{model_dir}/")
    could_be_one_dir_above = [
        "preprocessor_config.json",
        "tokenizer_config.json",
        "vocab.json",
        "special_tokens_map.json",
    ]
    for f in could_be_one_dir_above:
        file = f"{model_name_or_path}/{f}"
        if not Path(file).is_file():
            file = f"{model_name_or_path}/../{f}"
        if Path(file).is_file():
            shutil.copy(file, f"{model_dir}/")
        else:
            allowed_to_be_missing = ["special_tokens_map.json"]
            assert f in allowed_to_be_missing
    # TODO: no need for special permissions it is just a cache!
    # os.system(f"chmod -R 555 {model_dir}")


#
#
# @dataclass
# class FinetunedCheckpoint(HfCheckpoint):
#     """
#     kind of creepy that it is not supposed to be instantiated "normally" but only using this staticmethod (from_cache_dir)
#     """
#
#     finetune_master: Union[_UNDEFINED, dict] = UNDEFINED
#
#     @staticmethod
#     def from_cache_dir(finetune_master_cache_dir: str) -> list["FinetunedCheckpoint"]:
#         s = read_file(f"{finetune_master_cache_dir}/dataclass.json")
#         finetune_master: dict = json.loads(
#             s.replace("_target_", CLASS_REF_NO_INSTANTIATE)
#         )
#
#         def get_finetune_task_cache_dir(fm):
#             # TODO: this is very hacky!
#             prefix_suffix = fm["finetune_client"]["task"]["cache_dir"]
#             prefix_suffix["_target_"] = prefix_suffix.pop("_python_dataclass_")
#             ps: PrefixSuffix = decode_dataclass(prefix_suffix)
#             # dirr = f"{prefix_suffix['prefix']}/{prefix_suffix['suffix']}"
#             return f"{ps}/output_dir"
#
#         task_cache_dir = get_finetune_task_cache_dir(finetune_master)
#         dcs = [str(p.parent) for p in Path(task_cache_dir).rglob("pytorch_model.bin")]
#
#         if len(dcs) == 0:
#             print(f"{task_cache_dir=} got no pytorch_model.bin -> remove it!!")
#
#         def checkpoint_name_suffix(ckpt_dir):
#             suff = ckpt_dir.replace(f"{task_cache_dir}/", "")
#             return f"-{suff}" if ckpt_dir != task_cache_dir else ""
#
#         return [
#             FinetunedCheckpoint(
#                 name=f"{finetune_master['name']}{checkpoint_name_suffix(ckpt_dir)}",
#                 finetune_master=finetune_master,
#                 model_name_or_path=ckpt_dir,
#             )
#             for ckpt_dir in dcs
#         ]
#
#
# @dataclass
# class OnnxedHFCheckpoint(HfCheckpoint):
#     vanilla_chkpt: HfCheckpoint = UNDEFINED
#     do_quantize: bool = True
#     weight_type_name: Optional[WeightTypeName] = None
#     name: NeStr = field(init=False)
#
#     def __post_init__(self):
#         suffix = "-quantized" if self.do_quantize else ""
#         self.name = f"{self.vanilla_chkpt.name}-onnx{suffix}"
#         super().__post_init__()
#
#     @property
#     def model_path(self) -> str:
#         return self.vanilla_chkpt.model_path
#
#     @property
#     def onnx_model(self) -> str:
#         return self._create_onnx_model_file(self.do_quantize)
#
#     def _create_onnx_model_file(self, do_quantize: bool):
#         suf = ".quant" if do_quantize else ""
#         return self.prefix_cache_dir(f"wav2vec2{suf}.onnx")
#
#     def _build_cache(self):
#         model_id_or_path = self.vanilla_chkpt.model_path
#         onnx_model_name = self._create_onnx_model_file(False)
#         convert_to_onnx(model_id_or_path, onnx_model_name)
#
#         if self.do_quantize:
#             quantized_model_name = self._create_onnx_model_file(True)
#             quantize_onnx_model(
#                 model_id_or_path=model_id_or_path,
#                 onnx_model_path=onnx_model_name,
#                 quantized_model_path=quantized_model_name,
#                 weight_type_name=self.weight_type_name,
#             )
#             os.remove(onnx_model_name)
#
#         import onnx
#
#         onnx_model = onnx.load(self.onnx_model)
#         onnx.checker.check_model(self.onnx_model)
