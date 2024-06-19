import requests
from client.src.comm.key_property import CommProperty

class ApartPublicPriceCient:
    """
    공동주택가격속성조회
    https://www.vworld.kr/dtna/dtna_apiSvcFc_s001.do?apiNum=31
    """
    def __init__(self):
        self.api_key = CommProperty().get_vworld_api_key()

    def get_apart_public_prices_by(self, pnu, stdrYear, numOfRows, pageNo):
        """
        공동주택가격속성조회
        @param pnu:
        @param stdrYear:
        @param pnu:
        @param pnu:
        """
        try:
            response = requests.get(
                url='https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode',
                headers={
                    'X-NCP-APIGW-API-KEY-ID': self.client_id,
                    'X-NCP-APIGW-API-KEY': self.client_secret
                },
                params={
                    'query': query
                }
            )
            response.raise_for_status()
        except requests.RequestException as e:
            raise requests.HTTPError(f"An error occurred while fetching data: {e}")

        return response.json()['addresses']