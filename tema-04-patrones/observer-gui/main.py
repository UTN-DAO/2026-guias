"""Lista de precios con patrón Observer: ventana tkinter y modo consola."""
import sys

from precios import ListaPrecios
from vistas import VistaConsola


def demo_consola():
    print("=== Lista de precios (Observer) ===")
    modelo = ListaPrecios()
    modelo.attach(VistaConsola("cliente"))
    modelo.attach(VistaConsola("auditoria"))
    modelo.actualizar_precio("pan", 150)
    modelo.actualizar_precio("leche", 320)


def main():
    if "--consola" in sys.argv:
        demo_consola()
    else:
        from ventana import construir_ventana
        construir_ventana().mainloop()


if __name__ == "__main__":
    main()
