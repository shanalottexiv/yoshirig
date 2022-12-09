import json, os

ff_skel_json_path = os.path.join(os.path.dirname(__file__), '../data/ff_skel.json')

with open(ff_skel_json_path, 'r') as ff_skel_file:
    ff_bone_dict = json.load(ff_skel_file)

