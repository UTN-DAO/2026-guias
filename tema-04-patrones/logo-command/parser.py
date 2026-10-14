"""Parser del lenguaje LOGO: convierte el texto en objetos comando.

El parser no conoce el dibujo: sólo arma la lista de comandos que después
ejecuta el invocador.
"""
from comandos import (Avanzar, Retroceder, GirarDerecha, GirarIzquierda,
                      Levantar, Bajar, CambiarColor, Repetir)

COLORES = {
    "negro": "black", "rojo": "red", "verde": "green", "azul": "blue",
    "naranja": "orange", "violeta": "purple", "amarillo": "gold",
    "celeste": "deepskyblue", "rosa": "hotpink", "gris": "gray",
}


class ErrorLOGO(Exception):
    """Error de sintaxis o de colores en un programa LOGO."""


def tokenizar(texto):
    texto = texto.replace("[", " [ ").replace("]", " ] ").replace(",", " ")
    return texto.split()


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def mirar(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self):
        token = self.mirar()
        self.pos += 1
        return token

    def numero(self):
        token = self.consumir()
        if token is None:
            raise ErrorLOGO("Se esperaba un numero y el programa termino")
        try:
            return float(token)
        except ValueError:
            raise ErrorLOGO(f"Se esperaba un numero, no '{token}'")

    def esperar(self, simbolo):
        token = self.consumir()
        if token != simbolo:
            raise ErrorLOGO(f"Se esperaba '{simbolo}', no '{token}'")

    def parsear(self):
        comandos = []
        while self.mirar() is not None:
            comandos.append(self.parsear_comando())
        return comandos

    def parsear_comando(self):
        token = self.consumir()
        instruccion = token.upper()

        if instruccion == "AVANZA":
            return Avanzar(self.numero())
        if instruccion == "RETROCEDE":
            return Retroceder(self.numero())
        if instruccion == "GIRADERECHA":
            return GirarDerecha(self.numero())
        if instruccion == "GIRAIZQUIERDA":
            return GirarIzquierda(self.numero())
        if instruccion == "LEVANTA":
            return Levantar()
        if instruccion == "BAJA":
            return Bajar()
        if instruccion == "COLOR":
            return CambiarColor(self.color())
        if instruccion == "REPITE":
            veces = int(self.numero())
            self.esperar("[")
            cuerpo = []
            while self.mirar() != "]":
                if self.mirar() is None:
                    raise ErrorLOGO("Falta cerrar el bloque con ']'")
                cuerpo.append(self.parsear_comando())
            self.consumir()      # consume ']'
            return Repetir(veces, cuerpo)

        raise ErrorLOGO(f"Instruccion desconocida: '{token}'")

    def color(self):
        token = self.consumir()
        if token is None:
            raise ErrorLOGO("Falta el nombre del color")
        clave = token.lower()
        if clave not in COLORES:
            validos = ", ".join(sorted(COLORES))
            raise ErrorLOGO(f"Color '{token}' no valido. Opciones: {validos}")
        return COLORES[clave]


def compilar(texto):
    """Convierte el texto del programa en una lista de comandos."""
    return Parser(tokenizar(texto)).parsear()
