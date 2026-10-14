"""Contexto del patrón State: mantiene el estado actual y delega en él."""
from estado import Rojo


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
