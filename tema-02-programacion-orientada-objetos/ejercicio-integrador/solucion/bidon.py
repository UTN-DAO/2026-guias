from carga import Carga

class Bidon (Carga):
    """
    Modela un bidón, como tipo de carga
    """
    
    def __init__(self,contenido : str, capacidad : float, densidad : float) -> None:
        """
        Inicializa la carga, recibiendo un contenido (descripción)
        capacidad del bidon y densidad del líquido

        :param contenido: Descripción de la carga
        :type contenido: str
        :param capacidad: Capacidad del bidón
        :type capacidad: float
        :param densidad: Densidad del líquido
        :type densidad: float
        """
        super().__init__(contenido)
        self._capacidad = capacidad
        self._densidad = densidad

    def peso(self) -> float:
        """
        Retorna el peso de un bidón como capacidad por densidad

        :return: Peso del bidon
        :rtype: float
        """
        return self._capacidad * self._densidad
    
    def __str__(self) -> str:
        aux = super().__str__()
        return f"{aux} (Peso:{self.peso()} kg.)"
