from factory import Factory, Product
from random import choice, randint, random

class Veterinaria (Factory):
    def factory_method(self):
        nombres = ("Boby","Batuque","Sultan","Michifus","Rosalía")
        return Mascota(choice(nombres),randint(1,10),random()*10000)

class Forrajeria (Factory):
    def factory_method(self):
        nombres = ("Royal Canin","KMeal","Wiskas","Suelto","Ravioles")
        return Alimento(choice(nombres),randint(2,10),random()*8000)

class Mascota(Product):
    def __init__(self, nombre : str, cantidad : int, precio : float):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):
        return f"Mascota: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
    def operation (self):
        return self.cantidad*self.precio

class Alimento(Product):
    def __init__(self, nombre : str, cantidad : int, precio : float):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):
        return f"Alimento: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"
    def operation (self):
        return self.cantidad*self.precio

proveedores = [Veterinaria(),Forrajeria()]
productos = []
for i in range (10):
    producto = choice(proveedores).factory_method ()
    productos.append(producto)
for producto in productos:
    print (producto)
    print (f"TOTAL: {producto.operation():.2f}")
