import json
import os

CONTROL_SHAPES_NAME_PATH = os.path.join(os.path.dirname(__file__), '../data/ctrl_list.json')

cc = {}  # control curves to match
cc_dont_rotate = []
root_C_ctrl = 'root_C_ctrl'
cc[root_C_ctrl] = 'root_C_ctrl'
root_C_secondary_ctrl = 'root_C_secondary_ctrl'
cc[root_C_secondary_ctrl] = 'root_C_secondary_ctrl'
CoG_C_ctrl = 'CoG_C_ctrl'
cc[CoG_C_ctrl] = 'CoG_C_bnd'
spine_FK_ctrl_chain = ['spine_C_FK01_ctrl', 'spine_C_FK02_ctrl', 'spine_C_FK03_ctrl']
cc['spine_C_FK01_ctrl'] = 'spine_C_spine01_bnd'
cc['spine_C_FK02_ctrl'] = 'spine_C_spine02_bnd'
cc['spine_C_FK03_ctrl'] = 'spine_C_spine03_bnd'
hips_C_ctrl = 'hips_C_ctrl'
cc[hips_C_ctrl] = 'hips_C_bnd'

clavicle_L_ctrl = 'clavicle_L_ctrl'
cc[clavicle_L_ctrl] = 'clavicle_L_bnd'
clavicle_R_ctrl = 'clavicle_R_ctrl'
cc[clavicle_R_ctrl] = 'clavicle_R_bnd'

arm_L_FK_ctrl_chain = ['arm_L_FK_upperArm_ctrl', 'arm_L_FK_elbow_ctrl', 'arm_L_FK_wrist_ctrl']
cc['arm_L_FK_upperArm_ctrl'] = 'arm_L_upperArm_bnd'
cc['arm_L_FK_elbow_ctrl'] = 'arm_L_elbow_bnd'
cc['arm_L_FK_wrist_ctrl'] = 'arm_L_wrist_bnd'

arm_R_FK_ctrl_chain = ['arm_R_FK_upperArm_ctrl', 'arm_R_FK_elbow_ctrl', 'arm_R_FK_wrist_ctrl']
cc['arm_R_FK_upperArm_ctrl'] = 'arm_R_upperArm_bnd'
cc['arm_R_FK_elbow_ctrl'] = 'arm_R_elbow_bnd'
cc['arm_R_FK_wrist_ctrl'] = 'arm_R_wrist_bnd'

arm_L_IK_ctrl = 'arm_L_IK_ctrl'
cc[arm_L_IK_ctrl] = 'arm_L_wrist_bnd'
cc_dont_rotate.append(arm_L_IK_ctrl)
arm_R_IK_ctrl = 'arm_R_IK_ctrl'
cc[arm_R_IK_ctrl] = 'arm_R_wrist_bnd'
cc_dont_rotate.append(arm_R_IK_ctrl)

leg_L_FK_ctrl_chain = ['leg_L_FK_upperLeg_ctrl', 'leg_L_FK_knee01_ctrl', 'leg_L_FK_knee02_ctrl', 'leg_L_FK_foot_ctrl',
                       'leg_L_FK_toes_ctrl']
cc['leg_L_FK_upperLeg_ctrl'] = 'leg_L_upperLeg_bnd'
cc['leg_L_FK_knee01_ctrl'] = 'leg_L_knee01_bnd'
cc['leg_L_FK_knee02_ctrl'] = 'leg_L_knee02_bnd'
cc['leg_L_FK_foot_ctrl'] = 'leg_L_foot_bnd'
cc['leg_L_FK_toes_ctrl'] = 'leg_L_toes_bnd'

leg_R_FK_ctrl_chain = ['leg_R_FK_upperLeg_ctrl', 'leg_R_FK_knee01_ctrl', 'leg_R_FK_knee02_ctrl', 'leg_R_FK_foot_ctrl',
                       'leg_R_FK_toes_ctrl']
cc['leg_R_FK_upperLeg_ctrl'] = 'leg_R_upperLeg_bnd'
cc['leg_R_FK_knee01_ctrl'] = 'leg_R_knee01_bnd'
cc['leg_R_FK_knee02_ctrl'] = 'leg_R_knee02_bnd'
cc['leg_R_FK_foot_ctrl'] = 'leg_R_foot_bnd'
cc['leg_R_FK_toes_ctrl'] = 'leg_R_toes_bnd'

leg_L_IK_ctrl = 'leg_L_IK_ctrl'
cc[leg_L_IK_ctrl] = 'leg_L_foot_bnd'
cc_dont_rotate.append(leg_L_IK_ctrl)

leg_R_IK_ctrl = 'leg_R_IK_ctrl'
cc[leg_R_IK_ctrl] = 'leg_R_foot_bnd'
cc_dont_rotate.append(leg_R_IK_ctrl)

hasTail = True
if hasTail:
    tail_ctrl_chain = ['tail_C_tail01_ctrl', 'tail_C_tail02_ctrl', 'tail_C_tail03_ctrl', 'tail_C_tail04_ctrl',
                       'tail_C_tail05_ctrl']
    cc['tail_C_tail01_ctrl'] = 'tail_C_tail01_bnd'
    cc['tail_C_tail02_ctrl'] = 'tail_C_tail02_bnd'
    cc['tail_C_tail03_ctrl'] = 'tail_C_tail03_bnd'
    cc['tail_C_tail04_ctrl'] = 'tail_C_tail04_bnd'
    cc['tail_C_tail05_ctrl'] = 'tail_C_tail05_bnd'

