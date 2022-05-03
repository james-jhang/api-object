from apiobject.resource import Resource

class CustomField(Resource):
    def __init__(self, id, label, apply_to, classes, subclasses, part_classes, _type) -> None:
        super().__init__(id)
        self.label = label
        self.apply_to = apply_to
        self.classes = classes
        self.subclasses = subclasses
        self.part_classes = part_classes
        self._type = _type

        self.apply_to_models = None