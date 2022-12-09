"""

based on https://bindpose.com/creating-maya-control-shape-manager/

"""
import json

import maya.OpenMaya as om
import maya.cmds as mc
import os

CONTROL_SHAPE_JSONS_PATH = os.path.join(os.path.dirname(__file__), '../data/ctrL_shapes/')


def get_knots(crv_shape):
m_object = om.MObject()
selection = om.MSelectionList()
selection.add(crv_shape)
selection.getDependNode(0, m_object)
fn_curve = om.MFnNurbsCurve(m_object)
knots = om.MDoubleArray()
fn_curve.getKnots(knots)

    return [knots[i] for i in range(knots.length())]


def get_shape_nodes(crv):
    print(mc.nodeType(crv))
    if mc.nodeType(crv) == "transform":
        return mc.listRelatives(crv, c=1, s=1)
    elif mc.nodeType(crv) == "nurbsCurve":
        return mc.listRelatives(mc.listRelatives(crv, p=1)[0], c=1, s=1)


def get_shape(crv):
    crv_shapes = []
    crv_shape_nodes = get_shape_nodes(crv)
    for node in crv_shape_nodes:
        crv_shape_dict = {
            "points": [],
            "knots": [],
            "form": mc.getAttr(f"{node}.form"),
            "degree": mc.getAttr(f"{node}.degree"),
            "color": mc.getAttr(f"{node}.overrideColor")
        }
        points = []

        print(mc.getAttr(f"{node}.controlPoints", s=1))
        for i in range(mc.getAttr(f"{node}.controlPoints", s=1)):
            points.append(mc.getAttr(f"{node}.controlPoints[{i}]")[0])

        crv_shape_dict["points"] = points
        crv_shape_dict["knots"] = get_knots(node)
        crv_shapes.append(crv_shape_dict)
    return crv_shapes


def set_shape(crv, crv_shapes_list):
    crv_shapes = get_shape_nodes(crv)
    print(crv_shapes)
    mc.delete(crv_shapes)

    for i, crv_shape in enumerate(crv_shapes_list):
        print(crv_shape)
        tmp_crv = mc.curve(p=crv_shape["points"], k=crv_shape["knots"], d=crv_shape["degree"],
                           per=bool(crv_shape["form"]))
        new_shape_node = mc.listRelatives(tmp_crv, s=1)[0]
        mc.parent(new_shape_node, crv, r=1, s=1)
        mc.delete(tmp_crv)
        new_shape_node = mc.rename(new_shape_node, crv + "Shape" + str(i + 1).zfill(2))
        mc.setAttr(f"{new_shape_node}.overrideEnabled", 1)
        mc.setAttr(f"{new_shape_node}.overrideColor", crv_shape["color"])


def shape_curve_to_json_file(crv, shape_name=None):
    if not shape_name:
        shape_name = crv
    print(shape_name)

    crv_shape = get_shape(crv)
    json_path = os.path.join(CONTROL_SHAPE_JSONS_PATH, f"{shape_name}.json")
    with open(json_path, "w") as f:
        f.write(json.dumps(crv_shape, sort_keys=True, indent=4, separators=(",", ":")))


def json_file_to_shape(shape_name, json_path=None):
    if not json_path:
        json_path = os.path.join(CONTROL_SHAPE_JSONS_PATH, f"{shape_name}.json")

    with open(json_path, "r") as f:
        shape_data = json.loads(f.read())
        print(shape_data)

    return shape_data
