"""Exercício 14: Altere o programa anterior para que mostre todas
as tabuadas de 1 a 100. (ciclos for)."""

for numero in range(1, 101):
    print(f"\n--- Tabuada do {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
