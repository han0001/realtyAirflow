import concurrent

import pytest
from geoalchemy2 import Geometry, WKTElement

from client.src.naver.geocode.naver_geocode_client import NaverGeocodeClient
from domain.src.configuration.session_factory import SessionFactory
from domain.src.module.region.model.legal_region_emd import LegalRegionEmd
from domain.src.module.region.model.legal_region_ri import LegalRegionRi
from domain.src.module.region.model.legal_region_sgg import LegalRegionSgg
from domain.src.module.region.model.legal_region_sido import LegalRegionSido


session = SessionFactory.instance().get_session()

@pytest.fixture
def naver_geocode_client():
    return NaverGeocodeClient()


def test_get_search_address(naver_geocode_client):
    addresses = naver_geocode_client.get_geocode("대구광역시 중구 남성로")
    print(addresses)

def test_get_search_address_one(naver_geocode_client):
    address = naver_geocode_client.get_geocode_one("부산광역시 금정구 금사동")
    print(address)

def test_update_one_sido_xy(naver_geocode_client):
    session = SessionFactory.instance().get_session()
    sido_entity = session.query(LegalRegionSido).first()

    search_response = naver_geocode_client.get_geocode_one(sido_entity.address_name)
    sido_entity.center_location = WKTElement(f'POINT({search_response.x} {search_response.y})')
    session.commit()

def test_update_all_sido_one_xy(naver_geocode_client):
    sido_entity_list = session.query(LegalRegionSido).all()

    for sido_entity in sido_entity_list:
        search_response = naver_geocode_client.get_geocode_one(sido_entity.address_name)
        sido_entity.center_location = WKTElement(f'POINT({search_response.x} {search_response.y})')
        session.commit()


def test_update_all_sgg_one_xy(naver_geocode_client):
    sgg_entity_list = session.query(LegalRegionSgg).all()

    for sgg_entity in sgg_entity_list:
        search_response = naver_geocode_client.get_geocode_one(sgg_entity.address_name)
        sgg_entity.center_location = WKTElement(f'POINT({search_response.x} {search_response.y})')
        session.commit()


def test_update_all_emd_one_xy(naver_geocode_client):
    emd_entity_list = session.query(LegalRegionEmd).filter(LegalRegionEmd.center_location == None).all()

    pass_address_list = ['대구광역시 중구 남성로']

    for emd_entity in emd_entity_list:
        if emd_entity.address_name in pass_address_list:
            continue

        search_response = naver_geocode_client.get_geocode_one(emd_entity.address_name)
        emd_entity.center_location = WKTElement(f'POINT({search_response.x} {search_response.y})')
        session.commit()


def test_update_all_emd_one_xy_par(naver_geocode_client):
    emd_entity_list = session.query(LegalRegionEmd).filter(LegalRegionEmd.center_location == None).all()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(update_emd_entity, emd_entity_list)

def update_emd_entity(emd_entity):
    pass_address_list = ['대구광역시 중구 남성로']
    if emd_entity.address_name in pass_address_list:
        pass

    search_response = naver_geocode_client.get_geocode_one(emd_entity.address_name)
    emd_entity.center_location = WKTElement(f'POINT({search_response.x} {search_response.y})')
    session.commit()


def test_update_all_ri_one_xy(naver_geocode_client):
    session = SessionFactory.instance().get_session()
    ri_entity_list = session.query(LegalRegionRi).filter(LegalRegionRi.center_location == None).all()

    for ri_entity in ri_entity_list:
        search_response = naver_geocode_client.get_geocode_one(ri_entity.address_name)
        ri_entity.center_location = WKTElement(f'POINT({search_response.x} {search_response.y})')
        session.commit()
