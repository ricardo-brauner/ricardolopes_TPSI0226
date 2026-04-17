"""Exercício 4: Crie um algoritmo que leia um número inteiro,
e diga se ele é um número primo ou não."""

numero = int(input("Digite um número inteiro: "))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False

if primo:
    print("É primo!")

else:
    print("Não é primo!")
