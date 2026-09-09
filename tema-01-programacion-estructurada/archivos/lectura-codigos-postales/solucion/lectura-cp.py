

def leer_codigos(nombre_archivo):
    
    codigos = []
    archivo = open(nombre_archivo)
    
    for linea in archivo.readlines():
        codigo = tuple(linea[:-1].split(";"))
        codigos.append(codigo)

    archivo.close()
    
    return codigos    
       
    
def buscar_codigo(lista, buscado):
    encontrados = []
    
    for c in lista:
        if c[1] == buscado:
            encontrados.append(c)
            
    return encontrados    
    # Con comprensión de listas
    # return [c for c in lista if c[1] == buscado]
       
if __name__ == "__main__":
    codigos = leer_codigos("cp.csv")

    buscado = input("Ingrese un código a buscar (fin con cadena vacía):")
    while buscado:
        encontrados = buscar_codigo(codigos, buscado)
        if encontrados:
            for c in encontrados:
                print(f"{c[0]}: {c[2]}")
        else:
            print("No se encontró ninguna localidad")
        buscado = input("Ingrese un código a buscar (fin con cadena vacía):")
        


