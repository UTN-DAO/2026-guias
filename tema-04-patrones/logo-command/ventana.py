"""Ventana tkinter del intérprete LOGO (la vista).

La ventana compila el texto, ejecuta el programa sobre una tortuga nueva y
dibuja los trazos. La lógica del patrón no depende de ella.
"""
import tkinter as tk
from tkinter import messagebox

from comandos import Programa
from parser import compilar, ErrorLOGO
from programas import EJEMPLO, ESPIRAL, ESTRELLA
from tortuga import Tortuga


def construir_ventana():
    raiz = tk.Tk()
    raiz.title("Interprete LOGO (patron Command)")
    raiz.resizable(True, True)

    canvas = tk.Canvas(raiz, width=520, height=520, bg="white",
                       highlightthickness=1, highlightbackground="#B0BCD4")
    canvas.pack(side="right", fill="both", expand=True)

    panel = tk.Frame(raiz, padx=10, pady=10)
    panel.pack(side="left", fill="y")

    tk.Label(panel, text="Programa LOGO:").pack(anchor="w")
    texto = tk.Text(panel, width=34, height=14, font=("Courier", 11))
    texto.insert("1.0", EJEMPLO)
    texto.pack()

    estado = tk.Label(panel, text="", fg="#5A5A5A", wraplength=260,
                      justify="left")
    estado.pack(anchor="w", pady=6)

    app = {"programa": Programa(), "tortuga": Tortuga()}

    def redibujar():
        tortuga = Tortuga()
        app["programa"].ejecutar(tortuga)
        app["tortuga"] = tortuga
        dibujar_tortuga(canvas, tortuga)
        comandos = app["programa"].descripcion()
        estado.config(text="{} comandos: {}".format(
            len(comandos), ", ".join(comandos[:6]) + ("..." if len(comandos) > 6 else "")))

    def ejecutar():
        try:
            comandos = compilar(texto.get("1.0", "end"))
        except ErrorLOGO as error:
            messagebox.showerror("Error de LOGO", str(error))
            return
        app["programa"] = Programa(comandos)
        redibujar()

    def deshacer():
        quitado = app["programa"].deshacer()
        if quitado is None:
            estado.config(text="No hay comandos para deshacer")
            return
        redibujar()

    def limpiar():
        app["programa"] = Programa()
        app["tortuga"] = Tortuga()
        texto.delete("1.0", "end")
        dibujar_tortuga(canvas, app["tortuga"])
        estado.config(text="")

    def cargar(programa):
        texto.delete("1.0", "end")
        texto.insert("1.0", programa)
        ejecutar()

    botones = tk.Frame(panel)
    botones.pack(fill="x", pady=4)
    tk.Button(botones, text="Ejecutar", command=ejecutar).pack(side="left")
    tk.Button(botones, text="Deshacer", command=deshacer).pack(side="left", padx=4)
    tk.Button(botones, text="Limpiar", command=limpiar).pack(side="left")

    presets = tk.Frame(panel)
    presets.pack(fill="x")
    tk.Label(presets, text="Ejemplos:").pack(anchor="w")
    for nombre, programa in (("Cuadrado", EJEMPLO), ("Espiral", ESPIRAL),
                             ("Estrella", ESTRELLA)):
        tk.Button(presets, text=nombre,
                  command=lambda p=programa: cargar(p)).pack(side="left", padx=2)

    ejecutar()
    return raiz


def dibujar_tortuga(canvas, tortuga):
    """Dibuja los trazos de la tortuga, ajustando la escala al lienzo."""
    canvas.delete("all")
    ancho = int(canvas["width"])
    alto = int(canvas["height"])
    margen = 20

    puntos = [(x1, y1) for x1, y1, _, _, _ in tortuga.trazos]
    puntos += [(x2, y2) for _, _, x2, y2, _ in tortuga.trazos]
    puntos.append((tortuga.x, tortuga.y))
    if not puntos:
        return

    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    ancho_dibujo = max(max_x - min_x, 1e-6)
    alto_dibujo = max(max_y - min_y, 1e-6)
    escala = min((ancho - 2 * margen) / ancho_dibujo,
                 (alto - 2 * margen) / alto_dibujo, 3.0)

    def a_canvas(x, y):
        return (margen + (x - min_x) * escala,
                margen + (y - min_y) * escala)

    for x1, y1, x2, y2, color in tortuga.trazos:
        cx1, cy1 = a_canvas(x1, y1)
        cx2, cy2 = a_canvas(x2, y2)
        canvas.create_line(cx1, cy1, cx2, cy2, fill=color, width=2)

    # marcar la posicion final de la tortuga
    cx, cy = a_canvas(tortuga.x, tortuga.y)
    canvas.create_oval(cx - 4, cy - 4, cx + 4, cy + 4, fill="#003087", outline="")
