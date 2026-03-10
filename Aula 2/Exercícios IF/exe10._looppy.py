pares = 0
impares = 0

for i in range(1, 11):
    numero = int(input(f"Número {i}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nPares: {pares}")
print(f"Ímpares: {impares}")