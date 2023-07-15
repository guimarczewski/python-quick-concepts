from collections import namedtuple

MyList = namedtuple("Compra", "frutas local supermercados extras")

def minha_lista():

    return MyList(
        frutas= ["maça","uva", "abacate"],
        local= "rua das laranjeiras",
        supermercados= 2,
        extras= {"doces": "chocolates", "sucos": "morango"}
    )

def minha_lista2():

    return MyList(
        frutas= ["pera","banana"],
        local= "rua das figueiras",
        supermercados= 7,
        extras= {"doces": "paçoca", "sucos": "uva"}
    )

lista = minha_lista()
print(lista)
lista2 = minha_lista2()
print(lista2)