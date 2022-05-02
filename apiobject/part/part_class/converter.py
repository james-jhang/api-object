from apiobject.converter import Converter
from .part_class import PartClass

class PartClassConverter(Converter[PartClass]):

    @staticmethod
    def to_payload(resource: PartClass):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> PartClass:
        return PartClass(
            payload['id'],
            payload['label'],
            payload['assignableTo']['value'],
            [cls['value'] for cls in payload['classesForAssociation']],
        )
