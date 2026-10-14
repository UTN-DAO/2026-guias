"""Patrón Singleton: garantiza una única instancia de una clase.

La idea es controlar la creación del objeto desde el propio tipo, de modo que
sucesivas llamadas devuelvan siempre la misma instancia.

* ``Singleton`` -> implementación genérica del patrón.
* ``DBConnection`` -> ejemplo concreto: la conexión a la base es única en todo
  el programa, aunque se pida más de una vez.
"""


class Singleton:
    # Variable de instancia, para contener el objeto.
    _instance = None

    def __new__(cls):
        # Si no está asignado _instance, pedirle al padre (super) que cree un
        # objeto cls; si ya estaba, se reutiliza.
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class DBConnection:
    _instance = None
    dbconnection = None

    def __new__(cls, connection_string):
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls.dbconnection = connection_string
        return cls._instance
