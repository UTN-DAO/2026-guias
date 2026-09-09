import csv

def cargar_datos(archivo):
    datos = {}
    with open(archivo, 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            documento, nombre, apellido, edad = linea
            datos[documento] = {'nombre': nombre, 'apellido': apellido, 'edad': int(edad)}
    return datos

def buscar_por_documento(datos, documento):
    if documento in datos:
        return datos[documento]
    else:
        return None

def buscar_por_apellido(datos, apellido):
    personas_encontradas = []
    for persona in datos.values():
        if persona['apellido'] == apellido:
            personas_encontradas.append(persona)
    return personas_encontradas

def promedio_edades(datos):
    edades = [persona['edad'] for persona in datos.values()]
    if edades:
        return sum(edades) / len(edades)
    else:
        return 0

def main():
    archivo = 'personas.csv'
    datos = cargar_datos(archivo)
    opcion = '0'
    while opcion!='4':
        print("\nMenú:")
        print("1. Búsqueda por documento")
        print("2. Búsqueda por apellido")
        print("3. Mostrar promedio de edades")
        print("4. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
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
        elif opcion == '2':
            apellido = input("Ingrese el apellido: ")
            personas_encontradas = buscar_por_apellido(datos, apellido)
            if personas_encontradas:
                print("Personas encontradas con ese apellido:")
                for persona in personas_encontradas:
                    print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}, Edad: {persona['edad']}")
            else:
                print("No se encontraron personas con ese apellido.")
        elif opcion == '3':
            promedio = promedio_edades(datos)
            print(f"El promedio de edades de todas las personas es: {promedio}")
        elif opcion == '4':
            print("Salir")
        else:
            print("Opción no válida. Por favor ingrese una opción válida.")
            
if __name__ == "__main__":
    main()
