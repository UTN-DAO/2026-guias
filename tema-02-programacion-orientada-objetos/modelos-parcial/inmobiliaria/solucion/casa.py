from inmueble import Inmueble

class Casa(Inmueble):
    
    def __init__(self, codigo, propietario, superficie, importe_base, dormitorios, tiene_pileta):
        super().__init__(codigo, propietario, superficie, importe_base)
        self.dormitorios = dormitorios
        self.tiene_pileta = tiene_pileta
        
        
    def alquiler(self):
        importe_dormitorios = self.dormitorios * 30000
        importe_pileta = 0
        if self.tiene_pileta: importe_pileta = 100000
        
        return self.importe_base + importe_dormitorios + importe_pileta
    
    
        
        