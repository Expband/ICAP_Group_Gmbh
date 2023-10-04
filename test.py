from DataAccessLayer.LiteDatabase import LiteDatabase
from DataAccessLayer.Repositories.UserRepository import UserRepository
from DataAccessLayer.UUidGenerator import UuidGenerator
user_uuid = UuidGenerator
db = LiteDatabase()
db.create_tables()
user_repository = UserRepository(db.session)
user_repository.add_user(user_uuid.generate(), 'sonia', 'mishak', 'maxmishak', 'passwordmaxmishak')
db.close_session()
