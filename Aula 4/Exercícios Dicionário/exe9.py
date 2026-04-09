def calcular_medias():
    notas = {'André': [5, 7, 6],
             'Carla': [9, 7, 8],
             'Bruno': [6, 8, 7],
             }
    
    for nome, lista_notas in notas.items():
        media = sum(lista_notas) / len(lista_notas)
        print(f"A média de {nome} é: {media:.2f}")

calcular_medias()