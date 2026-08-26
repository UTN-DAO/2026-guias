import csv

def cargar_datos(archivo):
    datos = {}
    with open(archivo, 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            documento, nombre, apellido, edad = linea
            datos[documento] = {'nombre': nombre, 'apellido': apellido, 'edad': int(edad)}
    return datos

def opcion1(datos):
    documento = input("Ingrese el documento: ")
    persona = buscar_por_documento(datos, documento)
    if persona:
        print("Datos de la persona encontrada:")
        print(f"Documento: {documento}")
        print(f"Nombre: {persona['nombre']}")
        print(f"Apellido: {persona['apellido']}")
        print(f"Edad: {persona['edad']}")
    else:
        print("Persona no encontrada.")

def buscar_por_documento(datos, documento):
    return datos.get(documento)

def opcion2(datos):
    apellido = input("Ingrese el apellido: ")
    personas_encontradas = buscar_por_apellido(datos, apellido)
    if personas_encontradas:
        print("Personas encontradas con ese apellido:")
        for persona in personas_encontradas:
            print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}, Edad: {persona['edad']}")
    else:
        print("No se encontraron personas con ese apellido.")
    

def buscar_por_apellido(datos, apellido):
    return list(filter(lambda p: p['apellido'] == apellido, datos.values()))

def opcion3(datos):
    promedio = promedio_edades(datos)
    print(f"El promedio de edades de todas las personas es: {promedio}")

def promedio_edades(datos):
    suma = sum(map(lambda p: p['edad'], datos.values()))
    return suma / len(datos) if datos else 0

def main():
    archivo = 'personas.csv'
    datos = cargar_datos(archivo)
    
    menu = {
        '1': opcion1,
        '2': opcion2,
        '3': opcion3,
    }
    
    opcion = '0'
    while opcion!='4':
        print("\nMenú:")
        print("1. Búsqueda por documento")
        print("2. Búsqueda por apellido")
        print("3. Mostrar promedio de edades")
        print("4. Salir")
        
        opcion = input("Ingrese una opción: ")
                
        if opcion in menu and opcion != '4':
            menu[opcion](datos)
        else:
            print("Opción no válida. Por favor ingrese una opción válida.")
            
if __name__ == "__main__":
    main()
