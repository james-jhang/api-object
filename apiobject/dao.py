from apiobject.user import User

class DAO:
    def __init__(self, user: User) -> None:
        self.user = user