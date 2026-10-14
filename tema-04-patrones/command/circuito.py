"""
Patron Command: circuito de alta de clientes.

Cada paso del proceso de alta es un comando. El invocador (ProcesadorCircuito)
recorre la secuencia y llama a ejecutar() sin conocer los tipos concretos,
delegando el trabajo en los receptores (Solicitud, RepositorioClientes,
Notificador). El armador circuito_para(...) elige los pasos segun el segmento.

Ejecutar: python main.py
"""
from abc import ABC, abstractmethod


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


class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass


class ValidarDocumentacion(Comando):
    def __init__(self, solicitud):
        self._solicitud = solicitud

    def ejecutar(self):
        self._solicitud.agregar_observacion("Documentacion validada")


class VerificarSituacionFiscal(Comando):
    def __init__(self, solicitud):
        self._solicitud = solicitud

    def ejecutar(self):
        self._solicitud.agregar_observacion("Situacion fiscal verificada")


class EvaluarGarantias(Comando):
    def __init__(self, solicitud):
        self._solicitud = solicitud

    def ejecutar(self):
        self._solicitud.agregar_observacion("Garantias evaluadas")


class AsignarLimiteCredito(Comando):
    LIMITES = {"persona": 50000, "pyme": 500000, "corporativo": 5000000}

    def __init__(self, solicitud):
        self._solicitud = solicitud

    def ejecutar(self):
        self._solicitud.limite_credito = self.LIMITES[self._solicitud.segmento]


class RegistrarCliente(Comando):
    def __init__(self, solicitud, repositorio):
        self._solicitud = solicitud
        self._repositorio = repositorio

    def ejecutar(self):
        self._repositorio.guardar(self._solicitud)


class NotificarAlta(Comando):
    def __init__(self, solicitud, notificador):
        self._solicitud = solicitud
        self._notificador = notificador

    def ejecutar(self):
        self._notificador.enviar(
            self._solicitud,
            f"Alta aprobada con limite {self._solicitud.limite_credito}")


class ProcesadorCircuito:
    """Invocador: ejecuta la secuencia y registra cada paso (auditoria)."""

    def __init__(self):
        self.registro = []

    def procesar(self, solicitud, comandos):
        self.registro.append(f"Alta de {solicitud.nombre} ({solicitud.segmento})")
        for comando in comandos:
            comando.ejecutar()
            self.registro.append(f"  paso: {type(comando).__name__}")


def circuito_para(solicitud, repositorio, notificador):
    comandos = [ValidarDocumentacion(solicitud)]
    if solicitud.segmento == "pyme":
        comandos.append(VerificarSituacionFiscal(solicitud))
    elif solicitud.segmento == "corporativo":
        comandos.append(VerificarSituacionFiscal(solicitud))
        comandos.append(EvaluarGarantias(solicitud))
    comandos.append(AsignarLimiteCredito(solicitud))
    comandos.append(RegistrarCliente(solicitud, repositorio))
    comandos.append(NotificarAlta(solicitud, notificador))
    return comandos
