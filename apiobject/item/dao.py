from apiobject.dao import DAO

from ..user.user import User
from .converter import ItemConverter
from .item import Item
from apiobject.make import MakeDAO
from apiobject.model import ModelDAO
from apiobject.location import LocationDAO

class ItemDAO(DAO):
    def __init__(self, user: User) -> None:
        super().__init__(user)

    def create(self, name, make, model, status, location, **payload) -> Item:
        make = MakeDAO(user=self.user).get(name=make)
        model = ModelDAO(user=self.user).get(name=model)
        location = LocationDAO(user=self.user).get(code=location)

        ports = self.get_item_ports_info(model.id)
        dataPorts = self.get_port_info(ports['tabDataPorts'])
        powerPorts = self.get_port_info(ports['tabPowerPorts'])
        itemData = {
            "fields": [
                {"label": "tiName", "data": name},
                {"label": "cmbMake", "data": make.id},
                {"label": "cmbModel", "data": model.id},
                {"label": "cmbLocation", "data": location.id},
                {"label": "cmbStatus", "data": status.id},
            ],
            "dataPorts":dataPorts,
            "powerPorts": powerPorts,
            "sensorPorts": [],
            "customFields": []
        }

        fields_info = self.total_fields()
        for column, value in payload.items():
            for field_info in fields_info:
                if field_info['label'] == column :
                    itemData["fields"].append({
                        "label": field_info["uiComponentId"], "data": value
                    })
                    break

        item_id = self.user.http.request('POST','/items/-1', json=itemData).json()
        return self.get_item(item_id)

    def get_item(self, id) -> Item:
        item = self.user.http.request('GET', f'/items/details/{id}').json()
        return ItemConverter.to_resource(item)

    def get_item_ports_info(self, modelId):
        resp = self.user.http.request('GET', '/items/details/empty/%s' % modelId).json()
        return resp['item']

    def get_port_info(self, port_info):
        ports = port_info['value']
        for port in ports:
            port["itemId"]= -1
            port["portId"]= None
        return ports

    def total_fields(self, match=None):
        totalFields = self.user.http.request('GET', '/quicksearch/items/itemListFields').json()
        if callable(match):
            return [field for field in totalFields if match(field)]
        else:
            return totalFields


    def delete(self, item: Item):
        payload = [item.id]
        resp = self.user.http.request('POST', '/items/delete/false', json=payload).json()