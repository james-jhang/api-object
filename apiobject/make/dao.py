from apiobject.dao import DAO
from apiobject.user import User

from .conterver import MakeConverter


class MakeDAO(DAO):

    def __init__(self, user: User) -> None:
        super().__init__(user)

    def get(self, name):
        url = '/make'
        makes = self.user.http.request('GET', url, prefix='/dcTrackApp/api/v1').json()['makes']
        for make in makes:
            r_make = MakeConverter.to_resource(make)
            if r_make.name == name:
                return r_make

