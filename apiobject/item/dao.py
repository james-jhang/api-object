from apiobject.dao import DAO
from ..user.user import User
from .converter import ItemConverter

class ItemDAO(DAO):
    def __init__(self, user) -> None:
        super().__init__()
        self.user: User = user

    def create(self, name, make, model, status, location, **payload) -> Item:
        ports = self.get_item_ports_info(model.id)
        dataPorts = self.get_port_info(ports['tabDataPorts'])
        powerPorts = self.get_port_info(ports['tabPowerPorts'])
        itemData = {
            "fields": [
                {"label": "cmbLocation", "data": location.id},
                {"label": "cmbMake", "data": make.id},
                {"label": "cmbModel", "data": model.id},
                {"label": "cmbStatus", "data": status.id},
                {"label": "tiName", "data": name}
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
        return self.get_item(id=item_id)

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