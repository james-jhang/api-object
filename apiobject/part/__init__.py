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
