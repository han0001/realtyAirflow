import configparser


class CommProperty:

    def __init__(self):
        self.properties = configparser.ConfigParser()
        self.properties.read('C:/workspace_python/config.ini')

    def get_database_url(self):
        return self.properties.get('DATABASE', 'URL')

    def get_database_user_name(self):
        return self.properties.get('DATABASE', 'USER_NAME')

    def get_database_password(self):
        return self.properties.get('DATABASE', 'PASSWORD')
