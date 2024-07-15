# for FILE in tests/*.py ; do
#     aider --yes --test $FILE --test-cmd "pytest"
# done

# Limit to files in episode.py, features.py, geometry,.py image.py, sample.py, trajectory.py, motion/motion.py, motion/control.py
# for FILE in embdata/trajectory.py embdata/episode.py embdata/sample.py embdata/features.py embdata/geometry.py embdata/image.py embdata/motion/motion.py embdata/motion/control.py ; do
#     aider --yes --message "Ensure that that all classes and methods are present in a markdown file inside docs/ folder" $FILE 
# done

aider --yes --message "Update \"usage\" section to include MobileSingleHandControl and HumanoidControl and subclassing to create a new Motion. Note\
  that you must add these to the \"usage\" section. Not another section. Ensure that it matches the existing format and is collapsible" README.md

aider --yes --message "Update docs/example.md to include the full example of downloading the following dataset from repo id 'mbodiai/oxe_taco_play':\
DatasetInfo(\
  description='',\
  citation='',\
  homepage='',\
  license='',\
  features={\
    '__key__': Value(dtype='string', id=None),\
    '__url__': Value(dtype='string', id=None),\
    'data.pickle': {\
      'aspects': {\
        'already_success': Value(dtype='bool', id=None),\
        'feasible': Value(dtype='bool', id=None),\
        'has_aspects': Value(dtype='bool', id=None),\
        'success': Value(dtype='bool', id=None),\
        'undesirable': Value(dtype='bool', id=None)\
      },\
      'attributes': {\
        'collection_mode': Value(dtype='int64', id=None),\
        'collection_mode_name': Value(dtype='string', id=None),\
        'data_type': Value(dtype='int64', id=None),\
        'data_type_name': Value(dtype='string', id=None),\
        'env': Value(dtype='int64', id=None),\
        'env_name': Value(dtype='string', id=None),\
        'location': Value(dtype='int64', id=None),\
        'location_name': Value(dtype='string', id=None),\
        'objects_family': Value(dtype='int64', id=None),\
        'objects_family_name': Value(dtype='string', id=None),\
        'task_family': Value(dtype='int64', id=None),\
        'task_family_name': Value(dtype='string', id=None)\
      },\
      'image_list': Sequence(feature=Value(dtype='string', id=None), length=-1, id=None),\
      'steps': [\
        {\
          'action': {\
            'base_displacement_vector': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'base_displacement_vertical_rotation': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'gripper_closedness_action': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'rotation_delta': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'terminate_episode': Sequence(feature=Value(dtype='int64', id=None), length=-1, id=None),\
            'world_vector': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None)\
          },\
          'is_first': Value(dtype='bool', id=None),\
          'is_last': Value(dtype='bool', id=None),\
          'is_terminal': Value(dtype='bool', id=None),\
          'observation': {\
            'base_pose_tool_reached': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'gripper_closed': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'gripper_closedness_commanded': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'height_to_bottom': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'image': {'bytes': Value(dtype='binary', id=None), 'path': Value(dtype='null', id=None)},\
            'natural_language_embedding': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'natural_language_instruction': Value(dtype='string', id=None),\
            'orientation_box': Sequence(feature=Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None), length=-1, id=None),\
            'orientation_start': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'robot_orientation_positions_box': Sequence(\
              feature=Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
              length=-1,\
              id=None\
            ),\
            'rotation_delta_to_go': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'src_rotation': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'vector_to_go': Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
            'workspace_bounds': Sequence(\
              feature=Sequence(feature=Value(dtype='float64', id=None), length=-1, id=None),\
              length=-1,\
              id=None\
            )\
          },\
          'reward': Value(dtype='float32', id=None)\
        }\
      ]\
    }\
  },\
) , then \`flattening to\` desired nested subfields, then creating an episode, cleaning the data with\
  trajectory.py, visualizing with episode.show() and trajectory.save(), and finetuning this model on a basic gpt2vit model.
  . consult README.md and embdata/episode.py and embdata/trajectory.py and embdata/sample.py" README.md