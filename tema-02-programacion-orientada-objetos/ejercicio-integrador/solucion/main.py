import rich
from rich.console import Console
from rich.panel import Panel
import random
#from carga import Carga
from caja import Caja
from packing import Packing
from bidon import Bidon
from camion import Camion


def cargar_desde_csv(camion : Camion) -> None:
    select = (True,False)
    # Cargar Cajas
    m = open("Cajas.csv","rt")
    m.readline() # Descartar la linea de titulos
    for linea in m:
        if random.choice(select):   # Utilizado leer una muestra, lee "algunos" registros
            fields = linea.split(",")
            caja = Caja(fields[0],int(fields[1]))
            try:
                camion.subir_carga(caja)
            except ValueError as e:
                print (f"No se pudo cargar {caja}. Supera el peso máximo. Disponible: {camion.carga_maxima-camion.peso_cargas:.2f}")
    m.close()

    # Cargar Packing
    m = open("Packing.csv","rt")
    m.readline() # Descartar la linea de titulos
    for linea in m:
        if random.choice(select):   # Utilizado leer una muestra, lee "algunos" registros
            fields = linea.split(",")
            packing = Packing(fields[0],float(fields[1]),float(fields[2]),float(fields[3]))
            try:
                camion.subir_carga(packing)
            except ValueError as e:
                print (f"No se pudo cargar {packing}. Supera el peso máximo. Disponible: {camion.carga_maxima-camion.peso_cargas:.2f}")
    m.close()

    # Cargar Bidones
    m = open("Bidones.csv","rt")
    m.readline() # Descartar la linea de titulos
    for linea in m:
        if random.choice(select):   # Utilizado leer una muestra, lee "algunos" registros
            fields = linea.split(",")
            bidon = Bidon(fields[0],float(fields[2]),float(fields[1]))
            try:
                camion.subir_carga(bidon)
            except ValueError as e:
                print (f"No se pudo cargar {bidon}. Supera el peso máximo. Disponible: {camion.carga_maxima-camion.peso_cargas:.2f}")
    m.close()


def main():

    camion = Camion('KMS851', 200)
    camion.vaciar_carga()    # Borrar todas las cargas que hubiera
    cargar_desde_csv(camion)
    print(camion)


if __name__ == "__main__":
    main()