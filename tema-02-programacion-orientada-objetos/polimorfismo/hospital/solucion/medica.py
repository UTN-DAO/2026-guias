from atencion import *
from paciente import *


class Medica(Atencion):

    def __init__(self, codigo, tipo_cobro, paciente, importe):
        super().__init__(codigo, tipo_cobro)
        self.paciente = paciente
        self.importe = importe

    def importe_a_cobrar(self):
        importe = self.importe
        if self.paciente.habitual:
            importe *= .75
        importe *= 1.2 if self.tipo_cobro == 2 else .9
        return importe

    def es_medica(self):
        return True

