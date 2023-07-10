from src.interfaces import database

class Database2(database):

    def insert_something_into_database(self):
        print('Inserting something')

    def select_something_from_database(self):
        print('Selecting something')