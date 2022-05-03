from apiobject.resource import Resource


class Part(Resource):
    def __init__(self, id, make, model, part_number, count_in_stock, count_in_use, status, location, threshold) -> None:
        super().__init__(id)
        self.make = make
        self.model = model
        self.part_number = part_number
        self.count_in_stock = count_in_stock
        self.count_in_use = count_in_use
        self.status = status
        self.location = location
        self.threshold = threshold

        self.tracking_type = None

# class Part(Resource):
#     def __init__(self, id, user: User) -> None:
#         super().__init__(id)
#         self.user = user

#     def assign_to_item(self, item:Item, serial_number=None, quantity=1, reason=None, project:ProjectNumber=None, tracking_number=None):
#         payload = {
#             "itemId": item.id,
#             "partId": self.id,
#             "reason": reason,
#             "quantity": quantity,
#             "projectId": project.id if project else None ,
#             "serialNumber": serial_number,
#             "trackingNumber": tracking_number
#         }
#         resp = self.user.http.request('POST', '/parts/assignments/items', json=payload).json()
#         self.partItemAssignmentIds = resp['partItemAssignmentIds']

#     def unassign_from_item(self, item: Item):
#         payload = {
#             "partItemAssignmentIds": self.partItemAssignmentIds,
#             "isDeletePorts": False,
#             "reason": ""
#         }
#         resp = self.user.http.request('POST', '/parts/assignments/items/deletes', json=payload).json()

#     # def get_assign_part_in_item(self, item):
#     #     item_id = self.get_filter_items('tiName', [item])['searchResults']['items'][0]['id']
#     #     payload = {"columns": [{"name": "itemId", "filter": {"eq":  item_id}}],
#     #                "selectedColumns": [{"name": "partItemAssignmentId"}, {"name": "partId"}]}
#     #     url = f'{self.url}/dcTrackApp/api/v2/parts/assignments/items/list?pageNumber=1&pageSize=-1'
#     #     resp = self.request.post(url, json=payload)
#     #     if resp.status_code != 200:
#     #         raise Exception('Get assigning parts item fail: %s' % resp.content.decode('utf-8'))
#     #     return resp.json()['partItemAssignments']

#     # def unassign_all_parts(self, partItemAssignments, part_batch_number):
#     #     def get_batch_number_filter(batch_number):
#     #         filter = {"columns":[{"name":"serialNumber","filter":{"contains":"\""+batch_number+"\""},"displayValue":"\""+batch_number+"\""}],"selectedColumns":[]}
#     #         return filter
#     #     payload = {"partItemAssignmentIds": [partItemAssignment['partItemAssignmentId'] for partItemAssignment in partItemAssignments if partItemAssignment['partId'] == self.search_parts_by_conditions(get_batch_number_filter(part_batch_number))[0]['partId']], "isDeletePorts": False, "reason": ""}
#     #     url = f'{self.url}/dcTrackApp/api/v2/parts/assignments/items/deletes'
#     #     resp = self.request.post(url, json=payload)
#     #     if resp.status_code != 200:
#     #         raise Exception('Unassigning part to item fails: %s' % resp.content.decode('utf-8'))
