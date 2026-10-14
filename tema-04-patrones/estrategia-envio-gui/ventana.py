"""Ventana tkinter de la calculadora de envío (la vista).

La ventana es el cliente del patrón: es quien elige la estrategia con los
botones de opción y la inyecta en el contexto.
"""
import tkinter as tk

from estrategias import EnvioEstandar, EnvioExpreso, TarifaPlana
from envio import CalculadorEnvio, Paquete


def construir_ventana():
    estrategias = {
        "Estandar": EnvioEstandar,
        "Expreso": EnvioExpreso,
        "Tarifa plana": TarifaPlana,
    }
    calculador = CalculadorEnvio(EnvioEstandar())

    raiz = tk.Tk()
    raiz.title("Calculo de envio (patron Strategy)")
    raiz.resizable(False, False)

    datos = tk.Frame(raiz, padx=12, pady=12)
    datos.pack()

    tk.Label(datos, text="Peso (kg):").grid(row=0, column=0, sticky="e")
    peso = tk.Entry(datos, width=8)
    peso.insert(0, "2.5")
    peso.grid(row=0, column=1, padx=6, pady=3)

    tk.Label(datos, text="Distancia (km):").grid(row=1, column=0, sticky="e")
    distancia = tk.Entry(datos, width=8)
    distancia.insert(0, "120")
    distancia.grid(row=1, column=1, padx=6, pady=3)

    # --- seleccion de estrategia (la decide el cliente) ---
    grupo = tk.LabelFrame(raiz, text="Estrategia (la elige el cliente)",
                          padx=12, pady=8)
    grupo.pack(fill="x", padx=12)
    seleccion = tk.StringVar(value="Estandar")

    def recalcular(*_):
        # El cliente decide la estrategia y la inyecta en el contexto.
        calculador.set_estrategia(estrategias[seleccion.get()]())
        try:
            paquete = Paquete(float(peso.get()), float(distancia.get()))
        except ValueError:
            resultado.config(text="Ingrese numeros validos")
            return
        total = calculador.calcular(paquete)
        resultado.config(text=f"Total con {calculador.estrategia.nombre}: $ {total:.2f}")

    for nombre in estrategias:
        tk.Radiobutton(grupo, text=nombre, value=nombre, variable=seleccion,
                       command=recalcular).pack(side="left", padx=6)

    resultado = tk.Label(raiz, text="", font=("Helvetica", 14, "bold"),
                         fg="#003087")
    resultado.pack(pady=12)

    peso.bind("<KeyRelease>", recalcular)
    distancia.bind("<KeyRelease>", recalcular)
    recalcular()
    return raiz
