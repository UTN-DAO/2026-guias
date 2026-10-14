### Semáforo con interfaz (tkinter)

Ejemplo de referencia del patrón **State**: un semáforo de tráfico con interfaz
gráfica. Cada estado (`Rojo`, `Verde`, `Amarillo`) conoce su propia transición y
el contexto (`Semaforo`) sólo delega en el estado actual.

Requiere un entorno con interfaz gráfica (tkinter viene con Python).

Ejecutar la ventana:

```
python main.py
```

Demo por consola, sin interfaz gráfica:

```
python main.py --consola
```

La lógica del patrón vive en `estado.py` y `semaforo.py`; la ventana, en
`ventana.py`.
