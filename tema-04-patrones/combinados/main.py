"""Demostración: State + Strategy + Observer bajo una fachada."""
from fachada import FachadaPedidos
from observadores import Auditoria, NotificadorCliente
from estados import TransicionInvalida


def mostrar(fachada):
    for pedido in fachada.listar():
        print(f"   #{pedido.id} {pedido.cliente:<6} {pedido.estado.nombre:<11} "
              f"recargo {pedido.recargo.nombre:<8} total $ {pedido.total():.2f}")


def main():
    fachada = FachadaPedidos()
    fachada.suscribir(Auditoria())
    fachada.suscribir(NotificadorCliente())

    print("Altas:")
    fachada.crear_pedido("Ana", "centro", 1000)
    fachada.crear_pedido("Beto", "sur", 2500)
    fachada.crear_pedido("Caro", "islas", 800)

    print("\nCiclo del pedido 1:")
    fachada.avanzar(1, "confirmar")
    fachada.avanzar(1, "entregar")

    print("\nTransicion invalida:")
    try:
        fachada.avanzar(1, "entregar")
    except TransicionInvalida as error:
        print(f"      [rechazado] {error}")

    print("\nEstado final:")
    mostrar(fachada)


if __name__ == "__main__":
    main()
