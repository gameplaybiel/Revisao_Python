# Dado um número inteiro, exiba sua tabuada.

print("Dado um número inteiro, exiba sua tabuada.")
numero = int(input("Digite um número para o cálculo da tabuada:"))

for i in range(1, 11):
    print(i, "x", numero, "=", i*numero)
