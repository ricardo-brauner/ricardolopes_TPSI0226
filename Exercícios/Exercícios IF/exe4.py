saldo = float(input("Digite o seu saldo inicial: "))
cheque = float(input("Digite o valor do cheque: "))

if cheque > saldo:
    print("Saldo insuficiente, o valor do cheque não foi descontado.")
else:
    saldo -= cheque
    print(f"O cheque foi descontado e o seu novo saldo é: {saldo:.2f} euros.")
