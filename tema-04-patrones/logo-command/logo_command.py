"""
Patron Command: un interprete del lenguaje LOGO (tortuga grafica).

Cada instruccion del lenguaje se representa como un objeto comando con
ejecutar(). El invocador (Programa) recorre la lista de comandos y los
ejecuta sin conocer su tipo concreto; cada comando delega el trabajo en
el receptor (Tortuga).

Participantes:
  * Comando -> interfaz con ejecutar(tortuga).
  * Avanzar, Retroceder, GirarDerecha, GirarIzquierda, Levantar, Bajar,
    CambiarColor, Repetir -> comandos concretos.
  * Repetir -> comando COMPUESTO: contiene otros comandos.
  * Tortuga -> receptor. Sabe mover el cursor y registrar los trazos.
  * Programa -> invocador. Mantiene y ejecuta la secuencia de comandos.

Como los comandos son objetos, se pueden guardar (historial), descartar
(deshacer) y volver a ejecutar (repeticion). Aca el deshacer se resuelve
guardando la lista de comandos y volviendo a ejecutarla desde cero.
"""
import math
from abc import ABC, abstractmethod

# --------------------------------------------------------------- Receptor
class Tortuga:
    """Receptor: conoce las operaciones concretas de dibujo."""

    def __init__(self):
        self.reiniciar()

    def reiniciar(self):
        self.x = 0.0
        self.y = 0.0
        self.angulo = 0.0        # 0 grados = hacia arriba; crece a la derecha
        self.pluma_abajo = True
        self.color = "black"
        self.trazos = []         # (x1, y1, x2, y2, color)

    def avanzar(self, distancia):
        rad = math.radians(self.angulo)
        nueva_x = self.x + distancia * math.sin(rad)
        nueva_y = self.y - distancia * math.cos(rad)
        if self.pluma_abajo:
            self.trazos.append((self.x, self.y, nueva_x, nueva_y, self.color))
        self.x, self.y = nueva_x, nueva_y

    def girar(self, grados):
        self.angulo = (self.angulo + grados) % 360

    def levantar(self):
        self.pluma_abajo = False

    def bajar(self):
        self.pluma_abajo = True

    def cambiar_color(self, color):
        self.color = color


# --------------------------------------------------------------- Comandos
class Comando(ABC):
    @abstractmethod
    def ejecutar(self, tortuga):
        """Realiza la operacion sobre el receptor."""

    def descripcion(self):
        return type(self).__name__


class Avanzar(Comando):
    def __init__(self, distancia):
        self.distancia = distancia

    def ejecutar(self, tortuga):
        tortuga.avanzar(self.distancia)

    def descripcion(self):
        return f"Avanzar({self.distancia})"


class Retroceder(Comando):
    def __init__(self, distancia):
        self.distancia = distancia

    def ejecutar(self, tortuga):
        tortuga.avanzar(-self.distancia)

    def descripcion(self):
        return f"Retroceder({self.distancia})"


class GirarDerecha(Comando):
    def __init__(self, grados):
        self.grados = grados

    def ejecutar(self, tortuga):
        tortuga.girar(self.grados)

    def descripcion(self):
        return f"GirarDerecha({self.grados})"


class GirarIzquierda(Comando):
    def __init__(self, grados):
        self.grados = grados

    def ejecutar(self, tortuga):
        tortuga.girar(-self.grados)

    def descripcion(self):
        return f"GirarIzquierda({self.grados})"


class Levantar(Comando):
    def ejecutar(self, tortuga):
        tortuga.levantar()


class Bajar(Comando):
    def ejecutar(self, tortuga):
        tortuga.bajar()


class CambiarColor(Comando):
    def __init__(self, color):
        self.color = color

    def ejecutar(self, tortuga):
        tortuga.cambiar_color(self.color)

    def descripcion(self):
        return f"CambiarColor({self.color})"


class Repetir(Comando):
    """Comando compuesto: ejecuta una secuencia de comandos varias veces."""

    def __init__(self, veces, comandos):
        self.veces = veces
        self.comandos = comandos

    def ejecutar(self, tortuga):
        for _ in range(self.veces):
            for comando in self.comandos:
                comando.ejecutar(tortuga)

    def descripcion(self):
        return f"Repetir({self.veces}, {len(self.comandos)} comandos)"


