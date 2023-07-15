class MeuErroPersonalizado(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = 'Esse é meu erro'

try:
    raise MeuErroPersonalizado('Personalizei um erro')
except Exception as exception:
    print(exception)
    print(exception.error_type)