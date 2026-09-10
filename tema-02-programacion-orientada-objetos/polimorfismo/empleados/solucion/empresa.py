from administrativo import Administrativo
from obrero import Obrero
from vendedor import Vendedor



class Empresa:

    def __init__(self):
        self._plantel = {}

    def agregar_empleado(self, nuevo):
        self._plantel[nuevo.legajo] = nuevo

    def cantidad_empleados(self):
        return len(self._plantel)
    
    def total_sueldos(self):
        return sum(map(lambda e: e.neto, self._plantel.values()))
    
    def cantidad_tipo(self):
        c = [0,0,0]
        #c = {Obrero:0, Administrativo:0, Vendedor:0}
        for e in self._plantel.values():
            c[e.tipo-1] += 1

        return c
        
    def buscar_por_legajo(self, buscado):
        return self._plantel.get(buscado)