class Atencion:
    def __init__(self, codigo, tipo_cobro):
        self.codigo = codigo
        self.tipo_cobro = tipo_cobro

    def importe_a_cobrar(self):
        pass

    def es_medica(self):
        return False