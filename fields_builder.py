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
        'TrackingType' :'PART_TRACKING_TYPE'
    }
    field_detail_key_mapping = {
        'PartStatus': 'PART_STATUS',
        'Location': 'LOCATION'
    }
    with open(f'./apiobject/lookup/fields.py', 'w') as f:
        f.write('from .lookup import ValueID\n\n')
        for field, field_key  in field_key_mapping.items():
            f.write(f'class {field}:\n')
            value_id_mappings = lookup[field_key]
            for value_id in value_id_mappings:
                value = value_id['value']
                id = value_id['id']
                f.write(f'\t{value.upper().replace(" ", "_")} = ValueID(\'{value}\', {id})\n')
            f.write(f'\n\n')
        for field, field_key  in field_detail_key_mapping.items():
            f.write(f'class {field}:\n')
            value_id_mappings = lookupObject.field_detail(field_detail_key_mapping[field])
            for value_id in value_id_mappings:
                value = value_id['value']
                id = value_id['id']
                f.write(f'\t{value.upper().replace(" ", "_")} = ValueID(\'{value}\', {id})\n')
            f.write(f'\n\n')