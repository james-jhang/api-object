from typing import List

from apiobject.lookup.modelFields import *

from ..resource import Resource
from ..user.user import User
from ..part.part import Part
import json

class Item(Resource):
    def __init__(self, user: User, id=None) -> None:
        self.user = user
        self.id = None
        self.item_name = None
        self.make = None
        self.model = None
        self.status = None
        self.location = None
    
    def get_item_ports_info(self, modelId):
        resp = self.user.http.request('GET', '/items/details/empty/%s' % modelId, json=payload).json()
        if resp.status_code != 200:
            raise Exception('Can not get item ports info: %s' % resp.content.decode('utf-8'))
        return resp.json()['item']

    def get_port_info(self, port_info):
        ports = port_info['value']
        for port in ports:
            port["itemId"]= -1
            port["portId"]= None
        return ports

    def total_fields(self, match=None):
        resp = self.user.http.request('GET', '/items/itemListFields', json=payload).json()
        totalFields = json.loads(resp.content.decode('utf-8'))
        if callable(match):
            return [field for field in totalFields if match(field)]
        else:
            return totalFields

    def create(self, item_name, make, model, status, location, **payload):
        ports = self.get_item_ports_info(model.id)
        dataPorts = self.get_port_info(ports['tabDataPorts'])
        powerPorts = self.get_port_info(ports['tabPowerPorts'])
        itemData = {
            "fields": [
                {"label": "cmbLocation", "data": location.id},
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

        self.id = resp['id']

        fields_info = self.total_fields()
        for column, value in payload.items():
            for field_info in fields_info:
                if field_info['label'] == column :
                    itemData["fields"].append({
                        "label": field_info["uiComponentId"], "data": value
                    })
                    break

        resp = self.user.http.request('POST','/items/-1',
            headers={'Content-Type': 'application/json'}, data=json.dumps(itemData)
        )