import pytest
from apiobject.user.user import Administrator


@pytest.fixture()
def host():
    yield '192.168.1.18'

class TestUserLogin:

    def test_administrator(self, host):
        admin = Administrator(host, 'admin', 'Lab1321*')
        admin.login()
