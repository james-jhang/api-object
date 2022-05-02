from apiobject.converter import Converter

from .make import Make

class MakeConverter(Converter[Make]):

    @staticmethod
    def to_payload(resource: Make):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> Make:
        return Make(
            payload['mfrId'],
            payload['cmbMake']['value']
        )