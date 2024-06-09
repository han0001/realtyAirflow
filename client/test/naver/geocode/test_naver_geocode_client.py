import pytest
from client.src.naver.geocode.naver_geocode_client import NaverGeocodeClient


@pytest.fixture
def naver_geocode_client():
    return NaverGeocodeClient()

def test_get_search_address(naver_geocode_client):
    naver_geocode_client.get_geocode("인천광역시")
