from ConfigParser import ConfigReader
import pyodbc as odbc


class AzureDatabaseConnector:
    def __init__(self):
        self.config = ConfigReader()
        self.connection = odbc.connect(self.config.get_azure_string())
        self.cursor = self.connection.cursor()

    def close_session(self):
        self.cursor.close()
