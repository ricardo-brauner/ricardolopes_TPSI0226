vendas = {"Janeiro": 1500.00, "Fevereiro": 2000.00, "Março": 1800.00}

def valores_vendas():
    total= 0

    for mes, valor in vendas.items():
        total += valor        
        print(f"Valor da venda de {mes}: {valor:.2f}")
                
    print(f"\nO total de vendas do trimestre é: {total:.2f}")

valores_vendas()    