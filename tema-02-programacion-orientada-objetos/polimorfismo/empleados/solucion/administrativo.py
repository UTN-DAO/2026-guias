
from empleado import Empleado


class Administrativo(Empleado):
    def __init__(self, legajo, nombre, apellido, basico, presentismo):
        super().__init__(legajo, nombre, apellido, basico)
        self._presentismo = presentismo

    @property
    def presentismo(self):
        return self._presentismo
    
    @property
    def neto(self):
        return self.basico * (1.13 if self._presentismo else 1)

    @property
    def tipo(self):
        return 2
    
    def __str__(self):
        return super().__str__() + " " + str(self.presentismo)
    