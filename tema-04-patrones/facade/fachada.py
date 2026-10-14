"""Solución: patrón Facade sobre un subsistema de persistencia.

Subsistema: conexión, constructor de SQL, validador y auditoría.
Fachada: FachadaPersonas expone la API de ABM (alta, baja, modificar, listar).
Cliente: ServicioPersonas solo conoce la fachada.
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


class FachadaPersonas:
    def __init__(self):
        self._bd = ConexionBD()
        self._sql = ConstructorSQL()
        self._validador = Validador()
        self._auditoria = Auditoria()
        self._iniciar()

    def _iniciar(self):
        self._bd.abrir()
        self._bd.ejecutar(
            "CREATE TABLE personas ("
            "dni TEXT PRIMARY KEY, nombre TEXT, apellido TEXT, edad INTEGER)")

    def alta(self, dni, nombre, apellido, edad):
        self._validador.validar_persona(dni, nombre, apellido, edad)
        sentencia, parametros = self._sql.insert(
            "personas",
            {"dni": dni, "nombre": nombre, "apellido": apellido, "edad": edad})
        self._bd.ejecutar(sentencia, parametros)
        self._auditoria.registrar(f"ALTA dni={dni}")

    def baja(self, dni):
        sentencia, parametros = self._sql.delete("personas", "dni", dni)
        self._bd.ejecutar(sentencia, parametros)
        self._auditoria.registrar(f"BAJA dni={dni}")

    def modificar(self, dni, **cambios):
        if not cambios:
            return
        sentencia, parametros = self._sql.update("personas", cambios, "dni", dni)
        self._bd.ejecutar(sentencia, parametros)
        self._auditoria.registrar(f"MODIFICACION dni={dni}")

    def listar(self):
        return self._bd.consultar(self._sql.select("personas"))


class ServicioPersonas:
    def __init__(self, fachada):
        self._fachada = fachada

    def registrar(self, dni, nombre, apellido, edad):
        self._fachada.alta(dni, nombre, apellido, edad)

    def mostrar(self):
        for fila in self._fachada.listar():
            print("   ", fila)
