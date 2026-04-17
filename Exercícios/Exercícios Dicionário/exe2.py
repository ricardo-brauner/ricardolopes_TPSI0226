"""Exercício 2: Aceder a valores no dicionário dado o seguinte dicionário:
carro = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}
Escreve uma linha de código que imprima apenas o modelo do carro."""

carro = {"marca": "Ferrari", "modelo": "Spider", "ano": 2020, "cor": "Vermelha"}


def modelo_carro(carro):
    print(f"O modelo do carro é: {carro['modelo']}")


modelo_carro(carro)
