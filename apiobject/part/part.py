from typing import List

from apiobject.lookup.fields import Location, PartStatus, TrackingType

from ..resource import Resource
from ..user.user import User

class PartClass(Resource):
    def __init__(self, user: User, id=None) -> None:
        self.user = user
        self.id = None
        self.label = None
        self.assignableTo = None
        self.classesForAssociation = None

    def create(self, class_label, assignment_level, classes):
        payload = {
            "label": class_label,
            "assignableTo": assignment_level.pair(),
            "classesForAssociation": [cls.pair() for cls in classes]
        }
        resp = self.user.http.request('POST', '/parts/classes', json=payload).json()
        self.id = resp['id']
        self.label = resp['label']
        self.assignableTo = resp['assignableTo']
        self.classesForAssociation = resp['classesForAssociation']

    def delete(self):
        payload = [{'id': self.id}]
        resp = self.user.http.request('PUT', '/parts/classes/bulk/delete', json=payload).json()

    def get(self):
        resp = self.user.http.request('GET', '/parts/classes')
        return resp.json()


class Image:
    pass
    # TODO

class PartModel(Resource):
    def __init__(self, user: User) -> None:
        super().__init__()
        self.user = user

    def create(self,
            part_class: PartClass,
            make: str,
            model: str,
            part_number: str,
            slot_type: str,
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
            image: Image = None):

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
            "imageUri": { "value": image.uri if image else None },
            "imageIncluded": { "value": bool(image) },
            "partModelCustomFields": [] # TODO
        }
        resp = self.user.http.request('POST', '/part_models', json=payload).json()
        self.id = resp['partModelId']
        return resp
        # TODO how to handle resp?

    def delete(self):
        payload = {'partModels':[{'partModelId': self.id}]}
        resp = self.user.http.request('PUT', '/part_models/bulk/delete', json=payload).json()

class Part(Resource):
    def __init__(self, user: User) -> None:
        super().__init__()
        self.user = user

    def create(self,
        part_model: PartModel,
        make: str,
        serial_number: str,
        part_status: PartStatus,
        location: Location,
        tracking_type: TrackingType,
        count_in_stock: int = None,
        count_in_use: int = None,
        threshold: int = None, **payload):
        part_payload = {
            "partMake":{"value":make}, "partModel":{"id":part_model.id}, "partStatus": {"id": part_status.id},
            "countInStock":{"value": count_in_stock},"countInUse":{"value": count_in_use},
            "location": {"id": location.id}, "threshold": {"value": threshold},
            "serialNumber":{"value": serial_number}, "trackingType": {"code": tracking_type.id}
        }
        for uiComponentId, value in payload.items():
            part_payload.update({uiComponentId:{"value":value}})
        
        resp = self.user.http.request('POST', '/parts', json=part_payload).json()
        self.id = resp['partId']
        return resp
    
    def delete(self):
        payload = {'parts':[{'partId': self.id}]}
        resp = self.user.http.request('PUT', '/parts/bulk/delete', json=payload).json()
