from pathlib import Path
from typing import Annotated, Any, Callable, ClassVar, Generic, Iterable, List, Optional, Sequence, Tuple, TypeVar, Union
from typing_extensions import TypedDict
import numpy as np
import numpy.typing as npt
import pydantic_numpy.typing as pnd
from pydantic import BaseModel, FilePath, GetJsonSchemaHandler, PositiveInt, ValidationError, create_model, validate_call, field_validator
from pydantic_core import PydanticCustomError
from pydantic.json_schema import JsonSchemaValue
from pydantic_core.core_schema import (
        CoreSchema,
        chain_schema,
        is_instance_schema,
        json_or_python_schema,
        json_schema,
        no_info_plain_validator_function,
        plain_serializer_function_ser_schema,
        union_schema,
)
from pydantic_numpy.helper.annotation import (
        MultiArrayNumpyFile,
        NpArrayPydanticAnnotation,
        pd_np_native_numpy_array_to_data_dict_serializer,
)
from pydantic_numpy.helper.validation import (
        create_array_validator,
        validate_multi_array_numpy_file,
        validate_numpy_array_file,
)


SupportedDTypes = type[np.generic]
from pydantic_core import core_schema  # noqa: 


def create_array_validator(shape: Tuple[int, ...] | None, np_dtype: SupportedDTypes | None) -> Callable[[Any], npt.NDArray]:
    def array_validator(array_data: Any) -> npt.NDArray:
        if isinstance(array_data, dict):
            array = np.array(array_data["data"], dtype=array_data.get("dtype", None))
        elif isinstance(array_data, (list, tuple, np.ndarray)):
            array = np.array(array_data)
        else:
            raise ValueError(f"Unsupported type for array_data: {type(array_data)}")

        if shape is not None:
            print(f"Shape is not none: {shape}")
            expected_ndim = len(shape)
            actual_ndim = array.ndim
            if actual_ndim != expected_ndim:
                raise ValueError(f"Array has {actual_ndim} dimensions, expected {expected_ndim}")
            for i, (expected, actual) in enumerate(zip(shape, array.shape)):
                if expected != -1 and expected is not None and expected != actual:
                    raise ValueError(f"Dimension {i} has size {actual}, expected {expected}")

        if np_dtype:
            if array.dtype.type != np_dtype:
                if issubclass(np_dtype, np.integer) and issubclass(array.dtype.type, np.floating):
                    array = np.round(array).astype(np_dtype, copy=False)
                else:
                    array = array.astype(np_dtype, copy=True)

        return array
    return array_validator

class NumpyDataDict(TypedDict):
    data: List
    data_type: SupportedDTypes

@validate_call
def _deserialize_numpy_array_from_data_dict(data_dict: NumpyDataDict) -> np.ndarray:
    return np.array(data_dict["data"]).astype(data_dict["data_type"])


_common_numpy_array_validator = core_schema.union_schema(
    [
        core_schema.chain_schema(
            [
                core_schema.is_instance_schema(Path),
                core_schema.no_info_plain_validator_function(validate_numpy_array_file),
            ]
        ),
        core_schema.chain_schema(
            [
                core_schema.is_instance_schema(MultiArrayNumpyFile),
                core_schema.no_info_plain_validator_function(validate_multi_array_numpy_file),
            ]
        ),
        core_schema.is_instance_schema(np.ndarray),
        core_schema.chain_schema(
            [
                core_schema.is_instance_schema(Sequence),
                core_schema.no_info_plain_validator_function(lambda v: np.asarray(v)),
            ]
        ),
        core_schema.chain_schema(
            [
                core_schema.is_instance_schema(dict),
                core_schema.no_info_plain_validator_function(_deserialize_numpy_array_from_data_dict),
            ]
        ),
    ]
)


