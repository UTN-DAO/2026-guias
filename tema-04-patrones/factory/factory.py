"""Patrón Factory Method: delega la creación del producto en las subclases.

* ``Factory`` / ``Product`` -> interfaces del creador y del producto.
* ``ConcreteFactory`` / ``ConcreteProduct`` -> versión mínima del libro.
* ``Veterinaria`` / ``Forrajeria`` -> fábricas concretas del dominio.
* ``Mascota`` / ``Alimento`` -> productos concretos.
"""
from abc import ABC, abstractmethod
from random import choice, randint, random


class Factory(ABC):
    @abstractmethod
    def factory_method(self):
        ...


class Product(ABC):
    @abstractmethod
    def operation(self):
        ...


class ConcreteFactory(Factory):
    def factory_method(self):
        return ConcreteProduct()


class ConcreteProduct(Product):
    def operation(self):
        return "Product operation"


class Veterinaria(Factory):
    def factory_method(self):
        nombres = ("Boby", "Batuque", "Sultan", "Michifus", "Rosalía")
        return Mascota(choice(nombres), randint(1, 10), random() * 10000)


class Forrajeria(Factory):
    def factory_method(self):
        nombres = ("Royal Canin", "KMeal", "Wiskas", "Suelto", "Ravioles")
        return Alimento(choice(nombres), randint(2, 10), random() * 8000)


class Mascota(Product):
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Mascota: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def operation(self):
        return self.cantidad * self.precio


class Alimento(Product):
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Alimento: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

    def operation(self):
        return self.cantidad * self.precio
