from DataAccessLayer.Models.User import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    def add_user(self, id, name, surename, login, password):
        new_user = User(id=id, name=name, surename=surename, login=login, password=password)
        self.session.add(new_user)
        self.session.commit()
