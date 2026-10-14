"""
Patron State: semaforo de trafico con interfaz tkinter.

Participantes:
  * Estado -> interfaz comun de los estados (siguiente / entrar / salir).
  * Rojo, Verde, Amarillo -> estados concretos. Cada uno conoce su
    transicion (llama a cambiar_estado del contexto).
  * Semaforo -> contexto. Delega en el estado actual y no decide por si
    mismo cual es el proximo estado.

La ventana es solo una vista: cada cierto intervalo le pide al contexto
que avance (siguiente()) y redibuja las luces. El cliente no elige el
estado siguiente: lo decide el propio estado.
"""
from abc import ABC, abstractmethod

# ---------------------------------------------------------------- Estado
class Estado(ABC):
    """Interfaz comun de los estados del semaforo."""

    nombre = ""
    color_activo = "#000000"
    color_inactivo = "#222222"

    def entrar(self, semaforo):
        """Accion al entrar al estado (puede quedar vacia)."""

    def salir(self, semaforo):
        """Accion al salir del estado (puede quedar vacia)."""

    @abstractmethod
    def siguiente(self, semaforo):
        """Ejecuta la transicion al siguiente estado."""


class Rojo(Estado):
    nombre = "ROJO"
    color_activo = "#e53935"
    color_inactivo = "#5a1b1a"

    def siguiente(self, semaforo):
        semaforo.cambiar_estado(Verde())


class Verde(Estado):
    nombre = "VERDE"
    color_activo = "#43a047"
    color_inactivo = "#1b3a1e"

    def siguiente(self, semaforo):
        semaforo.cambiar_estado(Amarillo())


class Amarillo(Estado):
    nombre = "AMARILLO"
    color_activo = "#fdd835"
    color_inactivo = "#5a4d18"

    def siguiente(self, semaforo):
        semaforo.cambiar_estado(Rojo())


# --------------------------------------------------------------- Contexto
class Semaforo:
    """Contexto: mantiene el estado actual y delega en el."""

    def __init__(self, estado_inicial=None):
        self._estado = estado_inicial or Rojo()
        self._estado.entrar(self)

    @property
    def estado(self):
        return self._estado

    def cambiar_estado(self, estado):
        self._estado.salir(self)
        self._estado = estado
        self._estado.entrar(self)

    def siguiente(self):
        self._estado.siguiente(self)

    def actual(self):
        return self._estado.nombre


# ------------------------------------------------------------------- GUI
def construir_ventana():
    import tkinter as tk

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
            # color segun si es la luz encendida
            if nombre == actual:
                color = semaforo.estado.color_activo
                # brillo exterior de la luz encendida
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

    # --- controles ---
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


def demo_consola(transiciones=7):
    """Modo sin ventana: recorre el semaforo e imprime la secuencia."""
    semaforo = Semaforo()
    print("=== Semaforo (State), modo consola ===")
    for _ in range(transiciones):
        print(f"Estado actual: {semaforo.actual()}")
        semaforo.siguiente()


if __name__ == "__main__":
    import sys

    if "--consola" in sys.argv:
        demo_consola()
    else:
        construir_ventana().mainloop()
