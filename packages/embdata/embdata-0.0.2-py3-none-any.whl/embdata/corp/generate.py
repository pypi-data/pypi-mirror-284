# Copyright (c) 2024 Mbodi AI
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import json
from pathlib import Path

from datamodel_code_generator import InputFileType
from datamodel_code_generator import generate as generate_code
from datasets import Dataset
from datasets.arrow_dataset import Dataset

from embdata.describe import dict_to_schema


def generate(schema_out_path, ds: Dataset, base_class="Sample", class_name="XarmUtokyoDataset"):
    schema = dict_to_schema({"episodes": ds})

    with open(schema_out_path, "w") as f:
        json.dump(schema, f, indent=2)

    generate_code(
        Path(schema_out_path),
        input_filename=Path(schema_out_path).stem,
        input_file_type=InputFileType.JsonSchema,
        output=Path(schema_out_path).with_suffix(".py"),
        base_class=base_class,
        class_name=class_name,
        snake_case_field=True,
        additional_imports=[
            "embdata.sample.Sample",
            "embdata.image.Image",
            "embdata.geometry.Pose",
            "embdata.motion_controls.AbsoluteHandControl",
            "embdata.motion_controls.RelativePoseHandControl",
        ],
        apply_default_values_for_required_fields=True,
    )
