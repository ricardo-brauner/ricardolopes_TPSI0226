categoria = input("Digite a categoria (eletronico/alimento): ")
preco = float(input("Digite o preço: "))

match (categoria, preco):
    case ("eletronico", p) if p > 1000:
        print("Produto de luxo")
    case ("eletronico", _):
        print("Produto comum")
    case ("alimento", _):
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")