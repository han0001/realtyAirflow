import requests
from client.src.comm.key_property import CommProperty
from client.src.datago.mois.response.legal_district_response import LegalDistrictResponse


class MolitClient:
    """
    국토교통부 클라이언트 (Ministry of Land, Infrastructure and Transport : MOLIT)
    """
    def __init__(self):
        self.service_key = CommProperty().get_datago_servicekey()

    def get_apart_list(self, page_no, num_of_rows, bjdCode):
        """
        국토교통부_공동주택 단지 목록제공 서비스
        https://www.data.go.kr/data/15057332/openapi.do
        """
        url = 'http://apis.data.go.kr/1613000/AptListService2/getLegaldongAptList'
        params = {
            'serviceKey': self.service_key,
            'pageNo': page_no,
            'numOfRows': num_of_rows,
            'bjdCode': bjdCode,
            'type': 'json'
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException as e:
            raise requests.HTTPError(f"An error occurred while fetching data: {e}")

        # return [LegalDistrictResponse(**item) for item in response.json()['StanReginCd'][1]['row']]

    def get_apart_detail(self, kaptCode):
        """
        국토교통부_공동주택 기본 정보제공 서비스
        https://www.data.go.kr/data/15058453/openapi.do
        """

        url = 'http://apis.data.go.kr/1613000/AptBasisInfoService1/getAphusBassInfo'
        params = {
            'serviceKey': self.service_key,
            'kaptCode': kaptCode
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException as e:
            raise requests.HTTPError(f"An error occurred while fetching data: {e}")

        # return [LegalDistrictResponse(**item) for item in response.json()['StanReginCd'][1]['row']]

client = MolitClient()
# client.get_apart_list(1, 10, 1156011400)
client.get_apart_detail('A15004406')