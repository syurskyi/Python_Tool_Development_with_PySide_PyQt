#!/usr/bin/env python

from collections import OrderedDict
import os


class TP_Launcher_Model:
    def __init__(self):
        self._workspaces = OrderedDict()

    # ======== WORKSPACES ============
    
    def add_workspace(self, ws_name):
        self._workspaces[ws_name] = OrderedDict()

    def get_workspaces(self):
        return list(self._workspaces.keys()) # Python 3.0+ conversion

    def delete_workspace(self, ws_name):
        del self._workspaces[ws_name]


