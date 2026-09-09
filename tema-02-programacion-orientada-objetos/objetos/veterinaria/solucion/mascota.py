class Mascota:
    
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        self._edad = valor
        
    def __str__(self) -> str:
        return f"{self.nombre}: {self.edad} años"
