from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DataAccessLayer.Models.User import Base


class LiteDatabase:
    def __init__(self):
        self.engine = create_engine('sqlite:///ICAD.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def close_session(self):
        self.session.close()