head_L_ear_ctrl = 'head_L_ear_ctrl'
cc[head_L_ear_ctrl] = 'head_L_ear_bnd'
head_R_ear_ctrl = 'head_R_ear_ctrl'
cc[head_R_ear_ctrl] = 'head_R_ear_bnd'

head_L_lip_ctrl = 'head_L_lip_ctrl'
cc[head_L_lip_ctrl] = 'head_L_lip_bnd'

head_R_lip_ctrl = 'head_R_lip_ctrl'
cc[head_R_lip_ctrl] = 'head_R_lip_bnd'

head_L_cheek_ctrl = 'head_L_cheek_ctrl'
cc[head_L_cheek_ctrl] = 'head_L_cheek_bnd'
head_R_cheek_ctrl = 'head_R_cheek_ctrl'
cc[head_R_cheek_ctrl] = 'head_R_cheek_bnd'

head_C_jaw_ctrl = 'head_C_jaw_ctrl'
cc[head_C_jaw_ctrl] = 'head_C_jaw_bnd'
head_C_nose_ctrl = 'head_C_nose_ctrl'
cc[head_C_nose_ctrl] = 'head_C_nose_bnd'

head_C_lowerLip01_ctrl = 'head_C_lowerLip01_ctrl'
cc[head_C_lowerLip01_ctrl] = 'head_C_lowerLip01_bnd'
head_C_lowerLip02_ctrl = 'head_C_lowerLip02_ctrl'
cc[head_C_lowerLip02_ctrl] = 'head_C_lowerLip02_bnd'

head_L_brow_ctrl = 'head_L_brow_ctrl'
cc[head_L_brow_ctrl] = 'head_L_brow_bnd'

head_R_brow_ctrl = 'head_R_brow_ctrl'
cc[head_R_brow_ctrl] = 'head_R_brow_bnd'

armor_L_shoulderpad_ctrl = 'armor_L_shoulderpad_ctrl'
cc[armor_L_shoulderpad_ctrl] = 'armor_L_shoulderpad_bnd'

armor_R_shoulderpad_ctrl = 'armor_R_shoulderpad_ctrl'
cc[armor_R_shoulderpad_ctrl] = 'armor_R_shoulderpad_bnd'

eye_L_ctrl = 'head_L_eye_ctrl'
cc[eye_L_ctrl] = 'head_L_eye_bnd'

eye_R_ctrl = 'head_R_eye_ctrl'
cc[eye_R_ctrl] = 'head_R_eye_bnd'

upper_eyelid_L_ctrl = 'head_L_upperEyelid_ctrl'
cc[upper_eyelid_L_ctrl] = 'head_L_upperEyelid_bnd'

lower_eyelid_L_ctrl = 'head_L_lowerEyelid_ctrl'
cc[lower_eyelid_L_ctrl] = 'head_L_lowerEyelid_bnd'

upper_eyelid_R_ctrl = 'head_R_upperEyelid_ctrl'
cc[upper_eyelid_R_ctrl] = 'head_R_upperEyelid_bnd'

lower_eyelid_R_ctrl = 'head_R_lowerEyelid_ctrl'
cc[lower_eyelid_R_ctrl] = 'head_R_lowerEyelid_bnd'

leg_L_PV_ctrl = 'leg_L_PV_ctrl'
cc[leg_L_PV_ctrl] = 'leg_L_PV_loc'

leg_R_PV_ctrl = 'leg_R_PV_ctrl'
cc[leg_R_PV_ctrl] = 'leg_R_PV_loc'

finger_L_ctrl = [['hand_L_finger0{}_proximal_ctrl'.format(i), 'hand_L_finger0{}_distal_ctrl'.format(i)] for i in
                 range(1, 6)]
finger_R_ctrl = [['hand_R_finger0{}_proximal_ctrl'.format(i), 'hand_R_finger0{}_distal_ctrl'.format(i)] for i in
                 range(1, 6)]

for side in "LR":
    for i in range(1, 6):
        cc['hand_' + side + '_finger0' + str(i) + '_proximal_ctrl'] = 'hand_' + side + '_finger0' + str(
            i) + '_proximal_bnd'
        cc['hand_' + side + '_finger0' + str(i) + '_distal_ctrl'] = 'hand_' + side + '_finger0' + str(i) + '_distal_bnd'

cc['head_C_head_ctrl'] = 'head_C_head_bnd'
cc['head_C_neck_ctrl'] = 'head_C_neck_bnd'

ctrl_dict = {}
for k, v in cc.items():
    ctrl_dict[k] = {
        'bind_joint': v,
        'rotate': k not in cc_dont_rotate,
        'custom_shape_json': f"{k}.json"
    }

with open(CONTROL_SHAPES_NAME_PATH, 'w') as f:
    f.write(json.dumps(ctrl_dict, sort_keys=True, indent=4, separators=(",", ":")))
