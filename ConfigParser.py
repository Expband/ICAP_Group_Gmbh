import configparser


class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('DataAccessLayer/db_config.ini')
        self.__sql_lite_string = self.config.get('SQLite_connection', 'sqlite_connection_string')
        self.__azure_db = self.config.get('Azure_SQL_connection', 'connection_string')

    def get_sqlite_string(self):
        return self.__sql_lite_string

    def get_azure_string(self):
        return self.__azure_db
