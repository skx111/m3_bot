import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_table(self):
        if self.connection:
            print('Database connected successfully')

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)

    def sql_telegram_users(self, telegram_id, username, first_name, last_name):
        if self.connection:
            print('Database connected successfully')

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)


    def sql_insert_users(self,telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name)
        )
        self.connection.commit()



        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)