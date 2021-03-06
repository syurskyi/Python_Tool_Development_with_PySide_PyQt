## TPAYNE APPLICATION LAUNCHER
##      OCT. 2017
##      IRVINE, CA, USA
##  [See license at end of file]

''' 
The goal of this tool is to create a GUI that 
allows the user to quickly create, select and 
delete workspaces and add, remove and launch
applications within those workspaces.

This tool is the beginning of a pipeline 
management application in which you could keep
multiple users using the same version of software,
copy distinct settings and files to the clients 
machines and a whole bunch of other cool stuff.
'''

#!/usr/bin/env python

__author__ = 'Trevor Payne'
__version__ = '1.0'

import os
import sys

import Qt
from Qt import QtWidgets, QtCore, QtGui
import tp_launcher_model

QT_VER = Qt.__binding__
PY_VER = sys.version[:3]

class TP_Launcher_GUI(QtWidgets.QWidget):
    '''The goal of this tool is to create a GUI that 
        allows the user to quickly create, select and 
        delete workspaces and add, remove and launch
        applications within those workspaces.
    '''
    def __init__(self, parent=None):
        super(TP_Launcher_GUI, self).__init__(parent)

        self._icons = QtWidgets.QFileIconProvider()
        self._my_path = os.path.dirname(os.path.realpath(__file__))
        images_path = os.path.join(self._my_path, 'images')
        full_path = os.path.join(images_path, 'TPayne_Launcher.png')
        self._tpl_icon = QtGui.QIcon(full_path)
        
        self._tp_launcher = tp_launcher_model.TP_Launcher_Model()

        self._setup()
        self._testing()

    #======= SETUP UI =================================

    def _setup(self):
        v_layout = QtWidgets.QVBoxLayout(self)

        v_layout.addLayout(self._setup_header())
        v_layout.addWidget(self._setup_apps())

        self._setup_connections()

        self.setWindowTitle('TPayne\'s Launcher ' + __version__)
        self.setWindowIcon(self._tpl_icon)
        flag = QtCore.Qt.WindowCloseButtonHint
        self.setWindowFlags(QtCore.Qt.Window | flag)
        self.resize(190, 200)

    def _setup_header(self):
        h_layout = QtWidgets.QHBoxLayout()
        workspace_gb = QtWidgets.QGroupBox('Workspaces')
        v_layout = QtWidgets.QVBoxLayout(workspace_gb)

        self._workspace_cb = QtWidgets.QComboBox()

        v_layout.addWidget(self._workspace_cb)
        h_layout.addWidget(workspace_gb)
        h_layout.addStretch()
        return h_layout

    def _setup_apps(self):
        self._app_lw = QtWidgets.QListWidget()
        self._app_lw.setAlternatingRowColors(True)
        flag = QtWidgets.QAbstractItemView.InternalMove
        self._app_lw.setDragDropMode(flag)
        return self._app_lw

    def _setup_connections(self):
        ws = self._workspace_changed
        self._workspace_cb.currentIndexChanged.connect(ws)

    #======= DISPLAY =================================

    def _populate_workspaces(self):
        self._workspace_cb.clear()
        self._workspace_cb.addItems(self._tp_launcher.get_workspaces())

    #======= WORKSPACE + APP =================================

    def get_workspace(self):
        ''' Returns the currently selection workspace from combobox. '''
        return str(self._workspace_cb.currentText())

    def _workspace_changed(self):
        print('ham')

    def _testing(self):
        self._tp_launcher.add_workspace('My_first_workspace')
        self._tp_launcher.add_workspace('My_second_workspace')
        self._populate_workspaces()


if __name__ == '__main__':
    print (PY_VER)
    print (QT_VER)
    app = QtWidgets.QApplication(sys.argv)
    ex = TP_Launcher_GUI()
    ex.show()
    sys.exit(app.exec_())

# Copyright (c) 2017 Trevor Payne
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.