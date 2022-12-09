import os

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from shiboken2 import wrapInstance
import util.fftorig

customMixinWindow = None


class DockableWidget(MayaQWidgetDockableMixin, QWidget):
    def __init__(self, parent=None):
        super(DockableWidget, self).__init__(parent=parent)
        layout = QVBoxLayout()
        self.alignControllersButton = QPushButton(text="Align controllers to skeleton")
        self.buildRigButton = QPushButton(text='Build rig')
        layout.addWidget(self.alignControllersButton)
        layout.addWidget(self.buildRigButton)
        self.setLayout(layout)
        self.setWindowTitle("YoshiRig")



def DockableWidgetUIScript(restore=False):
    global customMixinWindow

    if restore:
        restored_control = omui.MQtUtil_getCurrentParent()

    if not customMixinWindow:
        customMixinWindow = DockableWidget()
        customMixinWindow.setObjectName("customMayaMixinWindow")

    if restore:
        mixinPtr = omui.MQtUtil.findControl(customMixinWindow.objectName())
        omui.MQtUtil.addWidgetToMayaLayout(int(mixinPtr), int(restored_control))
    else:
        customMixinWindow.show(dockable=True,
                               uiScript='import ui.mainwindow.DockableWidgetUIScript as DockableWidgetUIScript\nDockableWidgetUIScript(restore=True)')

    return customMixinWindow


def ui():
    ui_widget = DockableWidgetUIScript()
    return ui_widget
