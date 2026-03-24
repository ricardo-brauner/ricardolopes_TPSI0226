mensagem = input("Digite uma mensagem: ")

match mensagem:
    case "olá" | "ola" | "bom dia":
        print("Saudação")
    case m if m.endswith("?"):
        print("Pergunta")
    case m if "tchau" in m or "adeus" in m:
        print("Despedida")
    case _:
        print("Mensagem genérica")