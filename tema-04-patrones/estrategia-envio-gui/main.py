"""Cálculo de envío con patrón Strategy: ventana tkinter y modo consola."""
import sys

from estrategias import EnvioEstandar, EnvioExpreso, TarifaPlana
from envio import CalculadorEnvio, Paquete


def demo_consola():
    """Modo sin ventana: muestra como cambia el resultado al cambiar la
    estrategia, sin tocar la clase CalculadorEnvio."""
    paquete = Paquete(2.5, 120)
    calculador = CalculadorEnvio(EnvioEstandar())
    print("=== Calculo de envio (Strategy) ===")
    for estrategia in (EnvioEstandar, EnvioExpreso, TarifaPlana):
        calculador.set_estrategia(estrategia())
        print(f"  {calculador.estrategia.nombre:<12}: $ {calculador.calcular(paquete):.2f}")


def main():
    if "--consola" in sys.argv:
        demo_consola()
    else:
        from ventana import construir_ventana
        construir_ventana().mainloop()


if __name__ == "__main__":
    main()
