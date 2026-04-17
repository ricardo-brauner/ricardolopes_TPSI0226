"""Exercício 2: Ler 10 números, e determinar se
o número par e número impar."""

for i in range(1, 11):
    numero = int(input(f"Número {i}: "))
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
