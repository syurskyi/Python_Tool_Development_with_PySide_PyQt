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

        self._icons = QtWidgets.QFileIconProvider()                   # The QFileIconProvider class provides file icons for the QDirModel and the QFileSystemModel classes.
        self._my_path = os.path.dirname(os.path.realpath(__file__))   # path to the file
        images_path = os.path.join(self._my_path, 'images')           # path to the image
        full_path = os.path.join(images_path, 'TPayne_Launcher.png')  # full path to the image
        self._tpl_icon = QtGui.QIcon(full_path)                       # The PySide.QtGui.QIcon class provides scalable icons in different modes and states.
                                                                      # A PySide.QtGui.QIcon can generate smaller,
                                                                      # larger, active, and disabled pixmaps from the set of pixmaps it is given.
                                                                      # Such pixmaps are used by Qt widgets to show an icon representing a particular action.

        self._setup()

    #======= SETUP UI =================================

    def _setup(self):
        v_layout = QtWidgets.QVBoxLayout(self)

        v_layout.addLayout(self._setup_header())
        v_layout.addWidget(self._setup_apps())

        self.setWindowTitle('SYurskyi\'s Launcher ' + __version__)
        self.setWindowIcon(self._tpl_icon)
        flag = QtCore.Qt.WindowCloseButtonHint       # hide minimaze and maximize icons
        self.setWindowFlags(QtCore.Qt.Window | flag)
        self.resize(290, 300)

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


if __name__ == '__main__':
    print (PY_VER)
    print (QT_VER)
    app = QtWidgets.QApplication(sys.argv)
    ex = TP_Launcher_GUI()
    ex.show()
    sys.exit(app.exec_())

