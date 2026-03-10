status_input = input("Digite o status do servidor (ok ou erro): ")
tempo_input = int(input("Digite o tempo de resposta em milissegundos "))

servidor = {
    "status": status_input,
    "tempo_resposta": tempo_input
}

status = servidor["status"]
tempo = servidor["tempo_resposta"]

if status == "ok" and tempo > 200:
    print("Servidor lento")
elif status == "ok":
    print("Servidor ativo")
elif status == "erro":
    print("Servidor indisponível")
else:
    print("Estado desconhecido")