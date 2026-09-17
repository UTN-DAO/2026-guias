from atencion import *


class Farmacia(Atencion):

    def __init__(self, codigo, tipo_pago, importe_total, cupon_descuento):
        super().__init__(codigo, tipo_pago)
        self.importe_total = importe_total
        self.cupon_descuento = cupon_descuento

    def importe_a_cobrar(self):
        importe = self.importe_total - self.cupon_descuento
        importe *= 1.3 if self.tipo_cobro == 2 else 0.95

