from apiobject.converter import Converter

from .custom_field import CustomField
from .panel import Panel

class CustomFieldConverter(Converter[CustomField]):
    @staticmethod
    def to_payload(resource: CustomField):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> CustomField:
        custom_field = CustomField(
            payload['contentDetailId'],
            payload['tiLabel']['value'],
            payload['cmbAppliedTo'],
            [cls['value'] for cls in payload['cmbClass']['value']],
            [subcls['value'] for subcls in payload['cmbSubclass']['value']],
            [pcls['value'] for pcls in payload['cmbUserDefClass']],
            payload['tiType']['value']['value']
        )
        custom_field.apply_to_models = payload['chkApplyToModel']
        return custom_field

class PanelConverter(Converter[Panel]):
    @staticmethod
    def to_payload(resource: Panel):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> Panel:
        panel_payload = payload['panels'][0]
        panel = Panel(
            panel_payload['panelId'],
            payload['subtabId'],
            panel_payload['panelName'],
            panel_payload['width'],
            panel_payload['height']
        )
        panel.row = panel_payload['row']
        panel.column = panel_payload['column']
        return panel

