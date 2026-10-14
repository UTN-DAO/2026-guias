"""Estrategias concretas de cálculo de envío (patrón Strategy)."""
from abc import ABC, abstractmethod


class EstrategiaEnvio(ABC):
    nombre = ""

    @abstractmethod
    def calcular(self, paquete):
        """Devuelve el coste del envio para el paquete."""


class EnvioEstandar(EstrategiaEnvio):
    nombre = "Estandar"

    def calcular(self, paquete):
        base, por_kg, por_km = 5.0, 1.0, 0.05
        return round(base + por_kg * paquete.peso + por_km * paquete.distancia, 2)


class EnvioExpreso(EstrategiaEnvio):
    nombre = "Expreso"

    def calcular(self, paquete):
        base, por_kg, por_km = 10.0, 2.0, 0.12
        return round(base + por_kg * paquete.peso + por_km * paquete.distancia, 2)


class TarifaPlana(EstrategiaEnvio):
    nombre = "Tarifa plana"

    def calcular(self, paquete):
        return 9.99
