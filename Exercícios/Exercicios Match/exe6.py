status_input = input("Digite o status do servidor (ok ou erro): ")
tempo_input = int(input("Digite o tempo de resposta em milissegundos: "))

servidor = {"status": status_input, "tempo_resposta": tempo_input}

match servidor:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("Servidor lento")
    case {"status": "ok"}:
        print("Servidor ativo")
    case {"status": "erro"}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")