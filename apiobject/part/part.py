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



class Part(Resource):
    def __init__(self, id, user: User) -> None:
        super().__init__(id)
        self.user = user

    def create(self,
        part_model: PartModel,
        make: str,
        serial_number: str,
        part_status: PartStatus,
        location: Location,
        tracking_type: TrackingType,
        count_in_stock: int = None,
        count_in_use: int = None,
        threshold: int = None, **payload):
        part_payload = {
            "partMake":{"value":make}, "partModel":{"id":part_model.id}, "partStatus": {"id": part_status.id},
            "countInStock":{"value": count_in_stock},"countInUse":{"value": count_in_use},
            "location": {"id": location.id}, "threshold": {"value": threshold},
            "serialNumber":{"value": serial_number}, "trackingType": {"code": tracking_type.id}
        }
        for uiComponentId, value in payload.items():
            part_payload.update({uiComponentId:{"value":value}})

        resp = self.user.http.request('POST', '/parts', json=part_payload).json()
        self.id = resp['partId']
        return resp

    def delete(self):
        payload = {'parts':[{'partId': self.id}]}
        resp = self.user.http.request('PUT', '/parts/bulk/delete', json=payload).json()

    def assign_to_item(self, item:Item, serial_number=None, quantity=1, reason=None, project:ProjectNumber=None, tracking_number=None):
        payload = {
            "itemId": item.id,
            "partId": self.id,
            "reason": reason,
            "quantity": quantity,
            "projectId": project.id if project else None ,
            "serialNumber": serial_number,
            "trackingNumber": tracking_number
        }
        resp = self.user.http.request('POST', '/parts/assignments/items', json=payload).json()
        self.partItemAssignmentIds = resp['partItemAssignmentIds']

    def unassign_from_item(self, item: Item):
        payload = {
            "partItemAssignmentIds": self.partItemAssignmentIds,
            "isDeletePorts": False,
            "reason": ""
        }
        resp = self.user.http.request('POST', '/parts/assignments/items/deletes', json=payload).json()

    # def get_assign_part_in_item(self, item):
    #     item_id = self.get_filter_items('tiName', [item])['searchResults']['items'][0]['id']
    #     payload = {"columns": [{"name": "itemId", "filter": {"eq":  item_id}}],
    #                "selectedColumns": [{"name": "partItemAssignmentId"}, {"name": "partId"}]}
    #     url = f'{self.url}/dcTrackApp/api/v2/parts/assignments/items/list?pageNumber=1&pageSize=-1'
    #     resp = self.request.post(url, json=payload)
    #     if resp.status_code != 200:
    #         raise Exception('Get assigning parts item fail: %s' % resp.content.decode('utf-8'))
    #     return resp.json()['partItemAssignments']

    # def unassign_all_parts(self, partItemAssignments, part_batch_number):
    #     def get_batch_number_filter(batch_number):
    #         filter = {"columns":[{"name":"serialNumber","filter":{"contains":"\""+batch_number+"\""},"displayValue":"\""+batch_number+"\""}],"selectedColumns":[]}
    #         return filter
    #     payload = {"partItemAssignmentIds": [partItemAssignment['partItemAssignmentId'] for partItemAssignment in partItemAssignments if partItemAssignment['partId'] == self.search_parts_by_conditions(get_batch_number_filter(part_batch_number))[0]['partId']], "isDeletePorts": False, "reason": ""}
    #     url = f'{self.url}/dcTrackApp/api/v2/parts/assignments/items/deletes'
    #     resp = self.request.post(url, json=payload)
    #     if resp.status_code != 200:
    #         raise Exception('Unassigning part to item fails: %s' % resp.content.decode('utf-8'))


class CustomField(Resource):
    def __init__(self, id, user: User) -> None:
        super().__init__(id)
        self.user = user

    def create(self, name:str, appliesTo:str, classes:PartClassField, fieldType:CustomFieldDataType, applyToModels=None):
        payload = {
            "tiLabel": {"value": name},
            "cmbAppliedTo": [appliesTo],
            "cmbClass": None,
            "cmbUserDefClass": [{"id": classes.id}],
            "cmbSubclass": {"value": []},
            "tiType": {"value": {"id": fieldType.id}},
            "chkApplyToModel": applyToModels
        }
        resp = self.user.http.request('POST', '/settings/lists/customFields', json=payload).json()
        self.id = resp['listContent']['contentDetailId']
        return resp

    def delete(self):
        payload = {
            "method": "delete",
            "ids": [
                self.id
            ]
        }
        resp = self.user.http.request('POST', '/settings/lists/customFields/bulk', json=payload).json()


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