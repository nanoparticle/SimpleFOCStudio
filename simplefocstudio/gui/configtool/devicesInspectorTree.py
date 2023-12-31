#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QVBoxLayout, QFrame)

from simplefocstudio.gui.configtool.connectionControl import ConnectionControlGroupBox
from simplefocstudio.gui.configtool.deviceJoggingControl import DeviceJoggingControl
from simplefocstudio.gui.configtool.deviceTreeview import DeviceTreeView
from simplefocstudio.gui.configtool.droDisplayWidget import DROGroupBox
from simplefocstudio.gui.configtool.generalControls import GeneralControls
from simplefocstudio.simpleFOCConnector import SimpleFOCDevice


class DevicesInspectorTree(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.device = SimpleFOCDevice.getInstance()

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.droWidget = DROGroupBox(self)
        self.layout.addWidget(self.droWidget)

        self.generalControls = GeneralControls(self)
        self.layout.addWidget(self.generalControls)

        self.treeView = DeviceTreeView(self)
        self.layout.addWidget(self.treeView)

        self.joggingControl = DeviceJoggingControl(self)
        self.layout.addWidget(self.joggingControl)

        self.connectionControl = ConnectionControlGroupBox(self)
        self.layout.addWidget(self.connectionControl)

        self.setMaximumWidth(500)
