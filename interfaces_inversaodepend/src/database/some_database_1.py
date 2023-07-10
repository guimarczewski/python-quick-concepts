from src.interfaces import database

class Database1(database):

    def insert(self):
        print('Inserting something')

    def select(self):
        print('Selecting something')