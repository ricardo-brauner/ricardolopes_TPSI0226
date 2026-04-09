produto = {}

def gerir_produto():
  
    produto["Nome do equipamento"] = "Notebook"
    produto["Preço"] = 5000
    produto["Stock"] = 50
    produto.pop("Stock")
    
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")

gerir_produto()


