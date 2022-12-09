import pymel.core as pm
import rig.controllers as ctrlers
import json
import os
import util.polevectors as pv
menuId = "yoshirig"

rigBuilderUi_str = """
import ui.mainwindow as mainwindow
mainwindow.ui()
"""

saveShape_str = """
import util.controlshapes as cs
import maya.cmds as mc
crvs = mc.ls(sl=1)
for crv in crvs:
    cs.shape_curve_to_json_file(crv)
"""
CONTROL_SHAPES_NAME_PATH = os.path.join(os.path.dirname(__file__), '../data/ctrl_list.json')
def spawn_controllers(arg):
    with open(CONTROL_SHAPES_NAME_PATH, 'r') as f:
        shapes_dict = json.load(f)
        ctrlers.spawn_and_match_shapes(shapes_dict)

def spawn_pole_vectors(arg):
    pv.spawn_pole_vectors()

def install_menu(id=menuId):
    if pm.menu(id, exists=True):
        pm.deleteUI(id)

    label = "YoshiRig"

    pm.menu(id, parent="MayaWindow",tearOff=True, label=label)
    pm.setParent(id, menu=True)
    pm.menuItem(parent=id, label="Rig builder", command=rigBuilderUi_str)
    pm.menuItem(parent=id, label="Save Shape to JSON", command=saveShape_str)
    pm.menuItem(parent=id, label="Spawn controllers", command=spawn_controllers)
    pm.menuItem(parent=id, label="Spawn pole vector locators", command=spawn_pole_vectors)




