import configparser
import os
config = configparser.RawConfigParser()
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini'))
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common', 'baseURL')

    @staticmethod
    def getUsername():
        return config.get('common', 'username')

    @staticmethod
    def getPassword():
        return config.get('common', 'password')
