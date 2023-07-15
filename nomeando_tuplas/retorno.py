def minha_lista():

    return {
        "frutas": ["maça","uva", "abacate"],
        "local": "rua das laranjeiras",
        "supermercado": 2,
        "extras": {"doces": "chocolates", "sucos": "morango"}
    }

lista = minha_lista()
#processamento ...

lista["frutas"] = 'Qualquer coisa'
print(lista)