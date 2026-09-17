from inmueble import Inmueble

class Departamento(Inmueble):
    
    def __init__(self, codigo, propietario, superficie, importe_base, importe_expensas, piso):
        super().__init__(codigo, propietario, superficie, importe_base)
        self.importe_expensas = importe_expensas
        self.piso = piso
        
        
    def alquiler(self):
        importe_piso = 0
        if self.piso < 3: importe_piso = 20000
        
        return self.importe_base + importe_piso + self.importe_expensas
    
    
    