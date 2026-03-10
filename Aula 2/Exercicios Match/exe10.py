print("-------------------------------- Pedra, Papel e Tesoura --------------------------------")

jogada1 = input("Jogador 1, digite sua jogada: ").lower()
jogada2 = input("Jogador 2, digite sua jogada: ").lower()

vence = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}

if jogada1 not in vence or jogada2 not in vence:
    print("Jogada inválida")
elif jogada1 == jogada2:
    print("Empate")
elif vence[jogada1] == jogada2:
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")