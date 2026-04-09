alunos = []

def inserir_alunos ():
    nome  = input("Nome:")
    idade = int(input("Idade:"))
    curso = input("Curso:")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)
    print("Aluno inserido com sucesso!")

def listar_alunos():
    if not alunos:
        print("Esse aluno não está registrado.")
        return

    for aluno in alunos:
        print(f"  Nome: {aluno['nome']}")
        print(f"  Idade: {aluno['idade']}")
        print(f"  Curso: {aluno['curso']}")
        print()


while True:
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Sair do programa")

    opcao = input("Escolha uma opção: ")
    print()

    if opcao == "1":
        inserir_alunos()
    elif opcao == "2":
        listar_alunos() 
    elif opcao == "3":
        print("Fim do programa, obrigado!")
        break
    else:
        print("Opção inválida, tente novamente.")    
    

    