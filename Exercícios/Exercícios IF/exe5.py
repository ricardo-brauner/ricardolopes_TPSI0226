num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numeros = sorted([num1, num2, num3])

print(f"Crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
print(f"Decrescente: {numeros[2]}, {numeros[1]}, {numeros[0]}")