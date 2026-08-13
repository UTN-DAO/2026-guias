from math import sqrt


def recorrer_mostrar(v, funcion):
    for x in v:
        print(funcion(x))
              
              
def map(v, funcion):
    resultados = []
    for x in v:
        resultados.append(funcion(x))
    return resultados
              
              
              
numeros = [3,8,4,122]
print(map(numeros, lambda x: x ** 2))







