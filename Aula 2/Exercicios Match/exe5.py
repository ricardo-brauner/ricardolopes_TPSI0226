mensagem = input("Digite uma mensagem: ")

if mensagem == "olá" or mensagem == "ola" or mensagem == "bom dia":
    print("Saudação")
elif mensagem.endswith("?"):
    print("Pergunta")
elif "tchau" in mensagem or "adeus" in mensagem:
    print("Despedida")
else:
    print("Mensagem genérica")
