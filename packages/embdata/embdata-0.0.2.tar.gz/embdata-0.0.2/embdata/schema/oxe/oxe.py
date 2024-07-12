# Copyright (c) 2024 Mbodi AI
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Copyright (c) 2024 Mbodi AI
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


import os
from typing import Any, Dict, Generator

import numpy as np
from pydantic import Field
from rich import print

from datasets import Dataset, DatasetInfo, Features, Value
from datasets import Image as HFImage
from datasets.splits import SplitInfo
from embdata.describe import describe
from embdata.ds.oxe.load import get_hf_dataset
from embdata.ds.oxe.schemas.xarm_utokyo_ds import (
    Observation,
    State,
    Step,
)
from embdata.episode import VisionMotorEpisode
from embdata.features import to_features_dict
from embdata.geometry import Pose
from embdata.image import Image
from embdata.motion.control import AbsoluteHandControl, RelativePoseHandControl
from embdata.sample import Sample


class Metadata(Sample):
    num_depth_cams: int | str = Field(0, alias="# Depth Cams")
    num_episodes: int | str = Field(0, alias="# Episodes")
    num_rgb_cams: int | str = Field(0, alias="# RGB Cams")
    num_wrist_cams: int | str = Field(0, alias="# Wrist Cams")
    action_space: str = Field("", alias="Action Space")
    control_frequency: str = Field("", alias="Control Frequency")
    data_collect_method: str = Field("", alias="Data Collect Method")
    dataset_name: str = Field("", alias="Dataset")
    description: str = Field("", alias="Description")
    file_size_gb: float | str = Field(0.0, alias="File Size (GB)")
    gripper: str = Field("", alias="Gripper")
    has_camera_calibration: str = Field("", alias="Has Camera Calibration?")
    has_proprioception: str = Field("", alias="Has Proprioception?")
    has_suboptimal: str = Field("", alias="Has Suboptimal?")
    language_annotations: float | str = Field(0.0, alias="Language Annotations")
    registered_dataset_name: str = Field("", alias="Registered Dataset Name")
    robot: str = Field("", alias="Robot")
    robot_morphology: str = Field("", alias="Robot Morphology")
    scene_type: str = Field("", alias="Scene Type")

