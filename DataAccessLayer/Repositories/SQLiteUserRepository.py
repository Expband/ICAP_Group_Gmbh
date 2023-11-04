from DataAccessLayer.Models.User import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    def sqlite_add_user(self, id, name, surename, login, password):
        """"""
        new_user = User(id=id, name=name, surename=surename, login=login, password=password)
        self.session.add(new_user)
        self.session.commit()

    def sqlite_get_user_by_login(self, login):
        user = self.session.query(User).filter_by(login=login).first()
        return user
