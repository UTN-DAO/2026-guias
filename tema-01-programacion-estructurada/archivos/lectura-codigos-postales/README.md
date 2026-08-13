## Lectura de códigos postales

El archivo [cp.csv](./cp.csv) contiene el listado de los códigos postales de tres provincias argentinas. En cada línea se encuentran, separados por un símbolo de punto y coma (;) los siguientes datos:

* Provincia, representada por una letra mayúscula según el [estándar ISO](https://es.wikipedia.org/wiki/ISO_3166-2:AR) correspondiente.
* Código, es un número entero de cuatro dígitos que identifica una localidad o varias localidades vecinas. Puede estar repetido.
* Nombre, es el nombre de la localidad correspondiente a ese código.

Se requiere leer todo el contenido del archivo y guardarlo en una lista que contenga un elemento por cada línea. En cada elemento debe almacenarse alguna estructura de datos que permita acceder individualmente a cada dato que conforma un codigo postal.

Luego de la carga el programa debe permitir el ingreso de uno o más códigos numéricos y listar provincia y nombre de todas las localidades asignadas a dichos códigos.

