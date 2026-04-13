def ordenar_inversa():
    palavras = ["Java", "Python", "JavaScript", "C#", "PHP"]
    n = len(palavras)

    for i in range(n):
        for j in range(0, n-i-1):

            if palavras[j].lower() < palavras[j+1].lower():

                aux = palavras[j]
                palavras[j] = palavras[j+1]
                palavras[j+1] = aux

    print("Palavras ordenadas inversamente:", palavras)

   
ordenar_inversa()