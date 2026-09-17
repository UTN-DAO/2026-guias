# La inmobiliaria

## Consigna (tipo parcial)

Una inmobiliaria de la ciudad administra una serie de inmuebles disponibles para ser alquilados.

De cada inmueble se conoce un código numérico, el nombre del propietario, la superficie de la construcción y el importe base del alquiler mensual.

El importe base es asignado por la inmobiliaria en función de las condiciones del mercado, pero el importe definitivo es calculado a partir del importe base y de las características particulares del inmueble.

- En el caso de las **casas**, al importe base se le adicionan $30.000 por cada dormitorio que posea y $100.000 si posee pileta de natación.
- Los **departamentos** ven incrementado su importe base en $20.000 si se encuentran en un piso inferior al tercero y se les incorpora el importe de las expensas.

Se necesita un programa que lea del archivo `inmuebles.csv` la lista de todos los inmuebles y los almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Suma de alquileres**: informe el total a recaudar en concepto de alquileres si todos los inmuebles se encuentran alquilados.
2. **Cantidad de casas premium**: informe la cantidad de casas de más de 150 metros cuadrados, más de 2 dormitorios y que posean pileta.
3. **Propietario del alquiler más bajo**: informe el nombre del propietario del departamento con el alquiler cuyo importe definitivo sea el más bajo.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos anteriores.

### Estructura del archivo `inmuebles.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por inmueble):

1. Tipo de inmueble: 1 para casas y 2 para departamentos
2. Código: número sin repetición que identifica cada inmueble
3. Nombre del propietario
4. Alquiler base: número de tipo float
5. Superficie: número entero expresado en metros cuadrados
6. Si es una casa, la cantidad de habitaciones; si es un departamento, el importe de las expensas
7. Si es una casa, un número 1 si tiene pileta y 0 si no tiene; si es un departamento, un número indicando el piso, con 0 para planta baja

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Inmueble(codigo, propietario, superficie, alquiler_base)` — clase base con atributos homónimos y método `alquiler()`.
- `Casa(codigo, propietario, superficie, alquiler_base, dormitorios, pileta)` — `pileta` booleano; redefine `alquiler()`.
- `Departamento(codigo, propietario, superficie, alquiler_base, expensas, piso)` — redefine `alquiler()`.
- `Inmobiliaria()` — contiene la colección de inmuebles y ofrece:
  - `agregar(inmueble)`
  - `suma_alquileres()`
  - `cantidad_casas_premium()`
  - `propietario_alquiler_mas_bajo()`

## Archivos

- `inmuebles.csv` — datos del parcial.
- `test_inmobiliaria.py` — casos de prueba (pytest) entregados junto a la consigna.

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución junto a `test_inmobiliaria.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 16 pruebas en verde.