import pytest
from apiobject.user.user import Administrator

from .utils import certificate

class TestUserLogin:

    def test_administrator(self, host):
        admin = Administrator(*certificate())
        admin.login()
