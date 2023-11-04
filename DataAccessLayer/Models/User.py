from sqlalchemy import Column, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User data model"""
    __tablename__ = 'users'
    id = Column(String(), Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    surename = Column(String(50))
    login = Column(String(50))
    password = Column(String(50))

    def __init__(self, id, name, surename, login, password):
        self.id = id
        self.name = name
        self.surename = surename
        self.login = login
        self.password = password

    def __repr__(self):
        return f"{self.id}/{self.name}/{self.surename}/{self.login}/{self.password}"
