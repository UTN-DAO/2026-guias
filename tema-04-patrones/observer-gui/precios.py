"""Modelo del ejemplo: la lista de precios es el sujeto observado.

El modelo no conoce a las vistas: sólo conoce la interfaz ``Observer``.
"""
from observer import Subject


class ListaPrecios(Subject):
    """Sujeto concreto: guarda los precios y avisa cuando cambian."""

    def __init__(self):
        super().__init__()
        self._precios = {}

    def actualizar_precio(self, producto, precio):
        self._precios[producto] = precio
        self.notify()

    def quitar(self, producto):
        if producto in self._precios:
            del self._precios[producto]
            self.notify()

    def obtener_precios(self):
        return dict(self._precios)
