'''Exercício 4: Verificar se uma chave existe
Dado o dicionário:
utilizador = {'nome': 'Carlos', 'idade': 28}
Escreve um código que verifique se a chave email está presente no dicionário e
imprima uma mensagem adequada, por exemplo: "Email não encontrado."'''

utilizador = {"Nome": "Ricardo", "Idade": 42}


def verificar_email():
    print(f"Nome do utilizador: {utilizador['Nome']}")
    print(f"Idade do utilizador: {utilizador['Idade']}")

    if "email" in utilizador:
        print(f"E-mail do utilizador: {utilizador['email']}")
    else:
        print("O email do utilizador não foi encontrado.")


verificar_email()
