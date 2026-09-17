from casa import Casa
from departamento import Departamento

class Inmobiliaria:
    
    def __init__(self):
        self.inmuebles = []
        
    def agregar(self, inmueble):
        self.inmuebles.append(inmueble)
        
    def suma_alquileres(self):

        return sum(list(map(lambda i: i.alquiler(), self.inmuebles)))
        
    
    def cantidad_casas_premium(self):
        
        c = 0
        for inm in self.inmuebles:
            if isinstance(inm, Casa) and inm.superficie > 150 and inm.dormitorios > 2 and inm.tiene_pileta:
                c += 1
                                
        return c
                
    def propietario_alquiler_mas_bajo(self):
        
        menor = None
        for inm in self.inmuebles:
            if isinstance(inm, Departamento):
                if menor is None or inm.alquiler() < menor.alquiler():
                    menor = inm

        if menor is None: return None
        return menor.propietario
    
    
