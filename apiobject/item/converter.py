from apiobject.converter import Converter
from .item import Item

class ItemConverter(Converter):
    
    @staticmethod
    def to_payload():
        pass

    @staticmethod
    def to_resource(response):
        detail = response['item']
        item = Item(
            id=detail['tiName']['valueId'],
            make=detail['cmbMake'],
            model=detail['cmbModel'],
            name=detail['tiName']['value'],
            location=detail['cmbLocation']
        )
        # TODO complete all fields
        item.class_subclass(detail['tiClass'])
        # ...

        return item

