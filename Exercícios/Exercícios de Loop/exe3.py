soma = 0

for i in range(10):
    nota = float(input("Digite uma nota: "))
    soma = soma + nota

media = soma / 10
print(f"Média: {media:.2f}")