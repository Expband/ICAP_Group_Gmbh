from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DataAccessLayer.Models.User import Base
from ConfigParser import ConfigReader


class LiteDatabaseConnector:
    def __init__(self):
        self.conf_reader = ConfigReader()
        self.connection_string = self.conf_reader.get_sqlite_string()
        self.engine = create_engine(self.connection_string, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def close_session(self):
        self.session.close()
