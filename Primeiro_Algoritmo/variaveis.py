# Variáveis
nome = "João"
peso = 50.5
idade = 30
print("Nome: {} Peso: {} kg Idade: {} anos".format(nome, peso, idade))

idade = 10
idade = 30 + idade
print(idade)

x = 10
y = 30

soma = x + y

print(f"{x} + {y} = {soma}")
print("Soma: {}".format(soma))

subtracao = x - y
print("Subtração: {}".format(subtracao))

multiplicacao = x * y
print("Multiplicação: {}".format(multiplicacao))

divisao = x / y
print("Divisão: {}".format(divisao))

potencia =  x**2
print("Potência: {}".format(potencia))
potencia =  y**2
print("Potência: {}".format(potencia))

nome = input("Digite seu nome: ")
idade = input("Olá {}, digite sua idade: ".format(nome))

#print("Nome: {}".format(nome))
#print("Idade: {}".format(idade))


print("Nome: {}, Idade: {}".format(nome, idade), "anos")