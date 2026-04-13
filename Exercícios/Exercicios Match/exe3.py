tipo = input("Tipo (compra/venda): ")
valor = float(input("Valor: "))

match tipo:
    case "compra":
        print(f"Compra de {valor}€")
    case "venda":
        print(f"Venda de {valor}€")
    case _:
        print("Pedido desconhecido")