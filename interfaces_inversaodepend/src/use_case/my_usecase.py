class MyUsecase:

    def __init__(self, database):
        self.database = database

    def search_something(self):
        # Processamento
        self.database.select()

    def insert_something(self):
        # Processamento
        self.database.insert()