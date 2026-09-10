class Empleado:

    def __init__(self, legajo, nombre, apellido, basico):
        self._legajo = legajo
        self._nombre = nombre
        self._apellido = apellido
        self._basico = basico

    @property
    def legajo(self):
        return self._legajo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def basico(self):
        return self._basico
    
    @property
    def neto(self):
        pass

    @property
    def tipo(self):
        return 0
    
    def __str__(self) -> str:
        return f"{self.legajo} {self.nombre} {self.apellido} {self.neto}"
    
        
