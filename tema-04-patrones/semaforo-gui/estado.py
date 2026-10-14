"""Estados del semáforo (patrón State) con su color para dibujar.

Cada estado conoce su transición y define con qué colores se pinta cuando está
encendido y cuando está apagado.
"""
from abc import ABC, abstractmethod


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