class Programa:
    """Invocador: mantiene una secuencia de comandos y la ejecuta."""

    def __init__(self, comandos=None):
        self.comandos = list(comandos or [])

    def agregar(self, comando):
        self.comandos.append(comando)

    def deshacer(self):
        return self.comandos.pop() if self.comandos else None

    def ejecutar(self, tortuga):
        for comando in self.comandos:
            comando.ejecutar(tortuga)

    def descripcion(self):
        return [comando.descripcion() for comando in self.comandos]


# ---------------------------------------------------------------- Parser
COLORES = {
    "negro": "black", "rojo": "red", "verde": "green", "azul": "blue",
    "naranja": "orange", "violeta": "purple", "amarillo": "gold",
    "celeste": "deepskyblue", "rosa": "hotpink", "gris": "gray",
}


class ErrorLOGO(Exception):
    """Error de sintaxis o de colores en un programa LOGO."""


def tokenizar(texto):
    texto = texto.replace("[", " [ ").replace("]", " ] ").replace(",", " ")
    return texto.split()


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def mirar(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self):
        token = self.mirar()
        self.pos += 1
        return token

    def numero(self):
        token = self.consumir()
        if token is None:
            raise ErrorLOGO("Se esperaba un numero y el programa termino")
        try:
            return float(token)
        except ValueError:
            raise ErrorLOGO(f"Se esperaba un numero, no '{token}'")

    def esperar(self, simbolo):
        token = self.consumir()
        if token != simbolo:
            raise ErrorLOGO(f"Se esperaba '{simbolo}', no '{token}'")

    def parsear(self):
        comandos = []
        while self.mirar() is not None:
            comandos.append(self.parsear_comando())
        return comandos

    def parsear_comando(self):
        token = self.consumir()
        instruccion = token.upper()

        if instruccion == "AVANZA":
            return Avanzar(self.numero())
        if instruccion == "RETROCEDE":
            return Retroceder(self.numero())
        if instruccion == "GIRADERECHA":
            return GirarDerecha(self.numero())
        if instruccion == "GIRAIZQUIERDA":
            return GirarIzquierda(self.numero())
        if instruccion == "LEVANTA":
            return Levantar()
        if instruccion == "BAJA":
            return Bajar()
        if instruccion == "COLOR":
            return CambiarColor(self.color())
        if instruccion == "REPITE":
            veces = int(self.numero())
            self.esperar("[")
            cuerpo = []
            while self.mirar() != "]":
                if self.mirar() is None:
                    raise ErrorLOGO("Falta cerrar el bloque con ']'")
                cuerpo.append(self.parsear_comando())
            self.consumir()      # consume ']'
            return Repetir(veces, cuerpo)

        raise ErrorLOGO(f"Instruccion desconocida: '{token}'")

    def color(self):
        token = self.consumir()
        if token is None:
            raise ErrorLOGO("Falta el nombre del color")
        clave = token.lower()
        if clave not in COLORES:
            validos = ", ".join(sorted(COLORES))
            raise ErrorLOGO(f"Color '{token}' no valido. Opciones: {validos}")
        return COLORES[clave]


def compilar(texto):
    """Convierte el texto del programa en una lista de comandos."""
    return Parser(tokenizar(texto)).parsear()


# ------------------------------------------------------------------- GUI
EJEMPLO = """COLOR azul
REPITE 4 [ AVANZA 120 GIRADERECHA 90 ]
COLOR rojo
AVANZA 60
GIRADERECHA 90
AVANZA 60
"""

ESPIRAL = """COLOR verde
REPITE 36 [ REPITE 4 [ AVANZA 40 GIRADERECHA 90 ] GIRADERECHA 10 ]
"""

ESTRELLA = """COLOR naranja
REPITE 5 [ AVANZA 160 GIRADERECHA 144 ]
"""


def construir_ventana():
    import tkinter as tk
    from tkinter import messagebox

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


def demo_consola(programa=None):
    codigo = programa or EJEMPLO
    comandos = compilar(codigo)
    tortuga = Tortuga()
    invocador = Programa(comandos)
    invocador.ejecutar(tortuga)
    print("=== Interprete LOGO (Command) ===")
    print("Comandos de nivel superior:", invocador.descripcion())
    print(f"Trazos dibujados: {len(tortuga.trazos)}")
    print(f"Posicion final: ({tortuga.x:.1f}, {tortuga.y:.1f}), color {tortuga.color}")


if __name__ == "__main__":
    import sys

    if "--consola" in sys.argv:
        resto = [a for a in sys.argv[1:] if a != "--consola"]
        demo_consola(" ".join(resto) if resto else None)
    else:
        construir_ventana().mainloop()
