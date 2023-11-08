import bcrypt
from DataAccessLayer.LiteDatabaseConnector import LiteDatabaseConnector
from DataAccessLayer.AzureDatabaseConnector import AzureDatabaseConnector
from DataAccessLayer.Repositories.SQLiteUserRepository import UserRepository
from DataAccessLayer.Repositories.AzureUserRepository import AzureRepository
from DataAccessLayer.UUidGenerator import UuidGenerator


class UserServise:
    @staticmethod
    def hash_password(password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    @staticmethod
    def check_password(plain_password, hashed_password):
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

    @staticmethod
    def store_data(form_data):
        user_uuid = UuidGenerator
        sqlite_db = LiteDatabaseConnector()
        sqlite_db.create_tables()
        user_repository = UserRepository(sqlite_db.session)
        user_repository.sqlite_add_user(user_uuid.generate(),
                                        form_data['name'],
                                        form_data['surename'],
                                        form_data['login'],
                                        UserServise.hash_password(form_data['password']))
        sqlite_db.close_session()

    @staticmethod
    def store_data_azure(form_data):
        user_uuid = UuidGenerator
        az_db = AzureDatabaseConnector()
        azure = AzureRepository(az_db.return_connector())
        azure.azure_add_user(user_uuid.generate(),
                                        form_data['name'],
                                        form_data['surename'],
                                        form_data['login'],
                                        UserServise.hash_password(form_data['password']))

    @staticmethod
    def get_password_sqlite(login):
        db = LiteDatabaseConnector()
        user_repository = UserRepository(db.session)
        stored_user = user_repository.sqlite_get_user_by_login(login)
        return stored_user.password

    @staticmethod
    def get_password_azure(login):
        az_db = AzureDatabaseConnector()
        azure = AzureRepository(az_db.return_connector())
        return azure.azure_get_user(login)[0][4]

    @staticmethod
    def compare_passwords(stored_password, current_password):
        if UserServise.check_password(stored_password, current_password):
            return True
        else: return False
