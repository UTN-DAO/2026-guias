"""Contexto del patrón Strategy: el calculador delega en la estrategia.

Agregar una estrategia nueva no modifica esta clase.
"""


class Paquete:
    def __init__(self, peso, distancia):
        self.peso = peso
        self.distancia = distancia


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
