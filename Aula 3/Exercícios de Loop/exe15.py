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