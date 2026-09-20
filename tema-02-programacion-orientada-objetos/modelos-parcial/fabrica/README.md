# La fábrica

## Consigna (tipo parcial)

Una fábrica posee una máquina manufacturera a la que se le realizan diversos mantenimientos para garantizar su correcto funcionamiento.

Cada vez que se le realiza un mantenimiento se registra el nombre del operario que lo realiza, la fecha en que se efectuó y el importe que se gastó en repuestos.

- **Mantenimientos preventivos**: periódicos, reemplazan insumos (lubricantes, repuestos de vida útil restringida) y verifican el funcionamiento. De ellos se registra el importe gastado en insumos y el resultado: 1 si la máquina funciona correctamente, 2 si se recomienda la revisión del servicio técnico y 3 si se detecta una rotura.
- **Mantenimientos correctivos**: la máquina quedó impedida de funcionar y requiere la intervención. De ellos se registra la cantidad de horas de parada y el total abonado al técnico reparador.

Se necesita un programa que lea del archivo `mantenimientos.csv` la lista de todos los mantenimientos y los almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Suma de gastos**: total abonado por todo concepto en todos los mantenimientos registrados.
2. **Cantidad de mantenimientos caros**: total de mantenimientos de cualquier tipo que hayan tenido un gasto total de más de $10.000.
3. **Rotura más larga**: la fecha y el nombre del operario del mantenimiento correctivo de mayor duración.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos anteriores.

### Estructura del archivo `mantenimientos.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por mantenimiento):

1. Tipo de mantenimiento: 1 para preventivo y 2 para correctivo
2. Fecha: una cadena
3. Operario: nombre del operario que realizó el mantenimiento
4. Importe de repuestos: número de tipo float
5. Si es un preventivo, resultado del mantenimiento (1, 2 o 3); si es un correctivo, cantidad de horas de parada
6. Si es un preventivo, importe de los insumos; si es un correctivo, importe que cobró el técnico

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Mantenimiento(fecha, operario, repuestos)` — clase base con atributos homónimos y método `gasto_total()`.
- `Preventivo(fecha, operario, repuestos, resultado, insumos)` — redefine `gasto_total()` como repuestos + insumos.
- `Correctivo(fecha, operario, repuestos, horas_parada, tecnico)` — redefine `gasto_total()` como repuestos + técnico.
- `Maquina()` — contiene la colección de mantenimientos y ofrece:
  - `agregar_mantenimiento(mantenimiento)`
  - `suma_gastos()`
  - `cantidad_mantenimientos_caros()`
  - `rotura_mas_larga()`

## Archivos

- `mantenimientos.csv` — datos del parcial.
- `test_fabrica.py` — casos de prueba (pytest) entregados junto a la consigna.

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución junto a `test_fabrica.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 12 pruebas en verde.