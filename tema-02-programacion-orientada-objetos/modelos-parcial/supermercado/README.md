# El supermercado

## Consigna (tipo parcial)

Una cadena de supermercados posee varias sucursales con diferentes características, agrupadas en tres formatos diferentes.

- **Hipermercados**: además del punto de venta, poseen boxes que cede a comerciantes pequeños a cambio de un alquiler mensual.
- **Supermercados tradicionales**: en edificaciones propias; algunos tienen un formato más orientado a la venta mayorista.
- **Mini**: en locales que alquila en plantas bajas de edificios de viviendas, abonando un alquiler mensual al consorcio.

De cada sucursal el supermercado registra la superficie en metros cuadrados del salón de ventas y el total facturado en el último mes. Adicionalmente existen dos cálculos relevantes: el **resultado comercial** y el **índice de rentabilidad**.

- El resultado comercial de cada sucursal tipo supermercado es equivalente a la facturación. En los locales de hipermercados se suma el total ganado en concepto de alquileres; en los de modalidad Mini se resta el alquiler abonado al edificio.
- El índice de rentabilidad es el cociente entre el resultado comercial y la superficie. Un local de hipermercado es rentable si su índice es mayor a 50; uno Mini si es mayor a 35. Los locales tradicionales son rentables si su índice es mayor a 40, pero los mayoristas deben tener un índice mayor a 45.

Se necesita un programa que lea del archivo `sucursales.csv` la lista de todas las sucursales y las almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Suma de ganancia**: total del resultado comercial de todas las sucursales.
2. **Cantidad de locales no rentables**: cantidad de sucursales cuyo índice de rentabilidad sea menor al exigido.
3. **Local más rentable**: número y tipo de la sucursal cuyo índice de rentabilidad sea el mayor de todos.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos anteriores.

### Estructura del archivo `sucursales.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por sucursal):

1. Tipo de sucursal: 1 para hiper, 2 para super y 3 para mini
2. Número: número sin repetición que identifica cada sucursal
3. Superficie: número de tipo entero con la superficie en metros cuadrados
4. Facturación: número de tipo float con la facturación del local, expresada en miles de pesos
5. Si es una sucursal de hipermercado, el importe ganado por alquileres; si es de supermercado, un 1 si es mayorista y 0 si no lo es; si es de modalidad Mini, el importe pagado por el alquiler

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Sucursal(numero, superficie, facturacion)` — clase base con atributos homónimos y métodos `resultado_comercial()`, `es_rentable()` y `tipo()`.
- `Hiper(numero, superficie, facturacion, alquileres)` — suma los alquileres al resultado; rentable si índice > 50; `tipo()` = 1.
- `Super(numero, superficie, facturacion, mayorista)` — el resultado es la facturación; rentable si índice > 40 (tradicional) o > 45 (mayorista); `tipo()` = 2.
- `Mini(numero, superficie, facturacion, alquiler)` — resta el alquiler al resultado; rentable si índice > 35; `tipo()` = 3.
- `Empresa()` — contiene la colección de sucursales y ofrece:
  - `agregar_sucursal(sucursal)`
  - `suma_ganancia()`
  - `cantidad_no_rentables()`
  - `local_mas_rentable()`

## Archivos

- `sucursales.csv` — datos del parcial.
- `test_supermercado.py` — casos de prueba (pytest) entregados junto a la consigna.

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución junto a `test_supermercado.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 13 pruebas en verde.