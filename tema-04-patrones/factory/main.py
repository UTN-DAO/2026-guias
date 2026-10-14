"""Demostración del patrón Factory Method con dos fábricas concretas."""
from random import choice

from factory import Veterinaria, Forrajeria


def main():
    proveedores = [Veterinaria(), Forrajeria()]
    productos = [choice(proveedores).factory_method() for _ in range(10)]

    for producto in productos:
        print(producto)
        print(f"TOTAL: {producto.operation():.2f}")


if __name__ == "__main__":
    main()
