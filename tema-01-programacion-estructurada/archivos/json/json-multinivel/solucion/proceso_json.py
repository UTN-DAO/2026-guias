from rich import print
from rich import print_json
from rich.pretty import pprint
import json

#################################################################
# Este ejercicio muestra como se accede a los distintos elementos
# de un archivo JSON de estructura compleja, con diferentes
# tipos y estructuras de datos internas.
#################################################################

# Abrir el archivo
m = open ("resultset.json")
# y leer todo el contenido en una variable string
content = m.read()
# Utilizando la funcion loads (notar la s al final)
# del módulo
json_var = json.loads(content)
print ("Ver todo el contenido:")
pprint (json_var)


"""
Como la estructura devuelta por JSON es un diccionario,
para acceder a sus componentes se debe utilizar la sintaxis
[ ' clave ' ], siendo clave el nombre de la misma.
En este caso leemos el contenido de la clave `ResultSet`
"""
print ("Ver solamente ResultSet:")
pprint(json_var['ResultSet'])

"""
JSON permite incluir arrays dentro de sus elementos.
Para acceder a dichos elementos se debe utilzar la misma sintaxis
que en cualquier array de Python. [ indice ], siendo `indice` la
posición en el array, comenzando en 0.
"""
print ("Acceder a un campo particular (FileSize) del segundo item")
pprint (json_var['ResultSet']["Result"][1]["FileSize"])

""" 
Un elemento de un array JSON puede ser, a su vez, una estructura
JSON (diccionario), y en caso de ser así se debe volver a utilizar
la nomenclatura [ ' clave ' ] para acceder a su contenido.
"""
print ("Acceder a la URL del item Thumbnail del segundo item")
pprint (json_var['ResultSet']["Result"][1]["Thumbnail"]["Url"])
