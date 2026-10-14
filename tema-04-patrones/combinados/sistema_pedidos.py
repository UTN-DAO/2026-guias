"""Solución: un mismo sistema combinando State, Strategy, Observer y Facade.

Dominio: pedidos de una distribuidora.

  * State    -> EstadoPedido modela el ciclo de vida del pedido.
  * Strategy -> EstrategiaRecargo calcula el recargo de envio.
  * Observer -> el Pedido (sujeto) avisa a sus vistas al cambiar de estado.
  * Facade   -> FachadaPedidos oculta el subsistema y coordina todo.

Cada patrón se ocupa de un eje de variacion distinto.
"""
from abc import ABC, abstractmethod


# ------------------------------------------------------- Strategy
class EstrategiaRecargo(ABC):
    nombre = ""

    @abstractmethod
    def calcular(self, pedido):
        ...


class RecargoFijo(EstrategiaRecargo):
    nombre = "fijo"

    def calcular(self, pedido):
        return 500.0


class RecargoPorZona(EstrategiaRecargo):
    nombre = "por zona"

    TARIFAS = {"centro": 300.0, "norte": 800.0, "sur": 1200.0}

    def calcular(self, pedido):
        return self.TARIFAS.get(pedido.zona, 1500.0)


# ------------------------------------------------------- Observer
class Observer(ABC):
    @abstractmethod
    def update(self, pedido):
        ...


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Auditoria(Observer):
    def update(self, pedido):
        print(f"      [auditoria] pedido {pedido.id} -> {pedido.estado.nombre}")


class NotificadorCliente(Observer):
    def update(self, pedido):
        print(f"      [mail]      aviso a {pedido.cliente}: "
              f"su pedido esta {pedido.estado.nombre}")


# ------------------------------------------------------- State
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


class Pedido(Subject):
    """Contexto del State y del Strategy, y sujeto del Observer."""

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


# ------------------------------------------------------- Facade
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
