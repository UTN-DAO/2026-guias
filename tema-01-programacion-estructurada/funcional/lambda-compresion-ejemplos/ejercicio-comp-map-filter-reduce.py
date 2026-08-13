import rich
import random
from functools import reduce

def run():
    '''
    CONSIDERANDO la lista definida a continuación, 
    realizar las operaciones indicadas
    '''
    lst = [
        "Aruba","Jamaica","Bermuda",
        "Bahama","Key Largo","Montigo"
        ]

    '''
    Obtener POR COMPRENSION una lista con las letras inciales de cada palabra.
    '''
    iniciales = [p[0] for p in lst]
    rich.print (iniciales)
    '''
    Obtener POR COMPRENSION una lista con las longitudes de cada palabra.
    '''
    longitudes = [len(p) for p in lst]
    rich.print (longitudes)

    '''
    Utilizando REDUCE obtener un valor total de la cantidad de letras de
    las palabras que están en la lista original.
    '''
    total_caracteres = reduce(lambda x,y : x+y, longitudes)
    rich.print (total_caracteres)

    '''
    Dada la siguiente lista con 50 NUMEROS ENTEROS ALEATORIOS
    realizar las operaciones indicadas
    '''
    numeros = [random.randrange(1,100) for i in range (50)]
    print (numeros)

    '''
    Utilizando FILTER obtener una lista nueva con los numeros mayores a 50
    y otra lista con los numeros menores o iguales a 50
    '''
    mayores = list(filter(lambda x:x>50, numeros))
    menores = list(filter(lambda x:x<=50, numeros))
    print ('Mayores:',mayores)
    print ('Menores:',menores)

    '''
    Utilizando MAP obtener una lista donde los números impares estén con signo
    negativo mientras que los pares conserven su caracter positivo
    '''
    mixed = list(map(lambda x:x*-1 if x%2 != 0 else x, numeros))
    print (mixed)

    '''
    Utilizando REDUCE obtener dos valores, uno sumando los valores de la lista original
    y otro sumando los valores de la lista cuyos impares cambiaron de signo.
    '''
    suma1 = reduce (lambda x,y : x+y, numeros)
    suma2 = reduce (lambda x,y : x+y, mixed)
    rich.print (suma1)
    rich.print (suma2)

if __name__ == "__main__":
    run()