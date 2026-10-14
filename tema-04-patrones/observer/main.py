"""Demostración del patrón Observer: lista de precios con varias vistas."""
from precios import ListaPrecios, Cliente, Auditoria


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
