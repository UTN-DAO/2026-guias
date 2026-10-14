"""Demostración del patrón Observer: lista de precios con varias vistas."""
from observer import Subject, Observer


class ListaPrecios(Subject):
    """Sujeto: guarda los precios y avisa cuando cambian."""

    def __init__(self):
        super().__init__()
        self._precios = {}

    def actualizar(self, producto, precio):
        self._precios[producto] = precio
        self.notify()

    def quitar(self, producto):
        if producto in self._precios:
            del self._precios[producto]
            self.notify()

    def precios(self):
        return dict(self._precios)


class Cliente(Observer):
    def __init__(self, nombre):
        self.nombre = nombre

    def update(self, sujeto):
        print(f"[{self.nombre}] lista actualizada: {sujeto.precios()}")


class Auditoria(Observer):
    def __init__(self):
        self.eventos = []

    def update(self, sujeto):
        self.eventos.append(sujeto.precios())
        print(f"[auditoria] cambio registrado (#{len(self.eventos)})")


def main():
    lista = ListaPrecios()

    cliente1 = Cliente("Martin")
    cliente2 = Cliente("Analia")
    auditoria = Auditoria()

    lista.attach(cliente1)
    lista.attach(cliente2)
    lista.attach(auditoria)

    lista.actualizar("pan", 150)
    lista.actualizar("leche", 320)

    print("\nSe da de baja un observador (Analia):")
    lista.detach(cliente2)
    lista.actualizar("cafe", 1800)


if __name__ == "__main__":
    main()
