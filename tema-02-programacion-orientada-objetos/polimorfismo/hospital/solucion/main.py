from hospital import *
from medica import *
from paciente import *

if __name__ == '__main__':

    h = Hospital("Privado")

    h.agregar_atencion(Medica(1, 1, Paciente("Juan", "fiebre", False), 5000))

    print(h.importe_promedio_atenciones(1,10000))
    print(h.codigo_primera_atencion_habitual())
    print(h.importe_total_atencion_consulta())
