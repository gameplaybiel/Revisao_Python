def verificaSeTriangulo(valor1, valor2, valor3):
    if(valor1 + valor2) >= valor3 and (valor2 + valor3) >= valor1 and (valor3 + valor1) >= valor2:
        return 1
    return 0

def defineTipoTriangulo(valor1, valor2, valor3):
    if verificaSeTriangulo(valor1, valor2, valor3) == 1:
        if valor1 == valor2 and valor2 == valor3:
            print("Triângulo equilatero")
        else:
            if valor1 != valor2 and valor1 != valor3:
                print("Triângulo escaleno")
            else:
                print("Triângulo isosceles")
    else:
        print("Não é um triângulo")

lado1 = 10
lado2 = 20
lado3 = 30

defineTipoTriangulo(lado1, lado2, lado3)