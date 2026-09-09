def main():
    numeros = set()
    impares = 0
    suma_total = 0
    pares = []
    
    with open("numeros.txt", "r") as archivo:
        lineas = archivo.readlines()
        
        for linea in lineas:
            numero = int(linea.strip())
            numeros.add(numero)
            
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares += 1
                
            suma_total += numero
            
    cantidad_no_repetidos = len(numeros)
    cantidad_impares = impares
    suma_total = suma_total
    promedio_pares = sum(pares) / len(pares) if pares else 0
    
    print("Cantidad de números no repetidos:", cantidad_no_repetidos)
    print("Suma de todos los números:", suma_total)
    print("Cantidad de impares:", cantidad_impares)
    print("Promedio de pares:", promedio_pares)

if __name__ == "__main__":
    main()
