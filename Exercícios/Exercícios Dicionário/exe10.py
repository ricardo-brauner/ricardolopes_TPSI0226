"""Exercício 10: Contar palavras numa frase
Pede ao utilizador para introduzir uma frase.
Cria um dicionário que contenha cada palavra da frase como chave e o número de
vezes que ela aparece como valor.
Exemplo de entrada:
"hoje é um bom dia e hoje o sol está a brilhar"
Resultado esperado:
{'hoje': 2, 'é': 1, 'um': 1, 'bom': 1, 'dia': 1, 'e': 1, 'o': 1, 'sol': 1,
'está': 1, 'a': 1, 'brilhar': 1}"""


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
