from apiobject.dao import DAO
from apiobject.user import User

from .converter import PartClassConverter
from .part_class import PartClass


class PartClassDAO(DAO):
    def __init__(self, user: User) -> None:
        super().__init__(user)


    def create(self, class_label, assignment_level, classes) -> PartClass:
        payload = {
            "label": class_label,
            "assignableTo": assignment_level.pair(),
            "classesForAssociation": [cls.pair() for cls in classes]
        }
        resp = self.user.http.request('POST', '/parts/classes', json=payload).json()
        return PartClassConverter.to_resource(resp)
        # self.id = resp['id']
        # self.label = resp['label']
        # self.assignableTo = resp['assignableTo']
        # self.classesForAssociation = resp['classesForAssociation']

    def delete(self, part_class: PartClass):
        payload = [{'id': part_class.id}]
        resp = self.user.http.request('PUT', '/parts/classes/bulk/delete', json=payload).json()

    def get(self, name):
        url = '/parts/classes'
        part_classes = self.user.http.request('GET', url).json()
        for part_class in part_classes:
            r_part_class = PartClassConverter.to_resource(part_class)
            if r_part_class.class_label == name:
                return r_part_class
