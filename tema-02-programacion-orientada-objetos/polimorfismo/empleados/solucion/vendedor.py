
from empleado import Empleado


class Vendedor(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, ventas):
        super().__init__(legajo, nombre, apellido, basico)
        self._ventas = ventas

    @property
    def ventas(self):
        return self._ventas
    
    @property
    def neto(self):
        return self.basico + (self._ventas * 0.01)

    @property
    def tipo(self):
        return 3

    def __str__(self):
        return super().__str__() + " " + str(self.ventas)
    