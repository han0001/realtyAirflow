import requests
from client.src.comm.key_property import CommProperty


class KakaoLocalClient:
    """
    카카오 로컬 클라이언트
    로컬 API는 키워드로 특정 장소 정보를 조회하여 좌표 등 메타 정보를 조회 할 수 있음.
    https://developers.kakao.com/docs/latest/ko/local/dev-guide#address-coord
    """
    def __init__(self):
        self.rest_api_key = CommProperty().get_kakao_rest_api_key()

    def get_search_address(self, query):
        """
        주소 검색하기.
        """

        try:
            response = requests.get(
                url='https://dapi.kakao.com/v2/local/search/address',
                headers={'Authorization': 'KakaoAK ' + self.rest_api_key},
                params={'query': query}
            )
            response.raise_for_status()
        except requests.RequestException as e:
            raise requests.HTTPError(f"An error occurred while fetching data: {e}")

        print(response)


