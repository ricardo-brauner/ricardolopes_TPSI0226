valor = input("Digite um valor: ")

if valor.startswith("["):
    print("Lista")
elif valor.lstrip("-").isdigit():
    print("Número inteiro")
elif valor.lstrip("-").replace(".", "", 1).isdigit():
    print("Número decimal")
elif valor.isnumeric():
    print("String numérica")
else:
    print("String textual")