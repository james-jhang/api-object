import re
from codecs import lookup

if __name__ == '__main__':
    from apiobject.user.user import Administrator
    from apiobject.lookup.lookup import Lookup
    admin = Administrator('192.168.1.20', 'admin', 'Lab1321*')
    admin.login()
    lookup = Lookup(admin).lookup
    lookupObject = Lookup(admin)

    field_key_mapping = {
        'AssignmentLevel': 'PART_ASSIGNMENT_TYPE',
        'Class': 'CLASS',
        'SoltType': 'PART_SLOT_TYPE',
        'TrackingType' :'PART_TRACKING_TYPE',
        'CustomFieldDataType': 'CUSTOM_FIELD_DATA_TYPE',
        'ItemStatus': 'ITEM_STATUS',
        'SubtabType': 'SUBTAB_TYPE',
        'Subclass': 'SUBCLASS'
    }
    field_detail_key_mapping = {
        'PartStatus': 'PART_STATUS',
        # 'Location': 'LOCATION',
        'PartClass':'PART_CLASS',
        # 'Make': 'MAKE',
        'ProjectNumber': 'PROJECT_NUMBER'
    }
    with open(f'./apiobject/lookup/fields.py', 'w') as f:
        f.write('from .lookup import ValueID\n\n')
        for field, field_key  in field_key_mapping.items():
            f.write(f'class {field}:\n')
            value_id_mappings = lookup[field_key]
            for value_id in value_id_mappings:
                value = value_id['value']
                id = value_id['id']
                resultValue = (re.sub("\>|-|\.| ", "_", value_id["value"]).upper())
                f.write(f'\t{resultValue} = ValueID(\'{value}\', {id})\n')
            f.write(f'\n\n')

        for field, field_key in field_detail_key_mapping.items():
            if field == 'PartClass':
                f.write(f'class {field}Field:\n')
            else:
                f.write(f'class {field}:\n')
            value_id_mappings = lookupObject.field_detail(field_detail_key_mapping[field])
            for value_id in value_id_mappings:
                value = value_id['value']
                id = value_id['id']
                if re.match('^[0-9]', value):
                    resultValue = "_" + str(value)
                    resultValue = (re.sub("/|\.|\(|\)|-|\+|\,|\&|\=|\*|\^|#| ", "_", resultValue).upper())
                else:
                    resultValue = (re.sub("/|\.|\(|\)|-|\+|\,|\&|\=|\*|\^|#| ", "_", value).upper())
                f.write(f'\t{resultValue} = ValueID(\'{value}\', {id})\n')
            f.write(f'\n\n')

    # model_key = {
    #     'Model': 'MODEL'
    # }

    # with open(f'./apiobject/lookup/modelFields.py', 'w') as f:
    #     f.write('from .lookup import ValueID\n\n')
    #     for field, field_key in model_key.items():
    #         f.write(f'class {field}:\n')
    #         value_id_mappings = lookupObject.field_detail(model_key[field])
    #         for value_id in value_id_mappings:
    #             value = value_id['value']
    #             id = value_id['id']
    #             if re.match('^[0-9]', value):
    #                 resultValue = "_" + str(value)
    #                 resultValue = (re.sub("/|\.|\(|\)|-|\+|\,|\&|\=|\*|\^|#| ", "_", resultValue).upper())
    #             else:
    #                 resultValue = (re.sub("/|\.|\(|\)|-|\+|\,|\&|\=|\*|\^|#| ", "_", value).upper())
    #             f.write(f'\t{resultValue} = ValueID(\'{value}\', {id})\n')
    #         f.write(f'\n\n')

    subtab_key_mapping = {
        'Custom Fields': ['Part','PartModel']
    }

    subtab = lookupObject.subtab_detail()
    with open(f'./apiobject/lookup/subtabs.py', 'w') as f:
        f.write('from .lookup import ValueID\n\n')
        f.write(f'class Subtabs:\n')
        for i in range(len(subtab)):
            for subtabName, subtabType in subtab_key_mapping.items():
                for j in range(2):
                    if (subtab[i]["tiSubtabName"] == subtabName) & (subtab[i]["tiSubtabType"]["value"] == subtabType[j]):
                        subtabName = re.sub('>|-| ', '_', subtab[i]["tiSubtabName"])
                        subtabType = subtab[i]["tiSubtabType"]["value"]
                        subtabId = subtab[i]["subtabId"]
                        f.write(f'\t{subtabName.upper().replace(" ", "_")}_{subtabType.upper().replace(" ", "_")} = ValueID(\'{subtabType}\', {subtabId})\n')