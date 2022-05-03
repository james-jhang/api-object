from apiobject.dao import DAO
from apiobject.location import LocationDAO
from apiobject.lookup.fields import ValueID
from apiobject.user import User

from ..part_model import PartModelDAO
from .converter import PartConverter
from .part import Part


class PartDAO(DAO):
    def __init__(self, user: User) -> None:
        super().__init__(user)

    def create(self,
        part_model: str,
        make: str,
        part_status: ValueID,
        location: str,
        tracking_type: ValueID,
        batch_number: str,
        threshold: int = 0,
        count_in_stock: int = None,
        count_in_use: int = None,
        **payload):

        part_model = PartModelDAO(user=self.user).get(part_model)
        location = LocationDAO(user=self.user).get(location)

        # TODO batch_number should be unique.
        # Should we check the batch_number here?

        part_payload = {
            "partMake": {"value":make},
            "partModel":{"id":part_model.id},
            "partStatus": {"id": part_status.id},
            "countInStock":{"value": count_in_stock},
            "countInUse":{"value": count_in_use},
            "location": {"id": location.id},
            "threshold": {"value": threshold},
            "serialNumber":{"value": batch_number},
            "trackingType": {"code": tracking_type.id}
        }
        for uiComponentId, value in payload.items():
            part_payload.update({uiComponentId:{"value":value}})

        resp = self.user.http.request('POST', '/parts', json=part_payload).json()
        return PartConverter.to_resource(resp)

    def delete(self, part: Part):
        payload = {'parts':[{'partId': part.id}]}
        resp = self.user.http.request('PUT', '/parts/bulk/delete', json=payload).json()
