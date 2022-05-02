from apiobject.lookup.modelFields import *

from ..resource import Resource


class Item(Resource):
    def __init__(self, id, make, model, name, location) -> None:
        super().__init__(id)
        self.name = name
        self.make = make
        self.model = model
        self.location = location

        # TODO complete all fields
        self.status = None
        self.class_subclass = None
