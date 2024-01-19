# Comandos condicionais (if e else)

#Faça um algoritmo que escreva um número entre 100 e 200

numero = int(input("Digite o seu número:"))

if numero >= 100:
    if numero <= 200:
        print("O valor está no intervalo")
    else:
        print("O valor não está no intervalo, dentro do 100 e 200")
else:
    print("O valor não está no intervalo, menor que 200")