"""Ventana tkinter del semáforo (la vista, separada de la lógica).

La ventana es sólo una vista: cada cierto intervalo le pide al contexto que
avance y redibuja las luces. No decide el estado siguiente.
"""
import tkinter as tk

from semaforo import Semaforo
from estado import Rojo, Amarillo, Verde


def construir_ventana():
    raiz = tk.Tk()
    raiz.title("Semaforo (patron State)")
    raiz.configure(bg="#1c1c1c")
    raiz.resizable(False, False)

    semaforo = Semaforo()

    ancho, alto = 240, 560
    canvas = tk.Canvas(raiz, width=ancho, height=alto, bg="#1c1c1c",
                       highlightthickness=0)
    canvas.pack(padx=10, pady=10)

    radio = 62
    centros = {
        "ROJO": (ancho // 2, 100),
        "AMARILLO": (ancho // 2, 275),
        "VERDE": (ancho // 2, 450),
    }
    # El orden vertical de las luces (arriba rojo, abajo verde).
    orden = ["ROJO", "AMARILLO", "VERDE"]
    # Instancias sin estado solo para leer los colores apagados.
    apagados = {"ROJO": Rojo().color_inactivo,
                "AMARILLO": Amarillo().color_inactivo,
                "VERDE": Verde().color_inactivo}

    def dibujar():
        canvas.delete("all")
        canvas.create_rectangle(ancho // 2 - 90, 30, ancho // 2 + 90,
                                alto - 30, fill="#2b2b2b",
                                outline="#555555", width=3)
        actual = semaforo.actual()
        for nombre in orden:
            cx, cy = centros[nombre]
            if nombre == actual:
                color = semaforo.estado.color_activo
                canvas.create_oval(cx - radio - 8, cy - radio - 8,
                                   cx + radio + 8, cy + radio + 8,
                                   fill=color, outline="")
            else:
                color = apagados[nombre]
            canvas.create_oval(cx - radio, cy - radio, cx + radio, cy + radio,
                               fill=color, outline="#111111", width=2)

    etiqueta = tk.Label(raiz, text="", font=("Helvetica", 16, "bold"),
                        fg="white", bg="#1c1c1c")
    etiqueta.pack()

    controles = tk.Frame(raiz, bg="#1c1c1c")
    controles.pack(pady=6)

    pausado = tk.BooleanVar(value=False)

    def alternar_pausa():
        pausado.set(not pausado.get())
        boton_pausa.config(text="Reanudar" if pausado.get() else "Pausar")

    boton_pausa = tk.Button(controles, text="Pausar", width=10,
                            command=alternar_pausa)
    boton_pausa.pack(side="left", padx=4)

    tk.Label(controles, text="Velocidad (s):", fg="white",
             bg="#1c1c1c").pack(side="left", padx=(12, 2))
    velocidad = tk.DoubleVar(value=1.5)
    tk.Spinbox(controles, from_=0.5, to=5.0, increment=0.5, width=4,
               textvariable=velocidad).pack(side="left")

    def actualizar():
        etiqueta.config(text=f"Estado: {semaforo.actual()}")
        dibujar()
        if not pausado.get():
            semaforo.siguiente()
        raiz.after(int(velocidad.get() * 1000), actualizar)

    dibujar()
    actualizar()
    return raiz
