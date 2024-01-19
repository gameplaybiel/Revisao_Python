juros = float(input("Digite os juros:"))
capital = float(input("Digite o caoital:"))
periodo = int(input("Digite o período:"))

for i in range(0, periodo):
    capital = capital + (capital * (juros/100))
    print(capital)