from apiobject.resource import Resource

class Location(Resource):
    def __init__(self, id, code, name, level_in_hierarchy, country, area) -> None:
        super().__init__(id)
        self.code = code
        self.name = name
        self.level_in_hierarchy = level_in_hierarchy
        self.country = country
        self.area = area

        # TODO complete all fields
        self.parent =None
        self.type = None