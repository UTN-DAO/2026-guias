"""Semáforo con patrón State: ventana tkinter y modo consola."""
import sys

from semaforo import Semaforo


def demo_consola(transiciones=7):
    """Modo sin ventana: recorre el semáforo e imprime la secuencia."""
    semaforo = Semaforo()
    print("=== Semaforo (State), modo consola ===")
    for _ in range(transiciones):
        print(f"Estado actual: {semaforo.actual()}")
        semaforo.siguiente()


def main():
    if "--consola" in sys.argv:
        demo_consola()
    else:
        from ventana import construir_ventana
        construir_ventana().mainloop()


if __name__ == "__main__":
    main()
