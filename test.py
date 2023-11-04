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

import pyodbc as odbc

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

sql_query = """
insert into users(ID, name, surename, login, password)
values ('1', 'max', 'mishak', 'login', 'password')
"""

cursor_object.execute(sql_query)
cursor_object.commit()
cursor_object.close()
