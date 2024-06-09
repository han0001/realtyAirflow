import time

import pytest
from client.src.datago.mois.mois_client import MoisClient
import pandas as pd

@pytest.fixture
def mois_client():
    return MoisClient()


def test_legal_district(mois_client):
    page_no = 1
    num_of_rows = 1000

    for item in mois_client.get_legal_district(page_no, num_of_rows):
        print(item)

def test_get_si_do(mois_client):
    si_do_list = []
    si_gun_gu_list = []
    eup_myeon_dong_list = []

    page_no = 1
    num_of_rows = 1000

    while(True):
        items = mois_client.get_legal_district(page_no, num_of_rows)
        time.sleep(1)

        for item in items:
            if item.si_gun_gu_code == "000":
                si_do_list.append(item)
            if item.si_gun_gu_code != "000" and item.eup_myeon_dong_code == "000":
                si_gun_gu_list.append(item)
            if item.si_gun_gu_code != "000" and item.eup_myeon_dong_code != "000" and item.ri_code == "00":
                eup_myeon_dong_list.append(item)

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

    # print("")
    # print("##시도##")
    # for si_do in si_do_list:
    #     print(si_do.locat_address_name)
    # print("##시군구##")
    # for si_gun_gu in si_gun_gu_list:
    #     print(si_gun_gu.locat_address_name)
    # print("##읍면동##")
    # for eup_myeon_dong in eup_myeon_dong_list:
    #     print(eup_myeon_dong.locat_address_name)
