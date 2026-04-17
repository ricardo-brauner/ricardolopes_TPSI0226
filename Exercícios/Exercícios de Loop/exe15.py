"""Exercícios 15: Elabore um programa que escreva no ecrã todas as linhas de código ASCII
(0 a 255) e o código correspondente.
Dispor de 20 em 20 com a condição de continuação ou saída do programa."""

i = 0

while i < 256:
    for j in range(20):
        if i < 256:
            print(f"{i} = {chr(i)}", end="   ")
            i = i + 1

    print()
    opcao = input("\nContinuar? (s/n): ")

    if opcao == "n":
        break

print("Programa terminado!")
