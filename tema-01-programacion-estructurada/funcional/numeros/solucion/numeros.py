import random
from functools import reduce
import math

es_par = lambda x: x % 2 == 0
es_impar = lambda x: not es_par(x)
promedio = lambda lista: sum(lista) / len(lista) if len(lista) > 0 else 0
cuadrado = lambda x: x*x
numeros = [random.randint(-1000000,1000000) for _ in range(1000)]

menor = reduce(lambda x, y: x if x < y else y, numeros)
print("Menor de todos:", menor)

pares = list(filter(es_par, numeros))
cantidad_pares = len(pares)
print("Cantidad de pares:", cantidad_pares)

impares = list(filter(es_impar, numeros))
promedio_impares = promedio(impares)
print("Promedio de los impares:", promedio_impares)

cuadrados_10_100 = list(map(cuadrado, filter(lambda x: 10 < x < 100, numeros)))
print("Cuadrados de los que estan entre 10 y 100:", cuadrados_10_100)

multiplos_3 = list(filter(lambda x: x % 3 == 0, cuadrados_10_100))
print("Múltiplos de 3 de la lista anterior:", multiplos_3)

multiplos_7 = sorted(filter(lambda x: x % 7 == 0, numeros), reverse=True)
print("Múltiplos de 7 ordenados:", multiplos_7)

promedio_impares_negativos = promedio(list(filter(lambda x: x < 0, impares)))
print("Promedio de los impares negativos:", promedio_impares_negativos)

promedio_todos = promedio(numeros)
desviacion = math.sqrt(sum(list(map(lambda x: (x - promedio_todos)**2, numeros)))
                           /(len(numeros)-1))
print("Desviación estándar:", desviacion)

multiplos_127 = list(filter(lambda x: x % 14543527 == 0, numeros))
# La lista vacía se convierte en falso
hay_multiplo_127 = bool(multiplos_127) 
# Mas legible: 
# hay_multiplo_127 = len(multiplos_127) > 0
print("Hay multiplos de 127:", "Si" if hay_multiplo_127 else "No")

terminan_23 = list(filter(lambda x: str(x)[-1] in "23", numeros))
print("Todos los que terminan en 2 o 3", terminan_23)



























