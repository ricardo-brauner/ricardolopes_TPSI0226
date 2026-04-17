def ordenar_lista(caracteres):
    troca = True
    while troca:
        troca = False
        for i in range(len(caracteres) - 1):
            if ord(caracteres[i]) > ord(caracteres[i + 1]):
                caracteres[i], caracteres[i + 1] = caracteres[i + 1], caracteres[i]
                troca = True
    return caracteres


def ordenar_caracteres(palavra):
    caracteres = list(palavra)
    caracteres = ordenar_lista(caracteres)
    return "".join(caracteres)


print(ordenar_caracteres("algoritmo"))  