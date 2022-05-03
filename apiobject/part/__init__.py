from typing import List

from apiobject.lookup.fields import *

from .part_model import PartModel
from apiobject.location import Location

from ..resource import Resource
from ..user.user import User
from ..item.item import Item
import json

class PartsManagement:
    def __init__(self, user: User) -> None:
        self.user = user

    def enable_parts_management(self):
        payload = {
            "settingType": "APPLICATION_SETTING",
            "partsManagementEnabled": True
        }
        resp = self.user.http.request('PUT', '/settings/dctrack', json=payload)

    def disable_parts_management(self):
        payload = {
            "settingType": "APPLICATION_SETTING",
            "partsManagementEnabled": False
        }
        resp = self.user.http.request('PUT', '/settings/dctrack', json=payload)


class Panel(Resource):
    def __init__(self, id, user: User) -> None:
        super().__init__(id)
        self.user = user

    def create(self, subtab, name):
        payload = {
            "subtabId": subtab.id,
            "panels": [{
                "panelName": name,
                "column": 0,
                "row": 0,
                "height": 3,
                "width": 2}]
        }

        resp = self.user.http.request('POST', '/settings/lists/subtabs/panel', json=payload).json()
        self.id = resp['panels'][0]['panelId']
        return resp

    def delete(self):
        resp = self.user.http.request('DELETE', '/settings/lists/subtabs/panel/%s' % self.id)