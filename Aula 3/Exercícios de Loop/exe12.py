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