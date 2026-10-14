"""Ventana tkinter de la lista de precios (la vista).

Registra tres vistas distintas sobre el mismo modelo. El modelo no las conoce.
"""
import tkinter as tk
from tkinter import ttk

from precios import ListaPrecios
from vistas import VistaGrilla, VistaTotales, VistaAuditoria


def construir_ventana():
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
