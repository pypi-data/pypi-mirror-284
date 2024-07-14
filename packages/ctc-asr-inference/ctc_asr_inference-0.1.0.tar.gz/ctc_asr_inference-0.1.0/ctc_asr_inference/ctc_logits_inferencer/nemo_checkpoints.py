from dataclasses import dataclass
from pathlib import Path
from typing import Any

import nemo.collections.asr as nemo_asr
from beartype.door import is_bearable
from buildable_dataclasses.buildable_data import BuildableData
from misc_python_utils.beartypes import NeStr
from misc_python_utils.prefix_suffix import PrefixSuffix
from misc_python_utils.slugification import SlugStr, slugify_with_underscores

SAME_AS_NAME = "<SAME_AS_NAME>"


@dataclass(kw_only=True)
class NemoCheckpoint(BuildableData):
    name: NeStr
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
        return Path(self.model_file).is_file()

    def _build_data(self) -> Any:
        # see: tools/ctc_segmentation/scripts/run_ctc_segmentation.py in nemo-code
        model_name: str = self.model_name_or_path
        if Path(model_name).is_dir():
            raise NotImplementedError
            _model = nemo_asr.models.EncDecCTCModel.restore_from(model_name)  # pyright: ignore [reportUnreachable]
        elif model_name == "stt_de_quartznet15x5":  # TODO!  # noqa: RET506
            _model = nemo_asr.models.EncDecCTCModel.from_pretrained(
                model_name,
                strict=False,
            )
        else:
            _model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained(
                model_name,
                strict=False,
            )
        # else:
        #     raise ValueError(
        #         f"{model_name} not a valid model name or path. Provide path to the pre-trained checkpoint "
        #         f"or choose from {nemo_asr.models.EncDecCTCModelBPE.list_available_models()}"
        #     )

        _model.save_to(self.model_file)

    @property
    def model_file(self) -> str:
        return f"{self.data_dir}/model.nemo"
