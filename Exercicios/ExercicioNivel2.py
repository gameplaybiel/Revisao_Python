#Exercício 2 - Calcular a IMC (Variáveis)

print("Bem vindo a Calculadora IMC")

nome = input("Para começar, digite seu nome: ")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura * altura)

print(nome, " o seu IMC é: ", imc)