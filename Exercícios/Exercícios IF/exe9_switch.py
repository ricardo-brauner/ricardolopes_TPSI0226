mes = int(input("Digite o número do mês (1-12): "))

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if 1 <= mes <= 12:
    print(meses[mes - 1])
else:
    print("Mês inválido!")