def pd_np_native_numpy_array_json_schema_from_type_data(
    _field_core_schema: core_schema.CoreSchema,
    _handler: GetJsonSchemaHandler,
    shape: List[PositiveInt] | None = None,
    data_type: SupportedDTypes | None = None,
) -> JsonSchemaValue:
    """Generates a JSON schema for a NumPy array field within a Pydantic model.

    This function constructs a JSON schema definition compatible with Pydantic models
    that are intended to validate NumPy array inputs. It supports specifying the data type
    and dimensions of the NumPy array, which are used to construct a schema that ensures
    input data matches the expected structure and type.

    Parameters
    ----------
    _field_core_schema : core_schema.CoreSchema
        The core schema component of the Pydantic model, used for building basic schema structures.
    _handler : GetJsonSchemaHandler
        A handler function or object responsible for converting Python types to JSON schema components.
    shape : Optional[List[PositiveInt]], optional
        The expected shape of the NumPy array. If specified, the schema will enforce that the input
    data_type : Optional[SupportedDTypes], optional
        The expected data type of the NumPy array elements. If specified, the schema will enforce
        that the input array's data type is compatible with this. If `None`, any data type is allowed,
        by default None.

    Returns:
    -------
    JsonSchemaValue
        A dictionary representing the JSON schema for a NumPy array field within a Pydantic model.
        This schema includes details about the expected array dimensions and data type.
    """
    array_shape = shape if shape else "Any"

    if data_type:
        array_data_type = data_type.__name__
        item_schema = core_schema.list_schema(
            items_schema=core_schema.any_schema(metadata=f"Must be compatible with numpy.dtype: {array_data_type}"),
        )
    else:
        array_data_type = "Any"
        item_schema = core_schema.list_schema(items_schema=core_schema.any_schema())

    if shape:
        data_schema = core_schema.list_schema(items_schema=item_schema, min_length=shape[0], max_length=shape[0])
    else:
        data_schema = item_schema

    return {
        "title": "Numpy Array",
        "type": f"np.ndarray[{array_shape }, np.dtype[{array_data_type}]]",
        "required": ["data_type", "data"],
        "properties": {
            "data_type": {"title": "dtype", "default": array_data_type, "type": "string"},
            "data": data_schema,
        },
    }

class NumpyArray:
    shape: ClassVar[Tuple[PositiveInt, ...] | None] = None
    np_dtype: ClassVar[SupportedDTypes | None] = None

    @classmethod
    def __class_getitem__(cls, params=None) -> Any:
        _shape = None
        _np_dtype = None
        if params is None or params == "*" or params == Any or params == (Any,):
            params = ("*",)
        if not isinstance(params, tuple):
            params = (params,)
        if len(params) == 1:
            if isinstance(params[0], type):
                _np_dtype = params[0]
        else:
            *_shape, _np_dtype = params
            _shape = tuple(s if s not in ("*", Any) else -1 for s in _shape)

        if _np_dtype is int:
            _np_dtype: SupportedDTypes | None = np.int64
        elif _np_dtype is float:
            _np_dtype = np.float64
        elif _np_dtype is not None and _np_dtype != "*" and _np_dtype != Any:
            _np_dtype = np.dtype(_np_dtype).type
        else:
            _np_dtype = None

        print(f"Shape: {_shape}, Data type: {_np_dtype}")
        if _shape == ():
            _shape = None
        class ParameterizedNumpyArray(cls):
            shape = _shape
            np_dtype = _np_dtype

        return Annotated[np.ndarray | FilePath | MultiArrayNumpyFile, ParameterizedNumpyArray]



    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        np_array_validator = create_array_validator(cls.shape, cls.np_dtype)
        np_array_schema = core_schema.no_info_plain_validator_function(np_array_validator)

        return core_schema.json_or_python_schema(
            python_schema=core_schema.chain_schema([
                core_schema.union_schema([
                    core_schema.is_instance_schema(np.ndarray),
                    core_schema.is_instance_schema(list),
                    core_schema.is_instance_schema(tuple),
                    core_schema.is_instance_schema(dict),
                ]),
                np_array_schema
            ]),
            json_schema=core_schema.chain_schema([
                core_schema.union_schema([
                    core_schema.list_schema(),
                    core_schema.dict_schema(),
                ]),
                np_array_schema
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                pd_np_native_numpy_array_to_data_dict_serializer,
                is_field_serializer=False,
                when_used="json-unless-none",
            ),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, field_core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return pd_np_native_numpy_array_json_schema_from_type_data(field_core_schema, handler, cls.shape, cls.np_dtype)

