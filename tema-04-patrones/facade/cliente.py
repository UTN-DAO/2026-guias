"""Cliente del patrón: sólo conoce la fachada, nunca el subsistema."""


class ServicioPersonas:
    def __init__(self, fachada):
        self._fachada = fachada

    def registrar(self, dni, nombre, apellido, edad):
        self._fachada.alta(dni, nombre, apellido, edad)

    def mostrar(self):
        for fila in self._fachada.listar():
            print("   ", fila)
