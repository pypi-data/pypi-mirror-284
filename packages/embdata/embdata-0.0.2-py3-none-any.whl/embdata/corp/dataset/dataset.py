from typing import Any, Callable, List, Optional, Union, Dict, Type
from datasets import Dataset as HFDataset, IterableDataset
import numpy as np
import torch
from torch.utils.data import Dataset as TorchDataset
from gymnasium import spaces
from pydantic import Field
from embdata.sample import Sample
from embdata.episode import Episode, TimeStep


def default_loader(example: dict) -> Union[Episode, TimeStep]:
    if "steps" in example:
        return Episode(**example)
    return TimeStep(**example)


class Dataset(HFDataset, TorchDataset, Sample):
    """Unified Dataset for episodes and steps with efficient lazy loading, PyTorch compatibility,
    and enhanced data manipulation capabilities inherited from Sample.

    This class extends HuggingFace's Dataset, PyTorch's Dataset, and our custom Sample class,
    combining efficient lazy loading, PyTorch compatibility, and rich data manipulation methods.

    Attributes:
        item_type (Type[Union[Episode, TimeStep]]): The type of items in the dataset.
        loader (Callable): Function to convert dict items to Episode or TimeStep objects.
        metadata (Any): Metadata for the dataset.

    Key Methods:
        flatten_to(field: str) -> 'Dataset':
            Flatten the dataset to a specific field, like 'steps'.
        unflatten(parent_field: str, parent_class: Type[Episode] = Episode) -> 'Dataset':
            Unflatten the dataset back to its original structure.
        from_huggingface(dataset_name: str, split: Optional[str] = None, item_type: Type[Union[Episode, TimeStep]] = Episode, **kwargs):
            Class method to create a Dataset from a HuggingFace dataset.

    Useful Sample Methods:
        to(container: Any) -> Any:
            Convert the Dataset to a different container type (e.g., dict, list, numpy array, pytorch tensor).
        flatten(output_type: str = "list", non_numerical: str = "allow", ignore: set[str] | None = None) -> Any:
            Flatten the Dataset into a one-dimensional structure with various output options.
        schema(resolve_refs: bool = True, include_descriptions=False) -> Dict:
            Get a simplified JSON schema of the Dataset, useful for understanding its structure.
        infer_features_dict() -> Dict[str, Any]:
            Infer features from the data recursively, helpful for automatic feature detection.
        space() -> spaces.Dict:
            Return the corresponding Gym space for the Dataset, useful for reinforcement learning tasks.
        dump(*args, **kwargs) -> Dict[str, Any]:
            Dump the Dataset to a dictionary, providing a serializable representation.

    The class also implements standard list-like operations such as append, extend, insert, remove, pop,
    and supports indexing, iteration, and length queries.

    Examples:
        >>> # Create a dataset of episodes
        >>> episode_data = [
        ...     {"steps": [{"observation": 1, "action": 2}, {"observation": 3, "action": 4}]},
        ...     {"steps": [{"observation": 5, "action": 6}, {"observation": 7, "action": 8}]},
        ... ]
        >>> dataset = Dataset.from_dict({"episodes": episode_data}, item_type=Episode)
        >>> len(dataset)
        2

        >>> # Use Sample methods
        >>> flattened = dataset.flatten(output_type="np")  # Get a numpy array
        >>> schema = dataset.schema()  # Get the dataset's schema
        >>> features = dataset.infer_features_dict()  # Infer features automatically
        >>> gym_space = dataset.space()  # Get the corresponding Gym space

        >>> # Convert to different formats
        >>> as_dict = dataset.to("dict")
        >>> as_torch = dataset.to("pt")  # Convert to PyTorch tensor
    """

    metadata: Any = Field(default=None, description="Metadata for the dataset")

    def __init__(
        self, *args, item_type: Type[Union[Episode, TimeStep]] = Episode, loader: Callable = default_loader, **kwargs
    ):
        HFDataset.__init__(self, *args, **kwargs)
        Sample.__init__(self)
        self.item_type = item_type
        self.loader = loader

    def __getitem__(self, idx: Union[int, slice]) -> Union[Episode, TimeStep, "Dataset"]:
        """Get an item or slice of items from the dataset."""
        if isinstance(idx, int):
            return self.loader(super().__getitem__(idx))
        elif isinstance(idx, slice):
            return Dataset(super().__getitem__(idx), item_type=self.item_type, loader=self.loader)
        else:
            raise TypeError("Index must be int or slice")

    def flatten_to(self, field: str) -> "Dataset":
        """Flatten the dataset to a specific field, like 'steps'."""

        def flatten_generator():
            for idx, item in enumerate(self):
                if hasattr(item, field):
                    for sub_idx, sub_item in enumerate(getattr(item, field)):
                        flattened_dict = sub_item.dict()
                        if self.item_type == Episode:
                            flattened_dict["episode_idx"] = idx
                        flattened_dict["step_idx"] = sub_idx
                        yield flattened_dict
                else:
                    raise AttributeError(f"Items in dataset do not have field '{field}'")

        flattened_data = list(flatten_generator())
        return Dataset.from_dict({"data": flattened_data}, item_type=TimeStep, loader=lambda x: TimeStep(**x))

    def unflatten(self, parent_field: str, parent_class: Type[Episode] = Episode) -> "Dataset":
        """Unflatten the dataset back to its original structure."""
        grouped_items = {}
        for item in self:
            parent_idx = item.episode_idx if hasattr(item, "episode_idx") else 0
            if parent_idx not in grouped_items:
                grouped_items[parent_idx] = []
            grouped_items[parent_idx].append(item)

        unflattened_data = [
            parent_class(**{parent_field: sorted(items, key=lambda x: x.step_idx)}).dict()
            for items in grouped_items.values()
        ]

        return Dataset.from_dict({"data": unflattened_data}, item_type=parent_class, loader=lambda x: parent_class(**x))

    @classmethod
    def from_huggingface(
        cls,
        dataset_name: str,
        split: Optional[str] = None,
        item_type: Type[Union[Episode, TimeStep]] = Episode,
        **kwargs,
    ):
        """Create a Dataset from a HuggingFace dataset."""
        hf_dataset = HFDataset.load_dataset(dataset_name, split=split, **kwargs)
        return cls(hf_dataset, item_type=item_type)

    def to(self, container: Any) -> Any:
        """Convert the Dataset to a different container type."""
        return Sample.to(self, container)

    def flatten(self, output_type: str = "list", non_numerical: str = "allow", ignore: set[str] | None = None) -> Any:
        """Flatten the Dataset into a one-dimensional structure."""
        return Sample.flatten(self, output_type, non_numerical, ignore)

    def schema(self, resolve_refs: bool = True, include_descriptions=False) -> Dict:
        """Get a simplified JSON schema of the Dataset."""
        return Sample.schema(self, resolve_refs, include_descriptions)

    def infer_features_dict(self) -> Dict[str, Any]:
        """Infer features from the data recursively."""
        return Sample.infer_features_dict(self)

    def space(self) -> spaces.Dict:
        """Return the corresponding Gym space for the Dataset."""
        return Sample.space(self)

    def dump(self, *args, **kwargs) -> Dict[str, Any]:
        """Dump the Dataset to a dictionary."""
        return {idx: self.loader(item).dump(*args, **kwargs) for idx, item in enumerate(self)}

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """Return a dictionary representation of the Dataset."""
        return self.dump(*args, **kwargs)

    def append(self, item: Union[Episode, TimeStep]) -> None:
        """Append an item to the dataset."""
        if not isinstance(item, self.item_type):
            raise TypeError(f"Item must be of type {self.item_type}")
        super().add_item(item.dict())

    def extend(self, items: List[Union[Episode, TimeStep]]) -> None:
        """Extend the dataset with a list of items."""
        if not all(isinstance(item, self.item_type) for item in items):
            raise TypeError(f"All items must be of type {self.item_type}")
        super().add_items([item.dict() for item in items])

    def __len__(self) -> int:
        """Return the number of items in the dataset."""
        return super().__len__()

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __reversed__(self):
        for i in range(len(self) - 1, -1, -1):
            yield self[i]

    def __contains__(self, item: Union[Episode, TimeStep]) -> bool:
        """Check if an item is in the dataset."""
        return any(self.loader(x) == item for x in super().__iter__())

    def insert(self, index: int, item: Union[Episode, TimeStep]) -> None:
        """Insert an item at a given position."""
        if not isinstance(item, self.item_type):
            raise TypeError(f"Item must be of type {self.item_type}")
        new_data = HFDataset.from_dict(item.dict())
        self._data = HFDataset.concatenate_datasets([self[:index], new_data, self[index:]])

    def remove(self, item: Union[Episode, TimeStep]) -> None:
        """Remove the first occurrence of an item."""
        index = self.index(item)
        del self[index]

    def pop(self, index: int = -1) -> Union[Episode, TimeStep]:
        """Remove and return item at index (default last)."""
        item = self[index]
        del self[index]
        return item

    def clear(self) -> None:
        """Remove all items from the dataset."""
        self._data = HFDataset.from_dict({})

    def index(self, item: Union[Episode, TimeStep], start: int = 0, end: int = None) -> int:
        """Return first index of item. Raises ValueError if the item is not present."""
        end = end if end is not None else len(self)
        for i in range(start, end):
            if self[i] == item:
                return i
        raise ValueError(f"{item} is not in dataset")

    def count(self, item: Union[Episode, TimeStep]) -> int:
        """Return number of occurrences of item."""
        return sum(1 for x in self if x == item)

    def __add__(self, other: "Dataset") -> "Dataset":
        """Concatenate two datasets."""
        if not isinstance(other, Dataset) or self.item_type != other.item_type:
            raise ValueError(f"Can only add another Dataset with item_type {self.item_type}")
        new_dataset = HFDataset.concatenate_datasets([self, other])
        return Dataset(new_dataset, item_type=self.item_type, loader=self.loader)

    def __radd__(self, other: "Dataset") -> "Dataset":
        """Support for sum() and reverse add operations."""
        if other == 0:
            return self
        return self.__add__(other)

    def save(self, filename: str) -> None:
        """Save the dataset to a file."""
        super().save_to_disk(filename)

    @classmethod
    def load(
        cls, filename: str, item_type: Type[Union[Episode, TimeStep]] = Episode, loader: Callable = default_loader
    ) -> "Dataset":
        """Load a dataset from a file."""
        hf_dataset = HFDataset.load_from_disk(filename)
        return cls(hf_dataset, item_type=item_type, loader=loader)
