### Intérprete LOGO con interfaz (tkinter)

Ejemplo de referencia del patrón **Command**: cada instrucción del lenguaje LOGO
es un objeto comando con `ejecutar()`. El invocador (`Programa`) recorre la lista
de comandos sin conocer su tipo concreto; el receptor (`Tortuga`) hace el dibujo.
Los comandos `REPITE` son compuestos: contienen otros comandos.

Requiere un entorno con interfaz gráfica (tkinter viene con Python).

Ejecutar la ventana:

```
python logo_command.py
```

Interpretar un programa LOGO por consola, sin interfaz gráfica:

```
python logo_command.py --consola "REPITE 4 [ AVANZA 120 GIRADERECHA 90 ]"
```
