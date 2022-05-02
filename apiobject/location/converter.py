from apiobject.converter import Converter

from .location import Location


class LocationConterver(Converter[Location]):

    @staticmethod
    def to_payload(resource: Location):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> Location:
        return Location(
            payload['locationId'],
            payload['tiLocationCode']['value'],
            payload['tiLocationName']['value'],
            # TODO save value or id?
            payload['cmbHierarchyLevel']['value']['value'],
            payload['cmbAddressCountry']['value']['value'],
            payload['tiLocationArea']['value']
        )
