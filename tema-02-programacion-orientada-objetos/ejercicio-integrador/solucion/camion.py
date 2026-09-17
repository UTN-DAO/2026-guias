from carga import Carga
from functools import reduce
import random

ESTADO_CAMION = ('LIBRE','EN VIAJE', 'EN_REPARACION')

class Camion:
    
    def __init__(self, patente: str, carga_maxima: float) -> None:
        self._patente = patente
        self._estado = 'LIBRE'
        self._carga_maxima = carga_maxima
        self._cargas = []

    def __str__(self) -> str:
        aux = f"{'='*40}\nPATENTE: {self._patente}, ESTADO: {self._estado}\nCARGA MÁXIMA: {self.carga_maxima}\n"
        aux += f"{'-'*40}\n"
        aux += f"CANTIDAD DE CARGAS: {self.cantidad_cargas}, PESO DE CARGAS: {self.peso_cargas}\n"
        aux += f"{'-'*40}\n"
        aux += f"CARGAS:\n"
        for carga in self._cargas:
            aux += str(carga)+"\n"
        aux += f"{'='*40}"
        return aux

    @property
    def carga_maxima(self) -> float:
        return self._carga_maxima

    @property
    def cantidad_cargas(self) -> int:
        return len(self._cargas)
    
    def subir_carga(self, carga: Carga) -> None:
        if (self.peso_cargas+carga.peso()) < self._carga_maxima:
            self._cargas.append(carga)
        else:
            raise ValueError("El peso supera la carga máxima")

    def bajar_carga(self, carga: Carga) -> None:
        self._cargas.remove(carga)

    @property
    def peso_cargas(self) -> float:
        peso_aux = 0
        for carga in self._cargas:
            peso_aux += carga.peso()
        return peso_aux
        # Tambien se podría plantear con reduce por comprensión

    def en_viaje(self) -> None:
        """
        Cambia el estado del camión a "EN VIAJE"
        verificando si está en condiciones
        Debe verificar que la carga esté en no menos
        del 75% del máximo
        """
        if (self.peso_cargas >= self._carga_maxima*0.75) and (self._estado == "LIBRE"):
            self._estado = "EN VIAJE"
        else:
            raise ValueError("El camion no está suficientemente cargado o no está en estado 'LIBRE'")
        
    def libre(self) -> None:
        self._estado = "LIBRE"

    def en_reparacion(self) -> None:
        if (self._estado == 'LIBRE') and (self.cantidad_cargas() == 0):
            self._estado = 'EN REPARACION'
        else:
            raise ValueError (f"El camión no se encuentra LIBRE o aún está cargado ({self.cantidad_cargas()} cargas.)")

    def vaciar_carga(self) -> None:
        self._cargas.clear()

