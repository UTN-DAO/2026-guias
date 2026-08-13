from math import sqrt

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

def mitad(x):
    return x / 2

## operacion es una función
def calcular(valor, operacion):
    return operacion(valor)

print(calcular(9, cuadrado))
print(calcular(9, cubo))
print(calcular(9, mitad))
print(calcular(9, lambda x: x * 2))
print(calcular(9, sqrt))
calcular(9, print)

