import bcrypt
from DataAccessLayer.LiteDatabaseConnector import LiteDatabaseConnector
from DataAccessLayer.AzureDatabaseConnector import AzureDatabaseConnector
from DataAccessLayer.Repositories.SQLiteUserRepository import UserRepository
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
        azure_db = AzureDatabaseConnector


    @staticmethod
    def compare_passwords(user_data):

        db = LiteDatabaseConnector()
        user_repository = UserRepository(db.session)
        current_user = user_repository.sqlite_get_user_by_login(user_data['login'])
        if UserServise.check_password(user_data['password'], current_user.password):
            return True
