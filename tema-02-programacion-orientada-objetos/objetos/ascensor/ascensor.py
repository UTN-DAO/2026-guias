from __future__ import annotations

class Ascensor:
    """
    Representa un ascensor con capacidad máxima y rango de pisos.

    Reglas (según README):
    - ir_a_piso(p) => True si p en [piso_min, piso_max] y se mueve; False si no existe.
    - subir(n):
        * retorna -1 si n <= 0
        * si n > espacio disponible, suben solo las que entran; retorna esa cantidad efectiva
    - bajar(n):
        * retorna -1 si n <= 0
        * si n > personas dentro, bajan todas; retorna cantidad efectiva
    - str(ascensor) informa piso actual y personas dentro.
    """

    def __init__(self, piso_min: int, piso_max: int, capacidad_max: int) -> None:
        if piso_min > piso_max:
            raise ValueError("piso_min no puede ser mayor que piso_max")
        if capacidad_max <= 0:
            raise ValueError("capacidad_max debe ser positiva")
        self._piso_min = int(piso_min)
        self._piso_max = int(piso_max)
        self._capacidad_max = int(capacidad_max)
        # El ascensor siempre arranca en 0 (planta baja)
        if 0 < self._piso_min or 0 > self._piso_max:
            raise ValueError("El piso inicial 0 está fuera del rango permitido")
        self._piso_actual = 0
        self._personas = 0

    @property
    def piso_min(self) -> int:
        return self._piso_min

    @property
    def piso_max(self) -> int:
        return self._piso_max

    @property
    def capacidad_max(self) -> int:
        return self._capacidad_max

    @property
    def piso_actual(self) -> int:
        return self._piso_actual

    @property
    def personas(self) -> int:
        return self._personas

    def ir_a_piso(self, piso_destino: int) -> bool:
        if piso_destino < self._piso_min or piso_destino > self._piso_max:
            return False
        self._piso_actual = int(piso_destino)
        return True

    def subir(self, cantidad: int) -> int:
        if cantidad is None or cantidad <= 0:
            return -1
        espacio_disponible = self._capacidad_max - self._personas
        suben = cantidad if cantidad <= espacio_disponible else espacio_disponible
        self._personas += suben
        return suben

    def bajar(self, cantidad: int) -> int:
        if cantidad is None or cantidad <= 0:
            return -1
        bajan = cantidad if cantidad <= self._personas else self._personas
        self._personas -= bajan
        return bajan

    def __str__(self) -> str:
        return f"Ascensor(piso={self._piso_actual}, personas={self._personas})"
