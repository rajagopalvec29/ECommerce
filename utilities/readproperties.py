import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def GetUrl():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def GetUsername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common info','password')
        return password

