

if __name__ == "__main__":
    
    apellido_buscado = input("Ingrese el apellido que desea buscar: ")
    
    archivo = open("personas.csv")
    
    while True:
        linea = archivo.readline()
        if not linea: break
        datos = linea[:-1].split(",")
        if datos[2] == apellido_buscado:
            print(f"{datos[1]} {apellido_buscado}: {datos[3]} años")
            
    archivo.close()
    
    