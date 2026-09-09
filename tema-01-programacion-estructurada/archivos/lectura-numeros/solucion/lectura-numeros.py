from proceso_listas import *

def leer_archivo(nombre_archivo):
    
    numeros = []
    
    archivo = open(nombre_archivo)
    
    while True:
        linea = archivo.readline()
        if not linea:
            break
        n = int(linea[:-1])
        numeros.append(n)
    
    archivo.close()
    
    return numeros


if __name__ == "__main__":
    lista = leer_archivo("numeros.txt")
    promedio_todos = promedio(lista)
    mayores = cantidad_mayor(lista, promedio_todos)
    pares = [x for x in lista if x % 2 == 0]
    
    print("Del archivo se leyeron los números")
    print(f"El promedio de esos números es de {promedio_todos:5.2f}")
    print(f"Y {mayores} son mayores que el promedio")
    print("Listado de los pares:")
    for x in pares:
        print(x)
