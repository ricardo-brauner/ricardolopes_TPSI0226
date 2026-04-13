nomes = ["da","fa","oi","da"]
#index   0    1    2   3

indices = []

def insert(nomesi:list):
    nomesi.append(input("Insira um nome"))

def listar(nomesl:list):
    for nome in nomesl:
        print("nome : " , nome)

def delete(nomesd:list):
    nomesd.pop( int(input(" Insira uma posiçao ")))

def procurar(nomesprocura:list, indices:list):
    indices.clear()
    nome = input("Insira um nome: ")
    for i in range(len(nomesprocura)):
        if nomesprocura[i] == nome:
            indices.append(i)
    return(indices)

while True:
    print ("1 - Inserir nome ")
    print ("2 - Listar nomes ")
    print ("3 - Delete nome ")
    print ("4 - Procurar nome ")
    print ("5 - Sair do programa ")
    opt=input("Escolha uma opção ")
    match opt :
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
        case "3":
            delete(nomes)
        case "4":
            resultado = procurar(nomes, indices)
            print("Posições encontradas:", resultado)
        case "5":
            print("Fim do programa, obrigado")
            break
        case _:
            print("Não escolheu a opção certa")