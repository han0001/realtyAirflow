import requests
from client.src.comm.key_property import CommProperty


class ApartPublicPriceCient:
    """
    공동주택가격속성조회
    https://www.vworld.kr/dtna/dtna_apiSvcFc_s001.do?apiNum=31
    """
    def __init__(self):
        self.api_key = CommProperty().get_vworld_api_key()

    def get_apart_public_prices_by(self, pnu, stdr_year, num_of_rows, page_no):
        """
        공동주택가격속성조회
        @param pnu:         고유변호(8자리 이상)      필수
        @param stdrYear:    기준연도(YYYY: 4자리)    옵션
        @param numOfRows:   검색건수 (최대 1000)     옵션
        @param pageNo:      페이지 번호              옵션
        """
        try:
            response = requests.get(
                url='https://api.vworld.kr/ned/data/getApartHousingPriceAttr',
                params={
                    'key': self.api_key,
                    'pnu': pnu,
                    'stdrYear': stdr_year,
                    'numOfRows': num_of_rows,
                    'pageNo': page_no,
                    'domain': 'http://www.test.com/'
                }
            )
            response.raise_for_status()
        except requests.RequestException as e:
            raise requests.HTTPError(f"An error occurred while fetching data: {e}")

        return response.json()['addresses']


client = ApartPublicPriceCient()
response = client.get_apart_public_prices_by(2717010400, 2023, 1000, 1)
print(response)