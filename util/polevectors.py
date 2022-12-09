import maya.cmds as mc

def spawn_pole_vectors():
    loc_knee_l = mc.spaceLocator(n='leg_L_PV_loc')[0]
    pc_knee_l = mc.parentConstraint('j_asi_b_l', 'j_asi_c_l', loc_knee_l, mo=False)
    mc.delete(pc_knee_l)
    mc.move(40, loc_knee_l, r=True, ls=True, z = True)

    loc_knee_r = mc.spaceLocator(n='leg_R_PV_loc')[0]
    pc_knee_r = mc.parentConstraint('j_asi_b_r', 'j_asi_c_r', loc_knee_r, mo=False)
    mc.delete(pc_knee_r)
    mc.move(40, loc_knee_r, r=True, ls=True, z=True)

    loc_elbow_r = mc.spaceLocator(n='arm_R_PV_loc')[0]
    pc_elbow_r = mc.parentConstraint('j_ude_b_r', loc_elbow_r, mo=False)
    mc.delete(pc_elbow_r)
    mc.move(-30, loc_elbow_r, r=True, ls=True, z=True)

    loc_elbow_l = mc.spaceLocator(n='arm_L_PV_loc')[0]
    pc_elbow_l = mc.parentConstraint('j_ude_b_l', loc_elbow_l, mo=False)
    mc.delete(pc_elbow_l)
    mc.move(-30, loc_elbow_l, r=True, ls=True, z=True)

    for loc in [loc_knee_l, loc_knee_r, loc_elbow_l, loc_elbow_r]:
        mc.makeIdentity(loc, r=True)


