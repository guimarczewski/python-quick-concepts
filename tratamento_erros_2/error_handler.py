from meu_erro import MeuErroPersonalizado

#função para tratar meus erros
def error_handler_method(error):
    if isinstance(error, MeuErroPersonalizado):
        print('Tratar meu erro personalizado')
        return

    if isinstance(error, ZeroDivisionError):
        print('tratar divisao por zero')
        return

    if isinstance(error, Exception):
        print('Tratar caso geral')
        return
