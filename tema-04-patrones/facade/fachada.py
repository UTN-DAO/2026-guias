"""Patrón Facade: ``FachadaPersonas`` expone el ABM sobre el subsistema.

El cliente usa sólo esta clase: nunca ve SQL, ni ``sqlite3``, ni las clases
del subsistema (que viven en ``subsistema.py``).
"""
from subsistema import ConexionBD, ConstructorSQL, Validador, Auditoria


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

    def historial(self):
        return list(self._auditoria.eventos)
