from apiobject.converter import Converter

from .item import Item


class ItemConverter(Converter[Item]):

    @staticmethod
    def to_payload(resource: Item):
        pass

    @staticmethod
    def to_resource(payload) -> Item:
        detail = payload['item']
        item = Item(
            id=detail['tiName']['valueId'],
            make=detail['cmbMake']['value'],
            model=detail['cmbModel']['value'],
            name=detail['tiName']['value'],
            location=detail['cmbLocation']['value']
        )
        # TODO complete all fields
        item.class_subclass = detail['tiClass']['value']
        # ...

        return item

