from abc import ABC, abstractclassmethod

class database(ABC):

    @abstractclassmethod
    def insert():
        raise Exception("Should implement method: insert")
        #define metodos que são abstratos, que falam: sempre que tiver uma classe filha ess método 
        #precisa ser implementado

    @abstractclassmethod
    def select():
        raise Exception("Should implement method: select")
