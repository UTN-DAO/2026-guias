from medica import *
from typing import *
from atencion import *


class Hospital:

    def __init__(self, razon_social):
        self.atenciones = []
        self.razon_social = razon_social

    def agregar_atencion(self, atencion):
        self.atenciones.append(atencion)

    def importe_total_atencion_consulta(self):
        # Con comprensión: 
        #return sum([a.importe for a in self.atenciones if a.es_medica()])
        
        # Con programación funcional
        return sum(list(map(lambda a: a.importe, filter(lambda a: a.es_medica(), self.atenciones))))

    def importe_promedio_atenciones(self, desde, hasta):

        # Con compresión
        filtradas = [a.importe_a_cobrar()
                     for a
                     in self.atenciones
                     if a.es_medica()
                     and desde < a.importe_a_cobrar() < hasta]
        # Con programación funcional
        #filtradas = list(map(lambda a: a.importe_a_cobrar(), list(filter(lambda a: a.es_medica() and desde < a.importe_a_cobrar() < hasta, self.atenciones))))
        
        promedio = sum(filtradas) / len(filtradas) if len(filtradas) else 0
        return promedio

    def codigo_primera_atencion_habitual(self):
        encontradas = [a
                       for a
                       in self.atenciones
                       if type(a) == Medica and a.paciente.habitual]

        return encontradas[0].codigo if len(encontradas) else 0
