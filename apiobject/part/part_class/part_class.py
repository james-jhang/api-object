from apiobject.resource import Resource


class PartClass(Resource):
    def __init__(self, id, class_label, assignment_level, classes) -> None:
        super().__init__(id)
        self.class_label = class_label
        self.assignment_level = assignment_level
        self.classes = classes

# class PartClass(Resource):
#     def __init__(self, id, user: User) -> None:
#         super().__init__(id)
#         self.user = user
#         self.label = None
#         self.assignableTo = None
#         self.classesForAssociation = None




#     def get(self, class_label):
#         resps = self.user.http.request('GET', '/parts/classes').json()
#         for resp in resps:
#             if resp['label'] == class_label:
#                 self.id = resp['id']
#                 break