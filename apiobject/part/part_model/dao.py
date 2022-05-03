from typing import List

from apiobject.dao import DAO
from apiobject.lookup.lookup import ValueID
from apiobject.part.part_model.part_model import PartModel
from apiobject.user import User

from ..part_class.dao import PartClassDAO
from .converter import PartModelConverter


class PartModelDAO(DAO):
    def __init__(self, user: User) -> None:
        super().__init__(user)

    def create(self,
            part_class: str,
            make: str,
            model: str,
            part_number: str,
            slot_type: ValueID,
            description: str = None,
            oem_part: str = None,
            upc_sku: str = None,
            height: float = None,
            width: float = None,
            depth: float = None,
            weight: float = None,
            notes: str = None,
            threshold_contacts: List[User] = [],
            made_in: str = None,
            warranty_period: int = None,
            image: str = None) -> PartModel:

        part_class = PartClassDAO(user=self.user).get(name=part_class)

        payload = {
            "partClass": { "id": part_class.id },
            "make": { "value": make },
            "model": { "value": model },
            "partNumber": { "value": part_number },
            "partModelDesc": { "value": description },
            "oemPartNumber": { "value": oem_part },
            "upcSku": { "value": upc_sku },
            "dimH": { "value": height },
            "dimW": { "value": width },
            "dimD": { "value": depth },
            "weight": { "value": weight },
            "slotType": { "code": slot_type.id },
            "notes": { "value": notes },
            "partModelThresholdContacts": {
                "value": self.user_email_mapping(threshold_contacts) if threshold_contacts else None
            },
            "madeIn": {
                "id": self.get_make_id(made_in) if made_in else None
            },
            "warrantyPeriod": { "value": warranty_period },
            "partModelStatus": { "code": 93301 },
            "imageUri": { "value": image },
            "imageIncluded": { "value": bool(image) },
            "partModelCustomFields": [] # TODO
        }
        resp = self.user.http.request('POST', '/part_models', json=payload).json()
        return PartModelConverter.to_resource(resp)

    def delete(self, part_model: PartModel):
        payload = {'partModels':[{'partModelId': part_model.id}]}
        resp = self.user.http.request('PUT', '/part_models/bulk/delete', json=payload).json()

    def upload(self, image) -> str:
        file = {'file':  ("1.png", open(image, "rb"), "image/png")}
        resp = self.user.http.request('POST', '/part_models/images', files=file).json()
        uri = resp['results'][0]['newFileName']
        return uri