"""Solución: patrón Observer.

  * Observer -> interfaz con update(sujeto).
  * Subject  -> mantiene la lista de observadores y los notifica.
"""
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, sujeto):
        """Reacciona al cambio del sujeto."""


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)
