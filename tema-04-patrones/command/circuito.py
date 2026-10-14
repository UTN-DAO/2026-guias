"""Dominio del circuito de alta: la solicitud y los receptores.

Los receptores conocen las operaciones concretas; los comandos delegan en
ellos. Este módulo no depende del patrón Command.
"""


class Solicitud:
    def __init__(self, documento, nombre, segmento):
        self.documento = documento
        self.nombre = nombre
        self.segmento = segmento
        self.limite_credito = 0
        self.observaciones = []

    def agregar_observacion(self, texto):
        self.observaciones.append(texto)


class RepositorioClientes:
    def __init__(self):
        self.clientes = []

    def guardar(self, solicitud):
        self.clientes.append(solicitud)


class Notificador:
    def enviar(self, solicitud, mensaje):
        print(f"  [aviso a {solicitud.nombre}] {mensaje}")
