from typing import List

from apiobject.lookup.fields import *

from ..resource import Resource
from ..user.user import User
from ..part.part import Part
import json

class Item(Resource):
    def __init__(self, user: User, id=None) -> None:
        self.user = user
        self.id = None
        self.item_name = None
        self.makke = None
        self.model = None
        self.status = None
        self.location = None

    def create(self, item_name, make, model, status, location:Location):

        payload = {
            "itemId": -1,
            "fields": [
                {"label": "cmbLocation", "data": location},
                {"label": "cmbMake", "data": make.id},
                {"label": "cmbModel", "data": model.id},
                {"label": "cmbStatus", "data": status.id},
                {"label": "tiName", "data": item_name}
            ],
            "dataPorts":dataPorts,
            "powerPorts": powerPorts,
            "sensorPorts": [],
            "customFields": []
        }
        resp = self.user.http.request('POST', '/items/-1', json=payload).json()
        self.id = resp['id']
        self.label = resp['label']
        self.assignableTo = resp['assignableTo']
        self.classesForAssociation = resp['classesForAssociation']

    def delete(self):
        payload = [{'id': self.id}]
        resp = self.user.http.request('PUT', '/parts/classes/bulk/delete', json=payload).json()

    def get(self):
        resp = self.user.http.request('GET', '/parts/classes')
        return resp.json()


# @keyword(name='HTTP Request::Add An Item')
#     def http_request_add_an_item(self, make_name, model_name, item_name, status, Location=1, **payload):
#         make_id = self.http_request_get_make_id(make_name)
#         model_id = self.http_request_get_model_id(make_id, model_name)
#         item_status_info = self.rest.get_item_status_info(model_id)
#         item_status_id = [item_status['id'] for item_status in item_status_info if item_status['value'] == status][0]
#         ports = self.rest.get_item_ports_info(model_id)
#         dataPorts = self.get_port_info(ports['tabDataPorts'])
#         powerPorts = self.get_port_info(ports['tabPowerPorts'])
#         itemData = {
#             "itemId": -1,
#             "fields": [
#                 {"label": "cmbLocation", "data": Location},
#                 {"label": "cmbMake", "data": make_id},
#                 {"label": "cmbModel", "data": model_id},
#                 {"label": "cmbStatus", "data": item_status_id},
#                 {"label": "tiName", "data": item_name}
#             ],
#             "dataPorts":dataPorts,
#             "powerPorts": powerPorts,
#             "sensorPorts": [],
#             "customFields": []
#         }
#         fields_info = self.rest.total_fields()
#         for column, value in payload.items():
#             for field_info in fields_info:
#                 if field_info['label'] == column :
#                     itemData["fields"].append({
#                         "label": field_info["uiComponentId"], "data": value
#                     })
#                     break
#         self.rest.add_item(itemData)