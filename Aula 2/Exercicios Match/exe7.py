categoria = input("Digite a categoria do produto (eletronico/alimento): ")
preco = float(input("Digite o preço do produto: "))

if categoria == "eletronico" and preco > 1000:
    print("Produto de luxo")
elif categoria == "eletronico":
    print("Produto comum")
elif categoria == "alimento":
    print("Produto alimentar")
else:
    print("Categoria desconhecida")