"""Exercício 12: Elabore um programa que leia quantos números quer que se efetue a soma,
subtrações, divisões, multiplicações e no fim por meio de um acumulador diga
quantas operações foram efetuadas. Exemplo introduzindo o número 60 o programa
deve apresentar 60 a somar,
dividir multiplicar e subtrair por todos os números menores que ele."""

numero = int(input("Digite um número: "))

soma = 0
subtracao = 0
multiplicacao = 0
divisao = 0
operacoes = 0

for i in range(1, numero):
    soma = soma + i
    subtracao = subtracao - i
    multiplicacao = multiplicacao * i
    divisao = divisao / i
    operacoes = operacoes + 4

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Total de operações efetuadas: {operacoes}")
