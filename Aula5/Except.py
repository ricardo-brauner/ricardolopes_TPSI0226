def alfabética_inversa():
    palavras = ["Python", "Java", "C#", "C", "JavaScript"]
    n = len(palavras)

    for i in range(n):
        for j in range(0, n - i - 1):
            if palavras[j] < palavras[j + 1]:
                palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

                