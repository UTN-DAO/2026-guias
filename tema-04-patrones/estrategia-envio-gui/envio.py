"""Contexto del patrón Strategy: delega el cálculo en la estrategia.

El cliente (la ventana) es quien elige la estrategia y la inyecta acá.
"""


class Paquete:
    def __init__(self, peso_kg, distancia_km):
        self.peso = peso_kg
        self.distancia = distancia_km


class CalculadorEnvio:
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia):
        self._estrategia = estrategia

    @property
    def estrategia(self):
        return self._estrategia

    def calcular(self, paquete):
        return self._estrategia.calcular(paquete)
