import requests
from client.src.comm.key_property import CommProperty

class NaverGeocodeClient:
    """
    네이버 GEOCODE
    https://api.ncloud-docs.com/docs/ai-naver-mapsgeocoding-geocode
    """
    def __init__(self):
        self.client_id = CommProperty().get_naver_client_id()
        self.client_secret = CommProperty().get_naver_client_secret()

    def get_geocode(self, query):
        """
        주소 검색
        지번, 도로명를 질의어로 사용해서 주소 정보를 검색합니다. 검색 결과로 주소 목록과 세부 정보를 JSON 형태로 반환합니다.
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

        print(response)