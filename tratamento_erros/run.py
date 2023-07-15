try:
    print(ola)
    num1 = 3
    num2 = 0

    response = num1/num2

    print(response)
except NameError:
		print('Esse valor não existe')
except ZeroDivisionError:
    print('Erro de divisao de zero')
except Exception as exception:
    print(exception)
finally:
    #independente caso dê certo ou errado vem para cá
    print('Venha para cá independemente')

print(ola)