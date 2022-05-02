from apiobject.resource import Resource

class PartModel(Resource):
    def __init__(self, id, _class, make, name, part_number, slot_type) -> None:
        super().__init__(id)
        self._class = _class
        self.make = make
        self.name = name
        self.part_number = part_number
        self.slot_type = slot_type
