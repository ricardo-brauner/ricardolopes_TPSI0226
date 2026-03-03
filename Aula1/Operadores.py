#Operadores Aritimeticos
#som +, sub -, div /, mult *, mode % (resto da div), ** esponetial

''' total=0
num1=0
num2=0

#input value
num1=int(input("Insira num 1"))
num2=int(input("Insira num 2"))

total=num1+num2
print(f"soma : {total}")

     

      # Operadores de decisão

      # == Igualdade, != diferente, > Maior que, < Menor que, 
'''

val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
val3 = int(input("Digite o terceiro valor: "))

if   val1 > val2 and val2 > val3:
    print("O valor l1 é o maior, e o valor l3 é o menor")

elif val2 > val1 and val1 > val3:
    print("O valor l2 é o maior, e o  valor l3 é o menor")

elif val1 > val3 and val3 > val2:
    print("O valor l1 é o maior, e o valor 12 é o menor")

elif val3 > val1 and val1 > val2:
    print("O valor 13 é o maior, e o valor l2 é o menor")

elif val2 > val3 and val3 > val1:
    print("O valor l2 é o maior, e o valor l1 é o menor")

elif val3 > val2 and val2 > val1:
    print("O valor l3 é o maior, e o valor l1 é o menor")
