"""Estrategias de recargo de envío (patrón Strategy)."""
from abc import ABC, abstractmethod


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
