
import pytest

from client.src.kakao.local.kakao_local_client import KakaoLocalClient


@pytest.fixture
def kakao_local_client():
    return KakaoLocalClient()

def test_get_search_address(kakao_local_client):
    kakao_local_client.get_search_address('제주특별자치도 서귀포시')
