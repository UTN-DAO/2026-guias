### Semáforo con interfaz (tkinter)

Ejemplo de referencia del patrón **State**: un semáforo de tráfico con interfaz
gráfica. Cada estado (`Rojo`, `Verde`, `Amarillo`) conoce su propia transición y
el contexto (`Semaforo`) sólo delega en el estado actual.

Requiere un entorno con interfaz gráfica (tkinter viene con Python).

Ejecutar la ventana:

```
python semaforo_gui.py
```

Demo por consola, sin interfaz gráfica:

```
python semaforo_gui.py --consola
```
