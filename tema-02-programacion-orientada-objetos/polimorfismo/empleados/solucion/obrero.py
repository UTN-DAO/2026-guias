
from empleado import Empleado


class Obrero(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, dias):
        super().__init__(legajo, nombre, apellido, basico)
        self._dias = dias

    @property
    def dias(self):
        return self._dias
    
    @property
    def neto(self):
        return self.basico / 22 * self._dias

    @property
    def tipo(self):
        return 1
    
    def __str__(self):
        return super().__str__() + " " + str(self.dias)    
    