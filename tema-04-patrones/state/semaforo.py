"""
Patron State: semaforo con modo peatonal.

El semaforo tiene cuatro estados: Rojo, Peatonal, Verde y Amarillo.
Cuando el modo peatonal esta activado, la transicion desde Rojo pasa
primero por Peatonal (habilitando el cruce) y luego continua el ciclo
vehicular.

Ejecutar: python main.py
"""
from abc import ABC, abstractmethod


class Estado(ABC):
    nombre = ""

    @abstractmethod
    def siguiente(self, semaforo):
        pass


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
