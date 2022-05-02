from apiobject.resource import Resource


class Model(Resource):
    def __init__(self, id, _class, subclass, make, name, rack_units, height) -> None:
        super().__init__(id)
        self._class = _class
        self.subclass = subclass
        self.make = make
        self.name = name
        self.rack_units = rack_units
        self.height = height

        # TODO complete all fields
        self.mounting = None
        self.form_factors = None