from carga import Carga

class Packing (Carga):
    """
    Modela un Packing, como tipo de Carga
    """

    def __init__(self,contenido : str, peso_caja : float, cantidad : int, peso_estructura : float) -> None:
        """
        Inicializa la carga, recibiendo un contenido (descripción),
        un peso, una cantidad de cajas y el peso de la estructura

        :param contenido: Descripción de la carga
        :type contenido: str
        :param peso_caja: Peso de cada caja
        :type peso: float
        :param cantidad: Cantidad de cajas
        :type peso: int
        :param peso_estructura: Peso de la estructura
        :type peso: float
        """
        super().__init__(contenido)
        self._peso_caja = peso_caja
        self._cantidad = cantidad
        self._peso_estructura = peso_estructura

    def peso(self) -> float:
        """
        Retorna el peso de un packing

        :return: Peso de la caja
        :rtype: float
        """
        return (self._peso_caja * self._cantidad) + self._peso_estructura
    
    def __str__(self) -> str:
        aux = super().__str__()
        return f"{aux} (Peso total:{self.peso()} kg [{self._peso_caja}x{self._cantidad}+{self._peso_estructura}].)"