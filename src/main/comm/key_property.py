import configparser


class CommProperty:

    def __init__(self):
        self.properties = configparser.ConfigParser()
        self.properties.read('D:/my_workspace/python/config.ini')

    def get_datago_servicekey(self):
        return self.properties.get('DATAGO', 'SERVICE_KEY')
