"""
Demostracion del patron Strategy para el calculo de envio.
"""
from envios import (CalculadorEnvio, EnvioEstandar, EnvioExpreso,
                    TarifaPlana, EnvioPorVolumen, ESTRATEGIAS, Paquete)


def main():
    paquete = Paquete(peso=2.5, distancia=120)
    calculador = CalculadorEnvio(EnvioEstandar())

    print("=== Con clases ===")
    for estrategia in (EnvioEstandar, EnvioExpreso, TarifaPlana,
                       EnvioPorVolumen):
        calculador.set_estrategia(estrategia())
        print(f"{calculador._estrategia.nombre:<12}: $ {calculador.calcular(paquete):.2f}")

    print("\n=== Con diccionario de funciones ===")
    for nombre, funcion in ESTRATEGIAS.items():
        print(f"{nombre:<12}: $ {funcion(paquete):.2f}")


if __name__ == "__main__":
    main()
