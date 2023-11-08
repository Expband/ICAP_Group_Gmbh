from DataAccessLayer.Models.User import User


class AzureRepository:
    def __init__(self, cursor):
        self.cursor = cursor
        self.insert_query = f"""insert into users(ID, name, surename, login, password)
          values(?, ?, ?, ?, ?)
          """
        self.get_query = f"""select * from users where login = ?"""

    def azure_add_user(self, id, name, surename, login, password):
        new_user = User(id=id, name=name, surename=surename, login=login, password=password)
        self.cursor.execute(self.insert_query,
                            new_user.id,
                            new_user.name,
                            new_user.surename,
                            new_user.login,
                            new_user.password)
        self.cursor.commit()

    def azure_get_user(self, login):
        self.cursor.execute(self.get_query, login)
        return self.cursor.fetchall()
