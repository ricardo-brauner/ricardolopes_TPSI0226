numero = int(input("Digite um número: "))
perfeitos = 0

for i in range(1, numero + 1):
    soma = sum(j for j in range(1, i) if i % j == 0)
    
    if soma == i:
        perfeitos += 1
        print(f"{i} é perfeito!")

print(f"\nTotal: {perfeitos}")