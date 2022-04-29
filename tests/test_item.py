import pytest

from apiobject.lookup.modelFields import *
from apiobject.lookup.fields import *
from apiobject.item.item import *
from apiobject.item.dao import ItemDAO

from apiobject.user.user import Administrator

@pytest.fixture
def admin():
    host = '192.168.1.18'
    admin = Administrator(host, 'admin', 'Lab1321*')
    admin.login()
    yield admin

class TestItem:

    def test_create_item(self, admin):
        dao = ItemDAO(user=admin)
        item: Item = dao.create(
            name='Test Item', 
            make=Make._3COM, 
            model=Model.BLADE_3C13804, 
            status=ItemStatus.PLANNED, 
            location=Location.SITE_A
        )
        assert item.name == 'Test Item'
        assert item.make == Make._3COM
        assert item.model == Model.BLADE_3C13804
        assert item.status == ItemStatus.PLANNED
        assert item.location == Location.SITE_A
        # item = Item(user=admin)
        # item.create(item_name='Test Item', make=Make._3COM, model=Model.BLADE_3C13804, status=ItemStatus.PLANNED, location=Location.SITE_A)

        # teardown
        dao.delete(item)
        # item.delete()
