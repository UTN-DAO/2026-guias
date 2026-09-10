from obrero import Obrero
from administrativo import Administrativo
from vendedor import Vendedor
from empresa import Empresa


class Lector:
    
    @staticmethod
    def leer_empleados(nombre_archivo, empresa: Empresa):
        
        archivo = open(nombre_archivo)
        for linea in archivo.readlines():
            valores = linea.split(";")
            tipo = int(valores[0])
            legajo = int(valores[1])
            nombre = valores[2]
            apellido = valores[3]
            basico = float(valores[4])

            if tipo == 1:
                dias = int(valores[5])
                nuevo = Obrero(legajo, nombre, apellido, basico, dias)
            elif tipo == 2:
                presentismo = valores[5] == "true"
                nuevo = Administrativo(legajo, nombre, apellido, basico, presentismo)
            elif tipo == 3:
                ventas = float(valores[5])
                nuevo = Vendedor(legajo, nombre, apellido, basico, ventas)

            empresa.agregar_empleado(nuevo)
        
        archivo.close()
