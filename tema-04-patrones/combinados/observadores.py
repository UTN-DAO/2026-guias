"""Observer: el sujeto avisa a sus observadores cuando cambia de estado.

``Auditoria`` y ``NotificadorCliente`` son observadores concretos del dominio
de pedidos.
"""
from abc import ABC, abstractmethod


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
