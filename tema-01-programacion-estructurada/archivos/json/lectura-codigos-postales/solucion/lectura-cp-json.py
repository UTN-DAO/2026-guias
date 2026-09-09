import json
from rich import print_json
from rich.pretty import pprint

def leer_codigos(nombre_archivo):
    """Leer el archivo de códigos postales, en formato JSON

    :param nombre_archivo: Nombre del archivo que se desea leer
    :type nombre_archivo: string
    :return: Diccionario con el contenido del archivo
    :rtype: Dict
    """
    archivo = open(nombre_archivo)
    contenido = archivo.read()
    json_content = json.loads(contenido)
    archivo.close()
    
    return json_content    
       
    
def buscar_codigo(lista, buscado):
    """Busca el código indicado en la lista de códigos postales
    Elabora una lista con todas las coincidencias encontradas
    y la retorna al usuario.

    :param lista: Lista con los códigos postales
    :type lista: List
    :param buscado: Item a buscar
    :type buscado: string
    :return: Lista con los elementos encontrados
    :rtype: List
    """
    encontrados = []
    #pprint (lista)
    for item in lista:
        # Convierto el valor a buscar a entero porque en los archivos
        # JSON se mantiene el tipo de datos
        if item['codigo_postal'] == int(buscado):
            encontrados.append(item)
            
    return encontrados    
    # Con comprensión de listas
    # return [c for c in lista if c[1] == int(buscado)]
       
if __name__ == "__main__":
    codigos = leer_codigos("cp.json")
    #pprint (codigos)

    buscado = input("Ingrese un código a buscar (fin con cadena vacía):")
    while buscado:
        encontrados = buscar_codigo(codigos, buscado)
        if encontrados:
            for item in encontrados:
                print(f"{item['codigo_provincia']}: {item['codigo_postal']} -> {item['nombre_localidad']}")
        else:
            print("No se encontró ninguna localidad")
        buscado = input("Ingrese un código a buscar (fin con cadena vacía):")
        


