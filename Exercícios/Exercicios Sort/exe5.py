def ordenar_lista(palavras):
    troca = True
    while troca:
        troca = False
        for i in range(len(palavras) - 1):
            if palavras[i] > palavras[i + 1]:
                palavras[i], palavras[i + 1] = palavras[i + 1], palavras[i]
                troca = True
    return palavras


def agrupar_palavras(lista):
    grupos = {}

    for palavra in lista:
        letra = palavra[0]
        if letra not in grupos:
            grupos[letra] = []
        grupos[letra].append(palavra)

    for letra in grupos:
        grupos[letra] = ordenar_lista(grupos[letra])

    return grupos

palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
resultado = agrupar_palavras(palavras)
print(resultado)