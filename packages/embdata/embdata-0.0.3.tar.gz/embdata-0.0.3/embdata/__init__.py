"""
embdata: A package for handling embodied AI data structures and operations.

This package provides classes and utilities for working with various data types
commonly used in embodied AI tasks, such as episodes, time steps, images, and samples.

Examples:
    >>> from embdata import Episode, TimeStep, Image, Sample
    >>> # Create a sample episode
    >>> episode = Episode(steps=[TimeStep(observation=Image(), action=Sample(velocity=1.0))])
    >>> print(len(episode))
    1
"""

from typing import List
from .sample import Sample
from .image import Image
from .episode import Episode, TimeStep, ImageTask, VisionMotorStep

__all__ = [
    "Episode",
    "TimeStep",
    "ImageTask",
    "VisionMotorStep",
    "Image",
    "Sample",
]


def create_complex_episode(num_steps: int = 5) -> Episode:
    """
    Create a complex episode with multiple time steps, including nested image and text data.

    This function demonstrates the creation of a rich Episode object with multiple TimeStep
    instances, each containing complex Image and Sample objects with nested structures.

    Args:
        num_steps (int): Number of time steps to create in the episode. Defaults to 5.

    Returns:
        Episode: A complex episode with multiple time steps.

    Example:
        >>> complex_episode = create_complex_episode(3)
        >>> print(len(complex_episode))
        3
        >>> print(isinstance(complex_episode[0].observation, Image))
        True
        >>> print(isinstance(complex_episode[0].action, Sample))
        True
        >>> print(complex_episode[0].action.text_data)
        'Action description for step 0'
        >>> print(complex_episode[0].observation.metadata)
        {'resolution': (640, 480), 'format': 'RGB'}
        >>> print(complex_episode[0].action.nested_data['parameters'])
        {'gain': 0.5, 'offset': 0.0}
    """
    steps: List[TimeStep] = []
    for i in range(num_steps):
        observation = Image(
            array=None,
            base64="base64_encoded_image_data",
            metadata={"resolution": (640, 480), "format": "RGB"}
        )
        action = Sample(
            velocity=1.0 + i * 0.1,
            direction=i * 45,
            text_data=f"Action description for step {i}",
            nested_data={
                "parameters": {"gain": 0.5, "offset": i * 0.1},
                "flags": ["active", "validated"]
            }
        )
        step = TimeStep(observation=observation, action=action)
        steps.append(step)
    
    return Episode(steps=steps)


def create_complex_sample() -> Sample:
    """
    Create a complex sample with nested image, text, and sample data.

    This function demonstrates the creation of a rich Sample object with
    nested structures including image data, text annotations, and sub-samples.

    Returns:
        Sample: A complex sample with nested structures.

    Example:
        >>> complex_sample = create_complex_sample()
        >>> print(isinstance(complex_sample.image_data, Image))
        True
        >>> print(complex_sample.text_annotation)
        'This is a complex nested sample'
        >>> print(len(complex_sample.nested_samples))
        3
        >>> print(complex_sample.nested_samples[0].value)
        0
    """
    return Sample(
        image_data=Image(
            array=None,
            base64="complex_image_data",
            metadata={"depth": 3, "encoding": "PNG"}
        ),
        text_annotation="This is a complex nested sample",
        nested_samples=[
            Sample(value=i, metadata={"type": "subsample"})
            for i in range(3)
        ]
    )


if __name__ == "__main__":
    # Composite example using multiple classes
    complex_episode = create_complex_episode()
    print(f"Created an episode with {len(complex_episode)} steps")

    # Accessing nested data
    first_step = complex_episode[0]
    print(f"First step observation metadata: {first_step.observation.metadata}")
    print(f"First step action velocity: {first_step.action.velocity}")
    print(f"First step action nested data: {first_step.action.nested_data}")

    # Iterating through the episode
    for i, step in enumerate(complex_episode):
        print(f"Step {i} - Action text: {step.action.text_data}")

    # Using the Image class
    image = Image.open("path/to/image.jpg", encoding="jpeg", size=(224, 224))
    image.save("path/to/resized_image.jpg", encoding="jpeg", quality=95)

    # Creating a custom Sample
    custom_sample = Sample(
        sensor_data={"temperature": 25.5, "humidity": 60},
        timestamp="2023-07-10T12:34:56",
        labels=["indoor", "room1"]
    )
    print(f"Custom sample data: {custom_sample.dict()}")

    # Demonstrating complex nested structure
    complex_sample = create_complex_sample()
    print("Complex nested sample structure:")
    print(complex_sample.dict())

    # Creating a VisionMotorStep
    vision_motor_step = VisionMotorStep(
        image=Image(array=None, base64="vision_data"),
        motor_command=Sample(velocity=2.0, angle=30)
    )
    print("VisionMotorStep example:")
    print(vision_motor_step.dict())

    # Composite example using multiple classes
    print("\nComposite example using multiple classes:")
    # Create a complex episode
    episode = create_complex_episode(num_steps=3)
    
    # Add a complex sample to the episode
    complex_sample = create_complex_sample()
    episode.steps.append(TimeStep(observation=complex_sample.image_data, action=complex_sample))
    
    # Create a VisionMotorStep and add it to the episode
    vision_motor_step = VisionMotorStep(
        image=Image(array=None, base64="vision_data", metadata={"format": "RGB"}),
        motor_command=Sample(velocity=2.0, angle=30, text_data="Move forward")
    )
    episode.steps.append(vision_motor_step)
    
    # Print summary of the composite example
    print(f"Final episode length: {len(episode)}")
    print(f"Types of steps in the episode:")
    for i, step in enumerate(episode.steps):
        print(f"  Step {i}: {type(step).__name__}")
    
    # Access and print some nested data
    last_step = episode.steps[-1]
    if isinstance(last_step, VisionMotorStep):
        print(f"Last step image metadata: {last_step.image.metadata}")
        print(f"Last step motor command: {last_step.motor_command.dict()}")
