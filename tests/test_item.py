# import pytest

# from apiobject.lookup.modelFields import *
# from apiobject.lookup.fields import *
# from apiobject.item.item import *
# from apiobject.user.user import Administrator

# @pytest.fixture
# def admin():
#     host = '192.168.1.18'
#     admin = Administrator(host, 'admin', 'Lab1321*')
#     admin.login()
#     yield admin

# class TestItem:

#     def test_item(self, admin):
#         item = Item(user=admin)
#         item.create(itemname='Test Item', make=Make._3COM, model=Model.BLADE_3C13804, status=ItemStatus.PLANNED, location=Location.SITE_A)
        
        # # teardown
        # part_class.delete()
        # parts_management.disable_parts_management()