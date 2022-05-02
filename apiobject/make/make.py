from apiobject.resource import Resource

class Make(Resource):
    def __init__(self, id, name) -> None:
        super().__init__(id)
        self.name = name

        # TODO complete all fields
        self.customer_service = None
        self.technical_support = None