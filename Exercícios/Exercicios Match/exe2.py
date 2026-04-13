nota = int(input("Digite a nota entre 0 e 100: "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Bom")
    case n if n >= 50:
        print("Suficiente")
    case _:
        print("Insuficiente")