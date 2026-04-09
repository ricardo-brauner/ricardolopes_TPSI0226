# Função é um bloco de codigo que pode ser chamado repetidamente evitandpo a repetição de código. As funções podem receber parâmetros e retornar valores.
# dado partencer a um codigo pequeno, as funções ajudam a organizar o código e a torná-lo mais legível.
# Em segurança no scope, quando bem aplicadas em uma função
# Scopes e manipulação, são feitos atraves de passagens de valores e parametros e passagem das referencias das variaveis, e a manipulação

nomes=["da","fa","oi","da"]
#index   0    1    2   3
 
 
def insert(nomesi:list):
    nomesi.append(input("insert um nome"))
 
def listar(nomesl:list):
    for nome in nomesl:
        print("nome : " , nome)
 
def delete(nomesd:list):
    nomesd.pop( int(input(" insert posiçao ")))
 
def procurar(nomesp:list):
    nome=input("insert nome de procura")
    for i in range(len(nomesp)):
        if nomesp[i] == nome:
            print("nome: ",nomesp[i] ," na posiçao ", i)
   
 
while True:
    print ("1 - inserir nome")
    print ("2 - listar nomes")
    print ("3 - delete nome")
    print ("4 - procurar nome")
    print ("5 - sair")
    opt=input("Escolha Opção")
    match opt :
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
        case "3":
            delete(nomes)
        case "4":
            procurar(nomes)
            #print aqui os valores e posiçoes
        case "5":
            print("fim do programa")
            break
        case _:
            print("nao escolheu a opçao certa")