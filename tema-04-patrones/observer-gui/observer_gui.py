"""
Patron Observer: lista de precios con varias vistas que se actualizan solas.

Cuando el modelo (ListaPrecios) cambia, notifica a todos los observadores
que se hayan registrado. En esta demo hay TRES vistas distintas sobre el
mismo modelo:

  * VistaGrilla   -> una tabla con los productos y precios.
  * VistaTotales  -> cantidad de productos, total y promedio.
  * VistaAuditoria-> un registro historico de cada cambio.

El modelo no conoce a las vistas: solo conoce la interfaz Observer.
Agregar o quitar una vista no toca al modelo.

Participantes:
  * Observer -> interfaz con update(sujeto).
  * Subject -> mantiene la lista de observadores y los notifica.
  * ListaPrecios -> sujeto concreto; el estado observado son los precios.
  * VistaGrilla / VistaTotales / VistaAuditoria -> observadores concretos.
"""
from abc import ABC, abstractmethod


# --------------------------------------------------------------- Observer
class Observer(ABC):
    @abstractmethod
    def update(self, sujeto):
        """Reacciona al cambio del sujeto."""


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class ListaPrecios(Subject):
    """Sujeto concreto: guarda los precios y avisa cuando cambian."""

    def __init__(self):
        super().__init__()
        self._precios = {}

    def actualizar_precio(self, producto, precio):
        self._precios[producto] = precio
        self.notify()

    def quitar(self, producto):
        if producto in self._precios:
            del self._precios[producto]
            self.notify()

    def obtener_precios(self):
        return dict(self._precios)


# ----------------------------------------------------------- Observadores
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


# ------------------------------------------------------------------- GUI
def construir_ventana():
    import tkinter as tk
    from tkinter import ttk

    raiz = tk.Tk()
    raiz.title("Lista de precios (patron Observer)")

    modelo = ListaPrecios()

    # --- controles para cambiar el modelo ---
    controles = tk.Frame(raiz, padx=10, pady=8)
    controles.pack(fill="x")
    tk.Label(controles, text="Producto:").pack(side="left")
    entrada_producto = tk.Entry(controles, width=12)
    entrada_producto.pack(side="left", padx=4)
    tk.Label(controles, text="Precio:").pack(side="left")
    entrada_precio = tk.Entry(controles, width=8)
    entrada_precio.pack(side="left", padx=4)
    entrada_producto.focus_set()

    def actualizar(_evento=None):
        producto = entrada_producto.get().strip()
        try:
            precio = float(entrada_precio.get())
        except ValueError:
            return
        if producto:
            modelo.actualizar_precio(producto, precio)
            entrada_producto.delete(0, "end")
            entrada_precio.delete(0, "end")
            entrada_producto.focus_set()

    tk.Button(controles, text="Actualizar precio",
              command=actualizar).pack(side="left", padx=6)
    tk.Button(controles, text="Quitar",
              command=lambda: modelo.quitar(entrada_producto.get().strip())
              ).pack(side="left")
    raiz.bind("<Return>", actualizar)

    # --- vista 1: grilla ---
    grilla = ttk.Treeview(raiz, columns=("producto", "precio"),
                          show="headings", height=8)
    grilla.heading("producto", text="Producto")
    grilla.heading("precio", text="Precio")
    grilla.column("producto", width=200)
    grilla.column("precio", width=120, anchor="e")
    grilla.pack(fill="x", padx=10)

    # --- vista 2: totales ---
    etiqueta_totales = tk.Label(raiz, text="", font=("Helvetica", 12, "bold"),
                                fg="#003087")
    etiqueta_totales.pack(pady=8)

    # --- vista 3: auditoria ---
    tk.Label(raiz, text="Auditoria de cambios:").pack(anchor="w", padx=10)
    caja = tk.Text(raiz, height=7, width=54)
    caja.pack(padx=10, pady=(0, 10))

    # --- registro de observadores: el modelo no los conoce de antemano ---
    modelo.attach(VistaGrilla(grilla))
    modelo.attach(VistaTotales(etiqueta_totales))
    modelo.attach(VistaAuditoria(caja))

    # precios iniciales: disparan las tres vistas
    modelo.actualizar_precio("pan", 150)
    modelo.actualizar_precio("leche", 320)
    modelo.actualizar_precio("cafe", 1800)

    return raiz


def demo_consola():
    print("=== Lista de precios (Observer) ===")

    class _Ver(Observer):
        def __init__(self, nombre):
            self.nombre = nombre

        def update(self, sujeto):
            print(f"  [{self.nombre}] precios = {sujeto.obtener_precios()}")

    modelo = ListaPrecios()
    modelo.attach(_Ver("cliente"))
    modelo.attach(_Ver("auditoria"))
    modelo.actualizar_precio("pan", 150)
    modelo.actualizar_precio("leche", 320)


if __name__ == "__main__":
    import sys

    if "--consola" in sys.argv:
        demo_consola()
    else:
        construir_ventana().mainloop()
