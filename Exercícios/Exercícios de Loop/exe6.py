"""Exercício 6: Crie um algoritmo que mostre
os 10 primeiros números primos."""

contador = 0
numero = 2

while contador < 10:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    if primo:
        print(numero)
        contador = contador + 1
    numero = numero + 1
