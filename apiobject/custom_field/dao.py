from typing import List

from apiobject.dao import DAO
from apiobject.lookup.lookup import ValueID
from apiobject.user import User

from .converter import CustomFieldConverter, PanelConverter
from .custom_field import CustomField
from .panel import Panel


class CustomFieldDAO(DAO):
    def __init__(self, user: User) -> None:
        super().__init__(user)

    def create_custom_field(self,
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

    def create_panel(self, subtab_title, subtab_class, name, width=2, height=3):
        # TODO subtab is fixed so it is not a Resource.
        # How do we handle subtab?
        subtab = self.get_subtab(subtab_title, subtab_class)
        payload = {
            "subtabId": subtab['subtabId'],
            "panels":[
                {
                    "panelName": name,
                    # TODO column unit: 2, row unit: 3
                    "column": 0,
                    "row": 0,
                    "height": height,
                    "width": width
                }
            ]
        }
        resp = self.user.http.request('POST', '/settings/lists/subtabs/panel', json=payload).json()
        return PanelConverter.to_resource(resp)

    def get_subtab(self, subtab_title, subtab_class):
        subtabs = self.user.http.request('GET', '/settings/lists/subtabs').json()
        for subtab in subtabs:
            if subtab['tiSubtabName'] == subtab_title and \
                subtab['tiSubtabType']['value'] == subtab_class:
                return subtab

    def delete_custom_field(self, custom_field: CustomField):
        payload = {
            "method": "delete",
            "ids": [custom_field.id]
        }
        resp = self.user.http.request('POST', '/settings/lists/customFields/bulk', json=payload).json()

    def delete_panel(self, panel: Panel):
        resp = self.user.http.request('DELETE', '/settings/lists/subtabs/panel/%s' % panel.id)
