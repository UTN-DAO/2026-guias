"""Pedido: contexto del State y del Strategy, y sujeto del Observer.

El pedido delega el estado en los objetos ``EstadoPedido``, el recargo en la
estrategia que se le inyecta, y avisa a sus observadores al cambiar de estado.
"""
from observadores import Subject
from estados import Nuevo


class Pedido(Subject):
    def __init__(self, id, cliente, zona, monto_base, recargo):
        super().__init__()
        self.id = id
        self.cliente = cliente
        self.zona = zona
        self.monto_base = monto_base
        self.recargo = recargo
        self.estado = Nuevo()

    def cambiar_estado(self, estado):
        self.estado = estado
        self.notify()

    def confirmar(self):
        self.estado.confirmar(self)

    def entregar(self):
        self.estado.entregar(self)

    def cancelar(self):
        self.estado.cancelar(self)

    def total(self):
        return self.monto_base + self.recargo.calcular(self)
