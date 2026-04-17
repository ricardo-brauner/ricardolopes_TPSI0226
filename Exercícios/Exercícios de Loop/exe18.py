"""Exercícios 18: Elabore um programa que leia uma entrada e diga quantos números
perfeitos existem. Exemplo de numero perfeito em que somando todos os divisores ele
da o numero inicial. 6=3+2+1 ."""

numero = int(input("Digite um número: "))
perfeitos = 0

for i in range(1, numero + 1):
    soma = sum(j for j in range(1, i) if i % j == 0)

    if soma == i:
        perfeitos += 1
        print(f"{i} é perfeito!")

print(f"\nTotal: {perfeitos}")
