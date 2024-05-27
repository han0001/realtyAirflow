import pytest
from src.main.client.datago.stand_org import LawDongApi

@pytest.fixture
def stand_org():
    return LawDongApi()


def test_get_dong(stand_org):
    print(stand_org.get_dong(1, 3))


