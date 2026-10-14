### Lista de precios con vistas (tkinter)

Ejemplo de referencia del patrón **Observer**: el modelo (`ListaPrecios`) notifica
a sus observadores cada vez que cambia un precio. La ventana muestra **tres**
vistas sobre el mismo modelo: una grilla de productos, una etiqueta de totales y
una caja de auditoría.

Requiere un entorno con interfaz gráfica (tkinter viene con Python).

Ejecutar la ventana:

```
python observer_gui.py
```

Demo por consola, sin interfaz gráfica:

```
python observer_gui.py --consola
```
