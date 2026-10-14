"""Patrón Command: cada paso del alta es un objeto comando.

* ``Comando`` -> interfaz con ``ejecutar()``.
* validaciones, asignación de límite, registro y notificación -> comandos
  concretos; cada uno delega en un receptor.
* ``ProcesadorCircuito`` -> invocador: recorre la secuencia sin conocer los
  tipos concretos y deja un registro de auditoría.
* ``circuito_para(...)`` -> arma la secuencia según el segmento del cliente.
"""
from abc import ABC, abstractmethod


class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        ...


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
