"""Subsistema de persistencia que la fachada oculta al cliente.

* ``ConexionBD`` -> abre/cierra la conexión y ejecuta sentencias.
* ``ConstructorSQL`` -> arma las sentencias INSERT/UPDATE/DELETE/SELECT.
* ``Validador`` -> reglas de negocio.
* ``Auditoria`` -> registra cada operación.
"""
import sqlite3


class ConexionBD:
    def __init__(self, ruta=":memory:"):
        self._ruta = ruta
        self._conexion = None

    def abrir(self):
        self._conexion = sqlite3.connect(self._ruta)

    def ejecutar(self, sql, parametros=()):
        cursor = self._conexion.cursor()
        cursor.execute(sql, parametros)
        self._conexion.commit()
        return cursor

    def consultar(self, sql, parametros=()):
        cursor = self._conexion.cursor()
        cursor.execute(sql, parametros)
        return cursor.fetchall()

    def cerrar(self):
        if self._conexion is not None:
            self._conexion.close()


class ConstructorSQL:
    def insert(self, tabla, datos):
        columnas = ", ".join(datos.keys())
        marcas = ", ".join(["?"] * len(datos))
        return f"INSERT INTO {tabla} ({columnas}) VALUES ({marcas})", tuple(datos.values())

    def update(self, tabla, cambios, clave, valor):
        asignaciones = ", ".join(f"{c} = ?" for c in cambios)
        return f"UPDATE {tabla} SET {asignaciones} WHERE {clave} = ?", (*cambios.values(), valor)

    def delete(self, tabla, clave, valor):
        return f"DELETE FROM {tabla} WHERE {clave} = ?", (valor,)

    def select(self, tabla):
        return f"SELECT * FROM {tabla} ORDER BY dni"


class Validador:
    def validar_persona(self, dni, nombre, apellido, edad):
        if not dni or not nombre or not apellido:
            raise ValueError("Todos los campos son obligatorios")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")


class Auditoria:
    def __init__(self):
        self.eventos = []

    def registrar(self, mensaje):
        self.eventos.append(mensaje)
