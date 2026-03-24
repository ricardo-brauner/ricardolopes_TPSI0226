metodo = input("Digite o método (GET/POST): ")
conteudo = input("Digite o conteúdo: ")

match (metodo, conteudo):
    case ("GET", _):
        print("Requisição GET recebida")
    case ("POST", c) if c:
        print("Requisição POST com dados válidos")
    case ("POST", _):
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")