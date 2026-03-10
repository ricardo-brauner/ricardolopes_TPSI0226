notas = []

for i in range(1, 11):
    notas.append(float(input(f"Nota do aluno {i}: ")))

media = sum(notas) / 10
acima = 0

for nota in notas:
    if nota >= media:
        acima += 1

print(f"\nMédia: {media:.1f}")
print(f"Alunos acima ou na média: {acima}")