import time

import pytest
from client.src.datago.mois.mois_client import MoisClient
import pandas as pd

from domain.src.configuration.session_factory import SessionFactory
from domain.src.module.region.model.legal_region_emd import LegalRegionEmd
from domain.src.module.region.model.legal_region_ri import LegalRegionRi
from domain.src.module.region.model.legal_region_sgg import LegalRegionSgg
from domain.src.module.region.model.legal_region_sido import LegalRegionSido


@pytest.fixture
def mois_client():
    return MoisClient()


def test_legal_district(mois_client):
    page_no = 1
    num_of_rows = 1000

    for item in mois_client.get_legal_district(page_no, num_of_rows):
        print(item)


def test_region_response_to_csv(mois_client):
    si_do_list = []
    si_gun_gu_list = []
    eup_myeon_dong_list = []
    ri_list = []

    page_no = 1
    num_of_rows = 1000

    while(True):
        items = mois_client.get_legal_district(page_no, num_of_rows)
        time.sleep(0.5)

        for item in items:
            if item.si_gun_gu_code == "000":
                si_do_list.append(item)
            if item.si_gun_gu_code != "000" and item.eup_myeon_dong_code == "000":
                si_gun_gu_list.append(item)
            if item.si_gun_gu_code != "000" and item.eup_myeon_dong_code != "000" and item.ri_code == "00":
                eup_myeon_dong_list.append(item)
            if item.si_gun_gu_code != "000" and item.eup_myeon_dong_code != "000" and item.ri_code != "00":
                ri_list.append(item)

        if len(items) != num_of_rows:
            break

        page_no = page_no + 1

    data_dicts = [response.dict(by_alias=True) for response in si_do_list]
    df = pd.DataFrame(data_dicts)
    df.to_csv("si_do_list.csv", index=False, encoding='utf-8-sig')

    data_dicts = [response.dict(by_alias=True) for response in si_gun_gu_list]
    df = pd.DataFrame(data_dicts)
    df.to_csv("si_gun_gu_list.csv", index=False, encoding='utf-8-sig')

    data_dicts = [response.dict(by_alias=True) for response in eup_myeon_dong_list]
    df = pd.DataFrame(data_dicts)
    df.to_csv("eup_myeon_dong_list.csv", index=False, encoding='utf-8-sig')

    data_dicts = [response.dict(by_alias=True) for response in ri_list]
    df = pd.DataFrame(data_dicts)
    df.to_csv("ri_list.csv", index=False, encoding='utf-8-sig')


def test_save_sido(mois_client):
    si_do_list = []

    page_no = 1
    num_of_rows = 1000

    while True:
        items = mois_client.get_legal_district(page_no, num_of_rows)
        time.sleep(0.5)

        for item in items:
            if item.si_gun_gu_code == "000":
                si_do_list.append(item)

        if len(items) != num_of_rows:
            break

        page_no = page_no + 1

    session = SessionFactory.instance().get_session()
    for si_do in si_do_list:
        sido_entity = LegalRegionSido(
            sido_code=si_do.si_do_code,
            sido_name=si_do.locat_low_name,
            legal_region_code=si_do.legal_district_code,
            address_name=si_do.locat_address_name
        )
        session.add(sido_entity)
        session.commit()



def test_save_sgg(mois_client):
    si_gun_gu_list = []

    page_no = 1
    num_of_rows = 1000

    while True:
        items = mois_client.get_legal_district(page_no, num_of_rows)
        time.sleep(0.5)

        for item in items:
            if item.si_gun_gu_code != "000" and item.eup_myeon_dong_code == "000":
                si_gun_gu_list.append(item)

        if len(items) < num_of_rows:
            break

        page_no = page_no + 1

    session = SessionFactory.instance().get_session()
    for si_gun_gu in si_gun_gu_list:

        sido_entity = session.query(LegalRegionSido).filter(LegalRegionSido.sido_code == si_gun_gu.si_do_code).first()
        if sido_entity is None:
            raise Exception(f'sido entity id null - si_gun_gu : {si_gun_gu}')

        sgg_entity = LegalRegionSgg(
            sido_id=sido_entity.id,
            sgg_code=si_gun_gu.si_gun_gu_code,
            sgg_name=si_gun_gu.locat_low_name,
            legal_region_code=si_gun_gu.legal_district_code,
            address_name=si_gun_gu.locat_address_name
        )
        session.add(sgg_entity)
        session.commit()


def test_save_emd(mois_client):
    eup_myeon_dong_list = []

    page_no = 1
    num_of_rows = 1000

    while True:
        items = mois_client.get_legal_district(page_no, num_of_rows)
        time.sleep(0.5)

        for item in items:
            if item.si_gun_gu_code != "000" and item.eup_myeon_dong_code != "000" and item.ri_code == "00":
                eup_myeon_dong_list.append(item)

        if len(items) < num_of_rows:
            break

        page_no = page_no + 1

    session = SessionFactory.instance().get_session()
    for eup_myeon_dong in eup_myeon_dong_list:

        sgg_entity = session.query(LegalRegionSgg).filter(LegalRegionSgg.sgg_code == eup_myeon_dong.si_gun_gu_code).first()
        if sgg_entity is None:
            raise Exception(f'sgg_entity id null - eup_myeon_dong : {eup_myeon_dong}')

        eup_myeon_dong_entity = LegalRegionEmd(
            sgg_id=sgg_entity.id,
            emd_code=eup_myeon_dong.eup_myeon_dong_code,
            emd_name=eup_myeon_dong.locat_low_name,
            legal_region_code=eup_myeon_dong.legal_district_code,
            address_name=eup_myeon_dong.locat_address_name
        )
        session.add(eup_myeon_dong_entity)
        session.commit()




def test_save_ri(mois_client):
    ri_list = []

    page_no = 1
    num_of_rows = 1000

    while True:
        items = mois_client.get_legal_district(page_no, num_of_rows)
        time.sleep(0.5)

        for item in items:
            if item.si_gun_gu_code != "000" and item.eup_myeon_dong_code != "000" and item.ri_code != "00":
                ri_list.append(item)

        if len(items) < num_of_rows:
            break

        page_no = page_no + 1

    session = SessionFactory.instance().get_session()
    for ri in ri_list:

        emd_entity = session.query(LegalRegionEmd).filter(LegalRegionEmd.emd_code == ri.eup_myeon_dong_code).first()
        if emd_entity is None:
            raise Exception(f'sgg_entity id null - ri : {ri}')

        ri_entity = LegalRegionRi(
            emd_id=emd_entity.id,
            ri_code=ri.ri_code,
            ri_name=ri.locat_low_name,
            legal_region_code=ri.legal_district_code,
            address_name=ri.locat_address_name
        )
        session.add(ri_entity)
        session.commit()