"""Demostración del patrón Strategy para el cálculo de envío.

El cliente decide la estrategia y la inyecta en el contexto, que sólo delega.
"""
from envio import CalculadorEnvio, Paquete
from estrategias import (EnvioEstandar, EnvioExpreso, TarifaPlana,
                         EnvioPorVolumen, ESTRATEGIAS)


def main():
    paquete = Paquete(peso=2.5, distancia=120)
    calculador = CalculadorEnvio(EnvioEstandar())

    print("=== Con clases ===")
    for estrategia in (EnvioEstandar, EnvioExpreso, TarifaPlana,
                       EnvioPorVolumen):
        calculador.set_estrategia(estrategia())
        print(f"{calculador.estrategia.nombre:<12}: $ {calculador.calcular(paquete):.2f}")

    print("\n=== Con diccionario de funciones ===")
    for nombre, funcion in ESTRATEGIAS.items():
        print(f"{nombre:<12}: $ {funcion(paquete):.2f}")


if __name__ == "__main__":
    main()
