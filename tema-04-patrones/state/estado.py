"""Estados concretos del semáforo (patrón State).

Cada estado conoce su propia transición: llama a ``cambiar_estado`` del
contexto en vez de que el contexto decida con una cadena de ``if``.
"""
from abc import ABC, abstractmethod


class Estado(ABC):
    nombre = ""

    @abstractmethod
    def siguiente(self, semaforo):
        ...


class Rojo(Estado):
    nombre = "ROJO"

    def siguiente(self, semaforo):
        if semaforo.modo_peatonal:
            semaforo.cambiar_estado(Peatonal())
        else:
            semaforo.cambiar_estado(Verde())


class Peatonal(Estado):
    nombre = "PEATONAL"

    def siguiente(self, semaforo):
        semaforo.cambiar_estado(Verde())


class Verde(Estado):
    nombre = "VERDE"

    def siguiente(self, semaforo):
        semaforo.cambiar_estado(Amarillo())


class Amarillo(Estado):
    nombre = "AMARILLO"

    def siguiente(self, semaforo):
        semaforo.cambiar_estado(Rojo())
