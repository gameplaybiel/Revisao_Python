numeros = list(range(10))

for n in numeros:
    numeros[n] = int(input("Digite um número para: "))

for n in range(0, 10):
    if n % 2 != 0:
        print(numeros[n])
