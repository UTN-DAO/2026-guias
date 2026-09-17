class Carga(object):
    """
    Modela una carga genérica del camión
    """
    
    def __init__(self,contenido : str) -> None:
        """
        Inicializa la carga, recibiendo un contenido (descripción)

        :param contenido: Descripción de la carga
        :type contenido: str
        """
        self._contenido = contenido

    @property
    def contenido(self) -> str:
        """
        Retorna el contenido de una carga cualquiera

        :return: Descripción de la carga
        :rtype: str
        """
        return self._contenido

    @contenido.setter
    def contenido(self,valor):
        self._contenido = valor
    
    def peso() -> None:
        return None

    def __str__(self) -> str:
        return f"Contenido: {self.contenido}"

