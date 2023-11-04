from DataAccessLayer.Models.User import User


class AzureRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def azure_add_user(self,  id, name, surename, login, password):
        self.query = f"values ({id}, {name}, {surename}, {login}, {password})"
        self.cursor.execute("""insert into users(ID, name, surename, login, password)
        """) + self.query


azureRepository = AzureRepository

azureRepository.azure_add_user('')
