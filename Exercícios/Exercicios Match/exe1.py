# IF (o teu código)
dia = input("Digite um dia da semana: ")
if dia == "sabado" or dia == "domingo":
    print("Fim de semana")
else:
    print("Dia útil")

# MATCH (convertido)
dia = input("Digite um dia da semana: ").lower()
match dia:
    case "sabado" | "domingo":
        print("Fim de semana")
    case _:
        print("Dia útil")