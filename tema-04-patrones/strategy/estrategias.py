"""Estrategias concretas de cálculo de envío (patrón Strategy).

Incluye una variante sin herencia: un diccionario que asocia el nombre de la
estrategia con la función que la calcula.
"""
from abc import ABC, abstractmethod


class EstrategiaEnvio(ABC):
    nombre = ""

    @abstractmethod
    def calcular(self, paquete):
        ...


class EnvioEstandar(EstrategiaEnvio):
    nombre = "Estandar"

    def calcular(self, paquete):
        return round(5.0 + 1.0 * paquete.peso + 0.05 * paquete.distancia, 2)


class EnvioExpreso(EstrategiaEnvio):
    nombre = "Expreso"

    def calcular(self, paquete):
        return round(10.0 + 2.0 * paquete.peso + 0.12 * paquete.distancia, 2)


class TarifaPlana(EstrategiaEnvio):
    nombre = "Tarifa plana"

    def calcular(self, paquete):
        return 9.99


class EnvioPorVolumen(EstrategiaEnvio):
    nombre = "Por volumen"

    def calcular(self, paquete):
        volumen = paquete.peso * 100
        return round(3.0 + 0.02 * volumen + 0.03 * paquete.distancia, 2)


def estandar_fn(paquete):
    return round(5.0 + 1.0 * paquete.peso + 0.05 * paquete.distancia, 2)


def expreso_fn(paquete):
    return round(10.0 + 2.0 * paquete.peso + 0.12 * paquete.distancia, 2)


ESTRATEGIAS = {
    "estandar": estandar_fn,
    "expreso": expreso_fn,
    "plana": lambda paquete: 9.99,
}
