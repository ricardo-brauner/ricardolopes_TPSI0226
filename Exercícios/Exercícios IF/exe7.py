nota1 = float(input("Digite a nota 1 (peso 2): "))
nota2 = float(input("Digite a nota 2 (peso 3): "))
nota3 = float(input("Digite a nota 3 (peso 5): "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print(f"\nMédia: {media:.1f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")