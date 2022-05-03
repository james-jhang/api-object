from typing import List

from apiobject.dao import DAO
from apiobject.lookup.lookup import ValueID
from apiobject.user import User

from .converter import CustomFieldConverter
from .custom_field import CustomField


class CustomFieldDAO(DAO):
    def __init__(self, user: User) -> None:
        super().__init__(user)

    def create(self,
            label: str,
            appliesTo: List[ValueID],
            fieldType: ValueID,
            classes: List[ValueID]=[],
            subclasses: List[ValueID]=[],
            partClasses: List[ValueID]=[],
            applyToModels: bool=False):
        if (not classes) and (not subclasses) and (not partClasses):
            raise Exception('Either classes, subclasses, or partClasses should be provided.')

        payload = {
            "tiLabel": {"value": label},
            "cmbAppliedTo": [_type.value for _type in appliesTo],
            "cmbClass": {
                "value": [cls.pair() for cls in classes]
            },
            "cmbSubclass": {
                "value": [subcls.pair() for subcls in subclasses]
            },
            "cmbUserDefClass": [pcls.pair() for pcls in partClasses],
            "tiType": {"value": {"id": fieldType.id}},
            "chkApplyToModel": applyToModels
        }
        resp = self.user.http.request('POST', '/settings/lists/customFields', json=payload).json()['listContent']
        return CustomFieldConverter.to_resource(resp)


    def delete(self, custom_field: CustomField):
        payload = {
            "method": "delete",
            "ids": [custom_field.id]
        }
        resp = self.user.http.request('POST', '/settings/lists/customFields/bulk', json=payload).json()
