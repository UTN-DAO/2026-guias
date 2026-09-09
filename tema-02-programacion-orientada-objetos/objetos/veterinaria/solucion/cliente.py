
class Cliente:
    
    def __init__(self, numero, nombre, antiguedad, mascota):
        self._numero = numero
        self._nombre = nombre
        self._antiguedad = antiguedad
        self._mascota = mascota


    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, valor):
        self._numero = valor
       
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        
    @property
    def antiguedad(self):
        return self._antiguedad
    
    @antiguedad.setter
    def antiguedad(self, valor):
        self._numero = valor
        
    @property
    def mascota(self):
        return self._mascota
    
    # Sin setter para mascota para que no se cambie
    # el objeto mascota después de la construcción
    
    def __str__(self) -> str:
        return f"Cliente Nro. {self._numero}: {self._nombre} - " \
            f"{self._antiguedad} años - Mascota: {self._mascota}"
