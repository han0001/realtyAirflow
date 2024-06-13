import configparser


class CommProperty:

    def __init__(self):
        self.properties = configparser.ConfigParser()
        self.properties.read('D:/my_workspace/python/config.ini')

    def get_datago_servicekey(self):
        return self.properties.get('DATAGO', 'SERVICE_KEY')

    def get_kakao_rest_api_key(self):
        return self.properties.get('KAKAO', 'REST_API_KEY')

    def get_naver_client_id(self):
        return self.properties.get('NAVER', 'CLIENT_ID')

    def get_naver_client_secret(self):
        return self.properties.get('NAVER', 'CLIENT_SECRET')