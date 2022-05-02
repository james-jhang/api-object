from apiobject.converter import Converter

from .model import Model


class ModelConterver(Converter[Model]):

    @staticmethod
    def to_payload(resource: Model):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> Model:
        return Model(
            payload['modelId'],
            payload['tiClass']['value'],
            payload['tiSubclass']['value'],
            payload['cmbMake']['value'],
            payload['cmbModel']['value'],
            payload['tiRuHeight']['value'],
            payload['tiDimHeight']['value']
        )
