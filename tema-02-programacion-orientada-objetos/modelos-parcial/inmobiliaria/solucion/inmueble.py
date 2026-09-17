from abc import ABC, abstractmethod

class Inmueble(ABC):
    
    def __init__(self, codigo, propietario, superficie, importe_base):
        self.codigo = codigo
        self.propietario = propietario
        self.superficie = superficie
        self.importe_base = importe_base
        
        
    @abstractmethod
    def alquiler(self):
        pass
            
        
    