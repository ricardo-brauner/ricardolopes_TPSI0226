jogada1 = input("Jogador 1, digite sua jogada:(Pedra papel ou tesoura) ").lower()
jogada2 = input("Jogador 2, digite sua jogada: (Pedra papel ou tesoura) ").lower()

vence = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}

match (jogada1, jogada2):
    case (j1, j2) if j1 not in vence or j2 not in vence:
        print("Jogada inválida")
    case (j1, j2) if j1 == j2:
        print("Empate")
    case (j1, j2) if vence[j1] == j2:
        print("Jogador 1 venceu")
    case _:
        print("Jogador 2 venceu")