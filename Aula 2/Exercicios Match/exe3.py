tipo = input("Tipo (compra/venda): ")
valor = float(input("Valor: "))

if tipo == "compra":
    print(f"Compra de {valor}€")
elif tipo == "venda":
    print(f"Venda de {valor}€")
else:
    print("Pedido desconhecido")