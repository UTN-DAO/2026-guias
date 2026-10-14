"""Facade: coordina pedidos, estrategia y observadores.

Acá está la costura del sistema: la fachada elige la estrategia, conecta los
observadores y valida las entradas. El cliente no ve el subsistema.
"""
from pedidos import Pedido
from estrategias import RecargoFijo, RecargoPorZona


class FachadaPedidos:
    def __init__(self):
        self._pedidos = {}
        self._proximo_id = 1
        self._observers = []

    def suscribir(self, observer):
        self._observers.append(observer)

    def crear_pedido(self, cliente, zona, monto_base):
        if not cliente or monto_base <= 0:
            raise ValueError("datos del pedido invalidos")
        recargo = RecargoPorZona() if zona in RecargoPorZona.TARIFAS else RecargoFijo()
        pedido = Pedido(self._proximo_id, cliente, zona, monto_base, recargo)
        for observer in self._observers:
            pedido.attach(observer)
        self._pedidos[pedido.id] = pedido
        self._proximo_id += 1
        return pedido

    def avanzar(self, id, accion):
        pedido = self._pedidos[id]
        getattr(pedido, accion)()
        return pedido

    def listar(self):
        return list(self._pedidos.values())
