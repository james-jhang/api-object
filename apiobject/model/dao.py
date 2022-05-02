from apiobject.dao import DAO
from apiobject.user import User

from .converter import ModelConterver


class ModelDAO(DAO):
    def __init__(self, user: User) -> None:
        super().__init__(user)

    def get(self, name):
        # url = '/models/modelList?pageNumber=1&pageSize=100'
        url = '/models/modelList?pageNumber=1&pageSize=999999'
        # TODO refine the payload
        payload = {"columns":[{"name":"cmbModel","sortOrder":"1","sortType":"asc"}]}
        models = self.user.http.request('POST', url, prefix='/dcTrackApp/api/v1', json=payload).json()['models']
        for model in models:
            r_model = ModelConterver.to_resource(model)
            if r_model.name == name:
                return r_model
