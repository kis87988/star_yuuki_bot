# -*- coding: utf-8 -*-
"""
Yuuki_Libs
(c) 2020 Star Inc.
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
from .reader import Yuuki_WebDataReader

class Yuuki_WebAdminAPI:
    def __init__(self, YuukiData):
        self.YukkiData = YuukiData
        self.Yuuki_DataHandle = Yuuki_WebDataReader(YuukiData)
        self.events = {
            "": self.nothing,
            "get_logs": self.get_logs,
            "get_groups_joined": self.get_groups_joined,
        }

    def init(self, *, task="", data=None):
        return self.events[task](data)

    def get_groups_joined(self, data):
        if data:
            pass
        return self.YukkiData.getData(["Global", "GroupJoined"])

    def get_logs(self, data):
        return self.Yuuki_DataHandle.get_logs(data)

    @staticmethod
    def nothing(data):
        if data:
            pass
