from functools import reduce
from rich import print

'''
Ejemplos de utilización de las funciones
MAP, FILTER, REDUCE, caso de apliación típico
de funciones lambda
'''

# Vamos a trabajar con una lista inicial con enteros entre 1 y 5
lista = [1, 2, 3, 4, 5]

# MAP aplica una función lambda sobre cada elemento de una lista
# y crea otra lista con los valores obtenidos.
# En este caso vamos a generar una lista con los cuadrados de los
# elementos de la lista original.
cuadrados = list(
    map(
        lambda x : 
            x**2,
        lista)
    )

print ("Lista:",lista)
print ("Cuadrados:",cuadrados)

# Ahora vamos a utilizar una lista con enteros en el rango -10 a 10
lista = list(range(-10, 10))

# FILTER aplica una función lambda que debe entregar una valor True o 
# False. Si la función entrega True, el valor de la lista de origen se
# copia al destino. En caso contrario no se copia.
menor_cero = list(
    filter(
        lambda x: 
        #((x <= 0) and (x%2 == 0)) or (x>0), 
        (x < 0),
        lista)
    )
print("Lista: ",lista)
print("<0:",menor_cero)

# Vamos a trabajar con una lista de valores entre 1 y 5
lista = [1, 2, 3, 4, 5]
#lista = list(range(16))

# Para usar reduce hace falta importar el módulo functools
# REDUCE aplica una funcion lambda que recibe dos valores y 
# realiza alguna operación. La función REDUCE devuelve un
# único valor como resultado (reduce una lista a un valor)
sumatoria = reduce(
    lambda x,y :
    (x+y), 
    #(x+y)/(y+1), 
    lista)
print ("Lista:", lista)
print ("Sumatoria:", sumatoria)
