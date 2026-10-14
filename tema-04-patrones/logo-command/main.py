"""Intérprete LOGO con patrón Command: ventana tkinter y modo consola."""
import sys

from comandos import Programa
from parser import compilar
from programas import EJEMPLO
from tortuga import Tortuga


def demo_consola(programa=None):
    codigo = programa or EJEMPLO
    comandos = compilar(codigo)
    tortuga = Tortuga()
    invocador = Programa(comandos)
    invocador.ejecutar(tortuga)
    print("=== Interprete LOGO (Command) ===")
    print("Comandos de nivel superior:", invocador.descripcion())
    print(f"Trazos dibujados: {len(tortuga.trazos)}")
    print(f"Posicion final: ({tortuga.x:.1f}, {tortuga.y:.1f}), color {tortuga.color}")


def main():
    if "--consola" in sys.argv:
        resto = [a for a in sys.argv[1:] if a != "--consola"]
        demo_consola(" ".join(resto) if resto else None)
    else:
        from ventana import construir_ventana
        construir_ventana().mainloop()


if __name__ == "__main__":
    main()
