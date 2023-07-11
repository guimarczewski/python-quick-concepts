from typing import Type
from src.interfaces import database

class MyUsecase:

    def __init__(self, database: Type[database]):
    # nesse caso estamos informando que podemos colocar qualquer tipo de database, desde
    # que esteja de acordo com a nossa interface databse    
        self.database = database

    def search_something(self):
        # Processamento
        self.database.select()

    def insert_something(self):
        # Processamento
        self.database.insert()