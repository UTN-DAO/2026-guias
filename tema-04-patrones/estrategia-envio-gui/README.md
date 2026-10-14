### Cálculo de envío con interfaz (tkinter)

Ejemplo de referencia del patrón **Strategy**: el coste de envío se calcula con
una familia de estrategias (`EnvioEstandar`, `EnvioExpreso`, `TarifaPlana`). La
ventana es el cliente: es quien elige la estrategia y la inyecta en el contexto
(`CalculadorEnvio`).

Requiere un entorno con interfaz gráfica (tkinter viene con Python).

Ejecutar la ventana:

```
python estrategia_envio_gui.py
```

Demo por consola, sin interfaz gráfica:

```
python estrategia_envio_gui.py --consola
```
