from carga import Carga

class Caja (Carga):
    """
    Modela una caja, como tipo de carga
    """
    
    def __init__(self,contenido : str, peso : float) -> None:
        """
        Inicializa la carga, recibiendo un contenido (descripción)
        y un peso

        :param contenido: Descripción de la carga
        :type contenido: str
        :param peso: Peso de la carga
        :type peso: float
        """
        super().__init__(contenido)
        self._peso = peso

    def peso(self) -> float:
        """
        Retorna el peso de una caja

        :return: Peso de la caja
        :rtype: float
        """
        return self._peso
    
    def __str__(self) -> str:
        aux = super().__str__()
        return f"{aux} (Peso:{self.peso()} kg.)"