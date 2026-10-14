"""Observadores concretos: distintas vistas sobre el mismo modelo.

Las vistas que dibujan en la ventana reciben el widget ya creado; la vista de
consola imprime para el modo sin interfaz. Agregar o quitar una vista no toca
al modelo.
"""
from observer import Observer


class VistaGrilla(Observer):
    def __init__(self, grilla):
        self._grilla = grilla

    def update(self, sujeto):
        self._grilla.delete(*self._grilla.get_children())
        for producto, precio in sorted(sujeto.obtener_precios().items()):
            self._grilla.insert("", "end", values=(producto, f"$ {precio:.2f}"))


class VistaTotales(Observer):
    def __init__(self, etiqueta):
        self._etiqueta = etiqueta

    def update(self, sujeto):
        precios = list(sujeto.obtener_precios().values())
        total = sum(precios)
        promedio = total / len(precios) if precios else 0
        self._etiqueta.config(
            text=f"Productos: {len(precios)}     "
                 f"Total: $ {total:.2f}     Promedio: $ {promedio:.2f}")


class VistaAuditoria(Observer):
    def __init__(self, caja):
        self._caja = caja

    def update(self, sujeto):
        self._caja.insert("end", f"cambio -> {sujeto.obtener_precios()}\n")
        self._caja.see("end")


class VistaConsola(Observer):
    def __init__(self, nombre):
        self.nombre = nombre

    def update(self, sujeto):
        print(f"  [{self.nombre}] precios = {sujeto.obtener_precios()}")
