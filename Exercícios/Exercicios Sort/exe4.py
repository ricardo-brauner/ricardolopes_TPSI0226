def ordenarminusculas():

    palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
    
    flags = True
    while flags:
        flags = False
        for i in range(len(palavras) - 1):         
            
            conta_atual = 0
            for letra in palavras[i]:
                if letra.islower():
                    conta_atual += 1                               
            conta_proxima = 0

            for letra in palavras[i+1]:
                if letra.islower():
                    conta_proxima += 1            
            
            if conta_atual > conta_proxima:
                palavras[i], palavras[i+1] = palavras[i+1], palavras[i]
                flags = True
                
    print("Palavras ordenadas por minúsculas:", palavras)

ordenarminusculas()