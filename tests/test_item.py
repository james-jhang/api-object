import pytest

from apiobject.lookup.modelFields import *
from apiobject.lookup.fields import *
from apiobject.item import Item, ItemDAO

from apiobject.user.user import Administrator

from .utils import certificate

@pytest.fixture
def admin():
    admin = Administrator(*certificate())
    admin.login()
    yield admin

class TestItem:

    def test_create_item(self, admin):
        dao = ItemDAO(user=admin)
        item: Item = dao.create(
            name = 'Test Item',
            make = '3Com',
            model = 'Blade 3C13804',
            status = ItemStatus.PLANNED,
            location = 'SITE A'
        )

        assert item.name == 'Test Item'.upper()
        assert item.make == '3Com'
        assert item.model == 'Blade 3C13804'
        assert item.location == 'SITE A'

        # teardown
        dao.delete(item)
