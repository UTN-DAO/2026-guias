"""Patrón Command: cada instrucción LOGO es un objeto comando.

* ``Comando`` -> interfaz con ``ejecutar(tortuga)``.
* ``Avanzar``, ``Retroceder``, ``GirarDerecha``, ``GirarIzquierda``,
  ``Levantar``, ``Bajar``, ``CambiarColor`` -> comandos concretos.
* ``Repetir`` -> comando COMPUESTO: contiene otros comandos.
* ``Programa`` -> invocador: mantiene y ejecuta la secuencia de comandos.

Como los comandos son objetos, se pueden guardar (historial), descartar
(deshacer) y volver a ejecutar (repetición).
"""
from abc import ABC, abstractmethod


class Comando(ABC):
    @abstractmethod
    def ejecutar(self, tortuga):
        """Realiza la operacion sobre el receptor."""

    def descripcion(self):
        return type(self).__name__


class Avanzar(Comando):
    def __init__(self, distancia):
        self.distancia = distancia

    def ejecutar(self, tortuga):
        tortuga.avanzar(self.distancia)

    def descripcion(self):
        return f"Avanzar({self.distancia})"


class Retroceder(Comando):
    def __init__(self, distancia):
        self.distancia = distancia

    def ejecutar(self, tortuga):
        tortuga.avanzar(-self.distancia)

    def descripcion(self):
        return f"Retroceder({self.distancia})"


class GirarDerecha(Comando):
    def __init__(self, grados):
        self.grados = grados

    def ejecutar(self, tortuga):
        tortuga.girar(self.grados)

    def descripcion(self):
        return f"GirarDerecha({self.grados})"


class GirarIzquierda(Comando):
    def __init__(self, grados):
        self.grados = grados

    def ejecutar(self, tortuga):
        tortuga.girar(-self.grados)

    def descripcion(self):
        return f"GirarIzquierda({self.grados})"


class Levantar(Comando):
    def ejecutar(self, tortuga):
        tortuga.levantar()


class Bajar(Comando):
    def ejecutar(self, tortuga):
        tortuga.bajar()


class CambiarColor(Comando):
    def __init__(self, color):
        self.color = color

    def ejecutar(self, tortuga):
        tortuga.cambiar_color(self.color)

    def descripcion(self):
        return f"CambiarColor({self.color})"


class Repetir(Comando):
    """Comando compuesto: ejecuta una secuencia de comandos varias veces."""

    def __init__(self, veces, comandos):
        self.veces = veces
        self.comandos = comandos

    def ejecutar(self, tortuga):
        for _ in range(self.veces):
            for comando in self.comandos:
                comando.ejecutar(tortuga)

    def descripcion(self):
        return f"Repetir({self.veces}, {len(self.comandos)} comandos)"


class Programa:
    """Invocador: mantiene una secuencia de comandos y la ejecuta."""

    def __init__(self, comandos=None):
        self.comandos = list(comandos or [])

    def agregar(self, comando):
        self.comandos.append(comando)

    def deshacer(self):
        return self.comandos.pop() if self.comandos else None

    def ejecutar(self, tortuga):
        for comando in self.comandos:
            comando.ejecutar(tortuga)

    def descripcion(self):
        return [comando.descripcion() for comando in self.comandos]
