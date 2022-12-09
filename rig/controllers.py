import util.controlshapes as cs
import maya.cmds as mc
import os
CONTROL_SHAPE_JSONS_PATH = os.path.join(os.path.dirname(__file__), '../data/ctrL_shapes/')


def spawn_and_match_shapes(shapes_dict):
    for k, v in shapes_dict.items():
        print(k, v)
        ctrl = mc.circle(n=k)[0]
        custom_shape_json_path = os.path.join(CONTROL_SHAPE_JSONS_PATH, v['custom_shape_json'])
        if os.path.exists(custom_shape_json_path):
            shape = cs.json_file_to_shape(k, custom_shape_json_path)
            cs.set_shape(ctrl, shape)


