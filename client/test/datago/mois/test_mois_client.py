import time

import pytest
from client.src.datago.mois.mois_client import MoisClient
import pandas as pd

from domain.src.configuration.session_factory import SessionFactory
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


def test_get_sido(mois_client):
    si_do_list = []

    page_no = 1
    num_of_rows = 1000

    # while True:
    items = mois_client.get_legal_district(page_no, num_of_rows)
    time.sleep(0.5)

    for item in items:
        if item.si_gun_gu_code == "000":
            si_do_list.append(item)

    # if len(items) != num_of_rows:
    #     break

    page_no = page_no + 1


    for si_do in si_do_list:
        aa = LegalRegionSido(
            sido_code=si_do.si_do_code,
            sido_name=si_do.locat_low_name,
            legal_region_code=si_do.legal_district_code,
            address_name=si_do.locat_address_name
        )

        print(aa)

    ssesion = SessionFactory.instance().get_session()
    ssesion.add(aa)