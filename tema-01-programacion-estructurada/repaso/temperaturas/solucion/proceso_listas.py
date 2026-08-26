

def cantidad_menor(lista, techo):
    """
    Cuenta los elementos de una lista que sean menores a un tope
    
    :param lista: lista de valores
    :type lista: lista de datos que soporte comparación por menor
    :param techo: valor máximo para filtrar
    :type techo: el mismo de los elementos de la lista
    :returns: la cantidad de elementos cuyo valor sea menor al techo
    :rtype: entero
    """
    c = 0
    for x in lista:
        if x < techo:
            c += 1
            
    return c


def promedio(lista):
    """
    Calcula el promedio simple de todos los elemento de una lista
    
    :param lista: lista
    :type lista: lista de números
    :returns: el promedio de todos los valores de la lista o 0 si la lista está vacía
    :rtype: flotante
    """
    cantidad = len(lista)
    if cantidad == 0:
        return 0
    
    suma = 0
    for x in lista:
        suma += x         
           
    return suma / cantidad


def existe(lista, buscado):
    """
    Busca un valor en una lista e informa si lo pudo encontrar
    
    :param lista: una lista de cualquier tipo
    :param buscado: el valor que se busca
    :tipo buscado: el mismo tipo que el de los datos almacenados en la lista
    
    :returns: verdadero si el elemento buscado existe en la lista y falso en caso contrario
    :rtype: boolean
    """
    for x in lista:
        if x == buscado:
            return True
        
    return False


