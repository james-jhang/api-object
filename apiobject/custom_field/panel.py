from apiobject.resource import Resource

class Panel(Resource):
    def __init__(self, id, subtab_id, name, width, height) -> None:
        super().__init__(id)
        self.subtab_id = subtab_id
        self.name = name
        self.width = width
        self.height = height

        self.row = None
        self.column = None