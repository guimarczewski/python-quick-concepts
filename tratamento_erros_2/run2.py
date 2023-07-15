class HTTPError404(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = 'Esse é meu erro'
        self.status_code = 404

try:
    raise MeuErroPersonalizado('Personalizei um erro')
except Exception as exception:
    print(exception)
    print(exception.error_type)