from ..user import User

class ValueID:
    def __init__(self, value: str, id: int) -> None:
        self.value = value
        self.id = id

    def pair(self):
        return {
            'value': self.value,
            'id': self.id
        }

    def __repr__(self) -> str:
        return self.value

class Lookup:
    def __init__(self, user) -> None:
        self.user = user
        self.lookup = self.lookup = user.http.request(
            'GET', '/dcimoperations/lookups/ALL_LKS'
        ).json()['lookup']
    
    def field_detail(self, field) -> None:
        return self.user.http.request(
            'GET', '/dcimoperations/lookups/%s' % field
        ).json()['lookup']
    
    def subtab_detail(self):
        return self.user.http.request(
            'GET', '/settings/lists/subtabs'
        ).json()