# from typing import List

from apiobject.lookup.modelFields import *

from ..resource import Resource
# from ..user.user import User
# import json

class Item(Resource):
    def __init__(self, id, make, model, name, location) -> None:
        super().__init__(id)
        # self.user = user
        self.name = name
        self.make = make
        self.model = model
        self.location = location

        # TODO complete all fields
        self.status = None
        self.class_subclass = None

    # def get_item_ports_info(self, modelId):
    #     resp = self.user.http.request('GET', '/items/details/empty/%s' % modelId).json()
    #     return resp['item']

    # def get_port_info(self, port_info):
    #     ports = port_info['value']
    #     for port in ports:
    #         port["itemId"]= -1
    #         port["portId"]= None
    #     return ports

    # def total_fields(self, match=None):
    #     totalFields = self.user.http.request('GET', '/quicksearch/items/itemListFields').json()
    #     if callable(match):
    #         return [field for field in totalFields if match(field)]
    #     else:
    #         return totalFields

    # def create(self, item_name, make, model, status, location, **payload):
    #     ports = self.get_item_ports_info(model.id)
    #     dataPorts = self.get_port_info(ports['tabDataPorts'])
    #     powerPorts = self.get_port_info(ports['tabPowerPorts'])
    #     itemData = {
    #         "fields": [
    #             {"label": "cmbLocation", "data": location.id},
    #             {"label": "cmbMake", "data": make.id},
    #             {"label": "cmbModel", "data": model.id},
    #             {"label": "cmbStatus", "data": status.id},
    #             {"label": "tiName", "data": item_name}
    #         ],
    #         "dataPorts":dataPorts,
    #         "powerPorts": powerPorts,
    #         "sensorPorts": [],
    #         "customFields": []
    #     }

    #     fields_info = self.total_fields()
    #     for column, value in payload.items():
    #         for field_info in fields_info:
    #             if field_info['label'] == column :
    #                 itemData["fields"].append({
    #                     "label": field_info["uiComponentId"], "data": value
    #                 })
    #                 break

    #     resp = self.user.http.request('POST','/items/-1', json=itemData).json()
    #     self.id = resp

    # def delete(self):
    #     payload = [self.id]
    #     resp = self.user.http.request('POST','/items/delete/false', json=payload).json()