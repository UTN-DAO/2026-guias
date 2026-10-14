"""Sujeto concreto del ejemplo y sus observadores (patrón Observer).

``ListaPrecios`` es el sujeto; ``Cliente`` y ``Auditoria`` son observadores
concretos que reaccionan al cambio del modelo.
"""
from observer import Subject, Observer


class ListaPrecios(Subject):
    """Sujeto: guarda los precios y avisa cuando cambian."""

    def __init__(self):
        super().__init__()
        self._precios = {}

    def actualizar(self, producto, precio):
        self._precios[producto] = precio
        self.notify()

    def quitar(self, producto):
        if producto in self._precios:
            del self._precios[producto]
            self.notify()

    def precios(self):
        return dict(self._precios)


class Cliente(Observer):
    def __init__(self, nombre):
        self.nombre = nombre

    def update(self, sujeto):
        print(f"[{self.nombre}] lista actualizada: {sujeto.precios()}")


class Auditoria(Observer):
    def __init__(self):
        self.eventos = []

    def update(self, sujeto):
        self.eventos.append(sujeto.precios())
        print(f"[auditoria] cambio registrado (#{len(self.eventos)})")
