total_segundos = int(input("Digite a quantidade de segundos: "))

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

resultado = ""

if horas > 0:
    resultado += f"{horas} hora, "

if minutos > 0:
    resultado += f"{minutos} minutos e "

if segundos > 0:
    resultado += f"{segundos} segundos"


print(f"{resultado}")