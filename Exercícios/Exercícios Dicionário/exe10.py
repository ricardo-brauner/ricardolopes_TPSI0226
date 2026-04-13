def contador_palavras():

    frase = input("Digite uma frase: ")
    palavras = frase.split()
    contador = {}

    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    print("Contagem de Palavras:", contador)

contador_palavras()