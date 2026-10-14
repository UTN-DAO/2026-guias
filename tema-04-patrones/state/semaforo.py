"""Contexto del patrón State: el semáforo delega en su estado actual."""
from estado import Rojo


class Semaforo:
    def __init__(self):
        self._estado = Rojo()
        self.modo_peatonal = False

    @property
    def estado(self):
        return self._estado

    def activar_modo_peatonal(self):
        self.modo_peatonal = True

    def desactivar_modo_peatonal(self):
        self.modo_peatonal = False

    def cambiar_estado(self, estado):
        self._estado = estado

    def siguiente(self):
        self._estado.siguiente(self)

    def actual(self):
        return self._estado.nombre
