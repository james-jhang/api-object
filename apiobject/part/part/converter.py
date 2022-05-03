from apiobject.converter import Converter

from .part import Part

class PartConverter(Converter[Part]):
    @staticmethod
    def to_payload(resource: Part):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> Part:
        part = Part(
            payload['partId'],
            payload['make']['value'],
            payload['model']['value'],
            payload['partNumber']['value'],
            payload['countInStock']['value'],
            payload['countInUse']['value'],
            payload['partStatus']['value'],
            payload['location']['value'],
            payload['threshold']['value']
        )
        part.tracking_type = payload['trackingType']['value']
        return part