import requests
from src.main.comm.key_property import CommProperty


class LawDongApi:
    def __init__(self):
        self.base_url = 'https://api.odcloud.kr/api/15063424/v1/uddi:257e1510-0eeb-44de-8883-8295c94dadf7'
        self.service_key = CommProperty().get_datago_servicekey()

    def get_dong(self, page_no, per_page):
        response = requests.get(
            self.base_url,
            params={
                'serviceKey': self.service_key,
                'pageNo': page_no,
                'perPage': per_page
            }
        )

        print(response.text)