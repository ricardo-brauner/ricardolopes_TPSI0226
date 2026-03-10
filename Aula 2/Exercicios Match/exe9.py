metodo = input("Digite o método (GET/POST): ")
conteudo = input("Digite o conteúdo: ")

if metodo == "GET":
    print("Requisição GET recebida")
elif metodo == "POST":
    print("Requisição POST com dados válidos" if conteudo else "Requisição POST sem dados")
else:
    print("Método não suportado")