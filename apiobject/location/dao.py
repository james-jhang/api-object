from apiobject.dao import DAO
from apiobject.user import User

from .converter import LocationConterver

class LocationDAO(DAO):
    def __init__(self, user: User) -> None:
        super().__init__(user)

    def get(self, code):
        url = '/locations/locationList?pageNumber=1&pageSize=999999'
        # TODO refine the payload
        payload = {"columns":[{"name":"tiLocationCode","sortOrder":"1","sortType":"asc"}]}
        locations = self.user.http.request('POST', url, json=payload).json()['locations']
        for location in locations:
            r_location = LocationConterver.to_resource(location)
            if r_location.code == code:
                return r_location
