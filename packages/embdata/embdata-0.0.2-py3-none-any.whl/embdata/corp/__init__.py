import random


def format_robot_response(
    x=0, y=0, z=0, roll=0, pitch=0, yaw=0, translation_unit="meters", angle_unit="degrees", trajectory_planning=False
):
    assert all(
        isinstance(val, (int, float)) for val in (x, y, z, roll, pitch, yaw)
    ), "All position and orientation values must be numbers"
    assert translation_unit and angle_unit, "Units must be provided"
    assert isinstance(trajectory_planning, bool), "trajectory_planning must be a boolean"

    def get_direction(value, positive_options, negative_options):
        options = positive_options if value > 0 else negative_options
        return f"{abs(value):.2f} {translation_unit} {random.choice(options)}"

    def get_rotation(value, clockwise_options, counterclockwise_options):
        options = clockwise_options if value > 0 else counterclockwise_options
        return f"{abs(value):.2f} {angle_unit} {random.choice(options)}"

    translation_map = {
        "x": (
            ["forward", "ahead", "in the positive x direction", "towards the front"],
            ["backward", "back", "in the negative x direction", "towards the rear"],
        ),
        "y": (
            ["to the right", "rightward", "in the positive y direction", "starboard"],
            ["to the left", "leftward", "in the negative y direction", "port"],
        ),
        "z": (
            ["up", "upward", "in the positive z direction", "skyward"],
            ["down", "downward", "in the negative z direction", "groundward"],
        ),
    }

    rotation_map = {
        "roll": (
            ["clockwise roll", "positive roll", "roll to the right"],
            ["counterclockwise roll", "negative roll", "roll to the left"],
        ),
        "pitch": (
            ["upward pitch", "positive pitch", "nose-up pitch"],
            ["downward pitch", "negative pitch", "nose-down pitch"],
        ),
        "yaw": (["rightward yaw", "positive yaw", "yaw to starboard"], ["leftward yaw", "negative yaw", "yaw to port"]),
    }

    position_map = {
        "x": (["in front of", "ahead of", "forward from"], ["behind", "to the rear of", "backward from"]),
        "y": (
            ["to the right of", "on the right side of", "starboard of"],
            ["to the left of", "on the left side of", "port of"],
        ),
        "z": (["above", "over", "higher than"], ["below", "under", "lower than"]),
    }

    translation_components = [
        get_direction(val, *translation_map[axis]) for val, axis in zip((x, y, z), "xyz") if val != 0
    ]
    orientation_components = [
        get_rotation(val, *rotation_map[rot])
        for val, rot in zip((roll, pitch, yaw), ("roll", "pitch", "yaw"))
        if val != 0
    ]

    if trajectory_planning:
        if translation_components and orientation_components:
            move_verbs = ["Move", "Translate", "Shift", "Reposition"]
            adjust_verbs = ["adjust", "modify", "change", "alter"]
            response = f"{random.choice(move_verbs)} the robot's end-effector {', '.join(translation_components)}. Then, {random.choice(adjust_verbs)} its orientation with {', '.join(orientation_components)}."
        elif translation_components:
            move_verbs = ["Move", "Translate", "Shift", "Reposition"]
            response = f"{random.choice(move_verbs)} the robot's end-effector {', '.join(translation_components)}."
        elif orientation_components:
            adjust_verbs = ["Adjust", "Modify", "Change", "Alter"]
            response = f"{random.choice(adjust_verbs)} the robot's end-effector orientation with {', '.join(orientation_components)}."
        else:
            maintain_phrases = [
                "Maintain the robot's current end-effector position and orientation.",
                "Keep the robot's end-effector in its present position and orientation.",
                "Do not change the robot's end-effector position or orientation.",
                "The robot's end-effector should remain stationary.",
            ]
            response = random.choice(maintain_phrases)
    else:
        position_components = [
            get_direction(val, *position_map[axis]) for val, axis in zip((x, y, z), "xyz") if val != 0
        ]

        if position_components and orientation_components:
            location_verbs = ["is located", "is positioned", "is situated", "can be found"]
            orientation_verbs = ["oriented", "aligned", "rotated", "angled"]
            response = f"The object {random.choice(location_verbs)} {', '.join(position_components)} the base frame, {random.choice(orientation_verbs)} with {', '.join(orientation_components)}."
        elif position_components:
            location_verbs = ["is located", "is positioned", "is situated", "can be found"]
            response = f"The object {random.choice(location_verbs)} {', '.join(position_components)} the base frame."
        elif orientation_components:
            orientation_verbs = ["is oriented", "is aligned", "is rotated", "is angled"]
            response = f"The object is at the base frame and {random.choice(orientation_verbs)} with {', '.join(orientation_components)}."
        else:
            base_frame_phrases = [
                "The object is at the base frame with no change in position or orientation.",
                "The object remains at the base frame, maintaining its original position and orientation.",
                "There is no change in the object's position or orientation relative to the base frame.",
                "The object's position and orientation are unchanged from the base frame.",
            ]
            response = random.choice(base_frame_phrases)

    return response


# Example usage (for demonstration, not part of the final code):
# for _ in range(3):
#     print(format_robot_response(1.5, -2, 3, 10, -15, 20, "meters", "degrees", True))
#     print(format_robot_response(1.5, -2, 3, 10, -15, 20, "meters", "degrees", False))
#     print()
