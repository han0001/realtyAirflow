import pytest

from domain.src.comm.key_property import CommProperty


@pytest.fixture
def key_property():
    return CommProperty()


def test_get_datago_servicekey(key_property):
    print(key_property.get_database())
