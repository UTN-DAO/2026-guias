"""
Patron Strategy: calculadora de coste de envio con interfaz tkinter.

Participantes:
  * EstrategiaEnvio -> interfaz con calcular(paquete).
  * EnvioEstandar, EnvioExpreso, TarifaPlana -> estrategias concretas.
  * CalculadorEnvio -> contexto que delega el calculo en la estrategia.
  * La ventana -> cliente. El cliente ES quien elige la estrategia
    (con los botones de opcion) y la inyecta en el contexto.

Contraste con State: aca el cliente decide que algoritmo usar; el
contexto no cambia de estrategia por si mismo.
"""
from abc import ABC, abstractmethod


# ------------------------------------------------------------- Estrategias
class EstrategiaEnvio(ABC):
    nombre = ""

    @abstractmethod
    def calcular(self, paquete):
        """Devuelve el coste del envio para el paquete."""


class Paquete:
    def __init__(self, peso_kg, distancia_km):
        self.peso = peso_kg
        self.distancia = distancia_km


class EnvioEstandar(EstrategiaEnvio):
    nombre = "Estandar"

    def calcular(self, paquete):
        base, por_kg, por_km = 5.0, 1.0, 0.05
        return round(base + por_kg * paquete.peso + por_km * paquete.distancia, 2)


class EnvioExpreso(EstrategiaEnvio):
    nombre = "Expreso"

    def calcular(self, paquete):
        base, por_kg, por_km = 10.0, 2.0, 0.12
        return round(base + por_kg * paquete.peso + por_km * paquete.distancia, 2)


class TarifaPlana(EstrategiaEnvio):
    nombre = "Tarifa plana"

    def calcular(self, paquete):
        return 9.99


# --------------------------------------------------------------- Contexto
class CalculadorEnvio:
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia):
        self._estrategia = estrategia

    @property
    def estrategia(self):
        return self._estrategia

    def calcular(self, paquete):
        return self._estrategia.calcular(paquete)


# ------------------------------------------------------------------- GUI
def construir_ventana():
    import tkinter as tk

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


def demo_consola():
    """Modo sin ventana: muestra como cambia el resultado al cambiar la
    estrategia, sin tocar la clase CalculadorEnvio."""
    paquete = Paquete(2.5, 120)
    calculador = CalculadorEnvio(EnvioEstandar())
    print("=== Calculo de envio (Strategy) ===")
    for estrategia in (EnvioEstandar, EnvioExpreso, TarifaPlana):
        calculador.set_estrategia(estrategia())
        print(f"  {calculador.estrategia.nombre:<12}: $ {calculador.calcular(paquete):.2f}")


if __name__ == "__main__":
    import sys

    if "--consola" in sys.argv:
        demo_consola()
    else:
        construir_ventana().mainloop()
