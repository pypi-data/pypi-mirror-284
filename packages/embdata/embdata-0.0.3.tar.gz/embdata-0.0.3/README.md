# mbodied-data

[![PyPI - Version](https://img.shields.io/pypi/v/mbodied-data.svg)](https://pypi.org/project/mbodied-data)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mbodied-data.svg)](https://pypi.org/project/mbodied-data)

-----

## Table of Contents

- [mbodied-data](#mbodied-data)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Classes](#classes)
    - [Coordinate](#coordinate)
      - [Pose](#pose)
    - [Episode](#episode)
    - [Exploratory data analysis for common minmax and standardization normalization methods.](#exploratory-data-analysis-for-common-minmax-and-standardization-normalization-methods)
    - [Upsample and downsample the trajectory to a target frequency.](#upsample-and-downsample-the-trajectory-to-a-target-frequency)
    - [Make actions relative or absolute](#make-actions-relative-or-absolute)
  - [Applications](#applications)
    - [What are the grasping positions in the world frame?](#what-are-the-grasping-positions-in-the-world-frame)
  - [License](#license)
  - [Design Decisions](#design-decisions)

## Installation

```console
pip install embdata
```

## Classes

### Coordinate

Classes for representing geometric data in cartesian and polar coordinates.

#### Pose 
-  (x, y, z, roll, pitch, and yaw) in some reference frame.
- Contains `.numpy()`, `.dict()`, `.dataset()` methods from `Sample` class we all know and love.

Example:
```python
    >>> import math
    >>> pose_3d = Pose3D(x=1, y=2, theta=math.pi/2)
    >>> pose_3d.to("cm")
    Pose3D(x=100.0, y=200.0, theta=1.5707963267948966)

    >>> pose_3d.to("deg")
    Pose3D(x=1.0, y=2.0, theta=90.0)

    >>> class BoundedPose6D(Pose6D):
    ...     x: float = CoordinateField(bounds=(0, 5))

    >>> pose_6d = BoundedPose6D(x=10, y=2, z=3, roll=0, pitch=0, yaw=0)
    Traceback (most recent call last):
    ...
    ValueError: x value 10 is not within bounds (0, 5)
```


### Episode

The `Episode` class provides a list-like interface for a sequence of observations, actions, and/or other data points. It is designed to streamline exploratory data analysis and manipulation of time series data. Episodes can be easily concatenated, iterated over, and manipulated similar to lists.

```python
class Episode(Sample):
    """A list-like interface for a sequence of observations, actions, and/or other.

    Meant to streamline exploratory data analysis and manipulation of time series data.

    Just append to an episode like you would a list and you're ready to start training models.

    To iterate over the steps in an episode, use the `iter` method.
```

Example:
```python
    >>> episode = Episode(steps=[TimeStep(), TimeStep(), TimeStep()])
    >>> for step in episode.iter():
    ...     print(step)
```
To concatenate two episodes, use the `+` operator.

Example:
```python
    >>> episode1 = Episode(steps=[TimeStep(), TimeStep()])
    >>> episode2 = Episode(steps=[TimeStep(), TimeStep()])
    >>> combined_episode = episode1 + episode2
    >>> len(combined_episode)
    4 
```

```python
 def from_list(cls, steps: List[Dict|Sample], observation_key:str, action_key: str, supervision_key:str = None) -> 'Episode':
        """Create an episode from a list of dictionaries.

        Args:
            steps (List[Dict|Sample]): The list of dictionaries representing the steps.
            action_key (str): The key for the action in each dictionary.
            observation_key (str): The key for the observation in each dictionary.
            supervision_key (str, optional): The key for the supervision in each dictionary. Defaults to None.

        Returns:
            'Episode': The created episode.
```
Example:
```python
    >>> steps = [
    ...     {"observation": Image((224,224)), "action": Sample(1), "supervision": 0},
    ...     {"observation": Image((224,224)), "action": Sample(1), "supervision": 1},
    ...     {"observation": Image((224,224)), "action": Sample(100), "supervision": 0},
    ...     {"observation": Image((224,224)), "action": Sample(300), "supervision": 1},
    ... ]
    >>> episode = Episode.from_list(steps, "observation", "action", "supervision")
    >>> episode
    Episode(
        Stats(
            mean=[100.5]
            variance=[19867.0]
            skewness=[0.821]
            kurtosis=[-0.996]
            min=[1]
            max=[300]
            lower_quartile=[1.0]
            median=[50.5]
            upper_quartile=[150.0]
            non_zero_count=[4]
            zero_count=[0])
    )
```
### Exploratory data analysis for common minmax and standardization normalization methods.

Example
```python
    >>> steps = [
    ...     {"observation": Image((224,224)), "action": 1, "supervision": 0},
    ...     {"observation": Image((224,224)), "action": 1, "supervision": 1},
    ...     {"observation": Image((224,224)), "action": 100, "supervision": 0},
    ...     {"observation": Image((224,224)), "action": 300, "supervision": 1},
    ]
    >>> episode = Episode.from_list(steps, "observation", "action", "supervision")
    >>> episode.trajectory().transform("minmax")
    Episode(
        Stats(
            mean=[0.335]
            variance=[0.198]
            skewness=[0.821]
            kurtosis=[-0.996]
            min=[0.0]
            max=[1.0]
            lower_quartile=[0.0]
            median=[0.168]
            upper_quartile=[0.503]
            non_zero_count=[4]
            zero_count=[0])
    )
    >>> episode.trajectory().transform("standard")
    Episode(
        Stats(
            mean=[0.335]
            variance=[0.198]
            skewness=[0.821]
            kurtosis=[-0.996]
            min=[-1.0]
            max=[1.0]
            lower_quartile=[-1.0]
            median=[0.0]
            upper_quartile=[1.0]
            non_zero_count=[4]
            zero_count=[0])
    )
    >>> episode.trajectory().transform("unstandard", mean=0.335, std=0.198)
    Episode(
        Stats(
            mean=[100.5]
            variance=[19867.0]
            skewness=[0.821]
            kurtosis=[-0.996]
            min=[1]
            max=[300]
            lower_quartile=[1.0]
            median=[50.5]
            upper_quartile=[150.0]
            non_zero_count=[4]
            zero_count=[0])
    )
    >>> episode.trajectory().frequencies().show()  # .save("path/to/save.png") also works.
    >>> episode.trajectory().plot().show()
```
### Upsample and downsample the trajectory to a target frequency.

- Uses bicupic and rotation spline interpolation to upsample and downsample the trajectory to a target frequency.
```python
    >>> episode.trajectory().resample(target_hz=10).plot().show() # .save("path/to/save.png") also works.
```

### Make actions relative or absolute

- Make actions relative or absolute to the previous action.
```python
    >>> relative_actions = episode.trajectory("action").make_relative()
    >>>  absolute_again = episode.trajectory().make_absolute(initial_state=relative_actions[0])
    assert np.allclose(episode.trajectory("action"), absolute_again)
```

## Applications

### What are the grasping positions in the world frame?
    
```python
    >>> initial_state = episode.trajectory('state').flatten(to='end_effector_pose')[0]
    >>> episode.trajectory('action').make_absolute(initial_state=initial_state).filter(lambda x: x.grasp == 1)
```

## License

`embdata` is distributed under the terms of the [apache-2.0](https://spdx.org/licenses/apache-2.0.html) license.

## Design Decisions

- [x] Grasp value is [-1, 1] so that the default value is 0.
- [x] Motion rather than Action to distinguish from non-physical actions.
  