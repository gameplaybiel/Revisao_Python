temperatura = 0
somatorio = 0
quantidade = 0

while temperatura != 999:
    temperatura = float(input("Digite a temperatura ou 999 para sair:"))

    if temperatura != 999:
        somatorio += temperatura
        quantidade += 1

media = somatorio / quantidade
print("A temperatura média:", media)