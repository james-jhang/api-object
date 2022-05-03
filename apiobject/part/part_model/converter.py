from apiobject.converter import Converter

from .part_model import PartModel

class PartModelConverter(Converter[PartModel]):
    @staticmethod
    def to_payload(resource: PartModel):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> PartModel:
        part_model = PartModel(
            payload['partModelId'],
            payload['partClass']['value'],
            payload['make']['value'],
            payload['model']['value'],
            payload['partNumber']['value'],
            payload['slotType']['value'],
        )
        if payload['imageIncluded']['value']:
            part_model.image = f"/gdcitdz/images/parts/{payload['partModelId']}_part.png"

        return part_model
