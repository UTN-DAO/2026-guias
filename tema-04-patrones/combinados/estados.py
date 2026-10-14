"""State: ciclo de vida de un pedido.

Cada estado conoce qué acciones acepta y a qué estado se pasa; las
transiciones inválidas se rechazan con ``TransicionInvalida``.
"""
from abc import ABC


class TransicionInvalida(Exception):
    pass


class EstadoPedido(ABC):
    nombre = ""

    def _invalida(self, accion):
        raise TransicionInvalida(
            f"no se puede {accion} un pedido {self.nombre}")

    def confirmar(self, pedido):
        self._invalida("confirmar")

    def entregar(self, pedido):
        self._invalida("entregar")

    def cancelar(self, pedido):
        self._invalida("cancelar")


class Nuevo(EstadoPedido):
    nombre = "Nuevo"

    def confirmar(self, pedido):
        pedido.cambiar_estado(Confirmado())

    def cancelar(self, pedido):
        pedido.cambiar_estado(Cancelado())


class Confirmado(EstadoPedido):
    nombre = "Confirmado"

    def entregar(self, pedido):
        pedido.cambiar_estado(Entregado())

    def cancelar(self, pedido):
        pedido.cambiar_estado(Cancelado())


class Entregado(EstadoPedido):
    nombre = "Entregado"


class Cancelado(EstadoPedido):
    nombre = "Cancelado"
