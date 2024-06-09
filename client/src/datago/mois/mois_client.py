import requests
from client.src.comm.key_property import CommProperty
from client.src.datago.mois.response.legal_district_response import LegalDistrictResponse

class MoisClient:
    """
    행정안전부 클라이언트 (Ministry of the Interior and Safety : MOIS)
    """
    def __init__(self):
        self.service_key = CommProperty().get_datago_servicekey()

    def get_legal_district(self, page_no, num_of_rows) -> list[LegalDistrictResponse]:
        """
        행정안전부_행정표준코드_법정동코드
        https://www.data.go.kr/data/15077871/openapi.do
        """
        url = 'http://apis.data.go.kr/1741000/StanReginCd/getStanReginCdList'
        params = {
            'serviceKey': self.service_key,
            'pageNo': page_no,
            'numOfRows': num_of_rows,
            'type': 'json'
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException as e:
            raise requests.HTTPError(f"An error occurred while fetching data: {e}")

        return [LegalDistrictResponse(**item) for item in response.json()['StanReginCd'][1]['row']]
