"""Receptor del patrón Command: la tortuga de LOGO.

La tortuga conoce las operaciones concretas de dibujo; los comandos delegan en
ella.
"""
import math


class Tortuga:
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
