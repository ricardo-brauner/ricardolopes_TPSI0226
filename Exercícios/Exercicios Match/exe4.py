valor = input("Digite um valor: ")

match valor:
    case v if v.startswith("["):
        print("Lista")
    case v if v.lstrip("-").isdigit():
        print("Número inteiro")
    case v if v.lstrip("-").replace(".", "", 1).isdigit():
        print("Número decimal")
    case v if v.isnumeric():
        print("String numérica")
    case _:
        print("String textual")