# from DataAccessLayer.LiteDatabase import LiteDatabase
# from DataAccessLayer.Repositories.UserRepository import UserRepository
# from DataAccessLayer.Models.User import User
# from DataAccessLayer.UUidGenerator import UuidGenerator
# user_uuid = UuidGenerator
# db = LiteDatabase()
# db.create_tables()
# user_repository = UserRepository(db.session)
# # user_repository.add_user(user_uuid.generate(), 'sonia', 'mishak', 'maxmishak', 'passwordmaxmishak')
#
#
# def get_user(login):
#     user = db.session.query(User).filter_by(login=login).first()
#     print(user.password)
#
#
# get_user('s')
# db.close_session()
import urllib

from ConfigParser import ConfigReader
import pyodbc as odbc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user_name = "mishak_admin"
password = "makasin461!"

connection_string = ("Driver={ODBC Driver 18 for SQL Server};"
                     "Server=tcp:sql-db-setver.database.windows.net,1433;"
                     "Database=sql_db;"
                     "Uid=mishak_admin;"
                     "Pwd="+password+";"
                     "Encrypt=yes;"
                     "TrustServerCertificate=no;"
                     "Connection Timeout=30;")

connection = odbc.connect(connection_string)
cursor_object = connection.cursor()

b_password = b'$2b$12$WsJ1SONgUkw2aH0.M4XdceQseq6na/b3ccjLTwRMANZcXcnSdXCkO'

sql_query = """
insert into users(ID, name, surename, login, password)
values('3133516c-1fe9-411c-b7ce-29186440d817', 'das', 'da', 'dsa', ?)
"""

cursor_object.execute(sql_query, b_password)
cursor_object.commit()
cursor_object.close()
