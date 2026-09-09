import re

def cargar_palabras_archivo(archivo):
    with open(archivo, "r") as file:
        texto = file.read()
        palabras = re.findall(r'\b\w+\b', texto)  # Encuentra todas las palabras
#        palabras = file.read().split()
    return palabras

def main():
    # Cargar palabras del Quijote
    palabras_quijote = cargar_palabras_archivo("quijote.txt")
    palabras_quijote = set(palabras_quijote)  # Convertir a conjunto para eliminar duplicados
    
    # Cargar palabras del diccionario inglés
    palabras_ingles = cargar_palabras_archivo("words_alpha.txt")
    palabras_ingles = set(palabras_ingles)
    
    # Cálculos
    cantidad_palabras_quijote = len(palabras_quijote)
    cantidad_palabras_ingles = len(palabras_ingles)
    
    palabras_no_en_diccionario = palabras_quijote - palabras_ingles
    cantidad_palabras_no_en_diccionario = len(palabras_no_en_diccionario)
    
    palabras_no_en_diccionario_ordenadas = sorted(palabras_no_en_diccionario)
    
    # Resultados
    print("Cantidad de palabras únicas en el Quijote:", cantidad_palabras_quijote)
    print("Cantidad de palabras en el diccionario inglés:", cantidad_palabras_ingles)
    print("Cantidad de palabras en el Quijote que no están en el diccionario:", cantidad_palabras_no_en_diccionario)
    
    #if palabras_no_en_diccionario_ordenadas:
    #    print("\nPalabras en el Quijote que no están en el diccionario:")
    #    for palabra in palabras_no_en_diccionario_ordenadas:
    #       print(palabra)

if __name__ == "__main__":
    main()
