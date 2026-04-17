"""Exercício 8: Juntar dois dicionários
Dado os seguintes dicionários:
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
Cria um novo dicionário que contenha os pares chave-valor dos dois dicionários juntos.
"""


def juntar_dicionarios():

    dicionario1 = {"a": 1, "b": 2}
    dicionario2 = {"c": 3, "d": 4}

    dicionario3 = dicionario1 | dicionario2

    print("Dicionário 1:", dicionario1)
    print("Dicionário 2:", dicionario2)
    print("Dicionário Resultante:", dicionario3)


juntar_dicionarios()
