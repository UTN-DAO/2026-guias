

from empresa import Empresa
from lector import Lector


emp = Empresa()
Lector.leer_empleados("empleados.csv", emp)
print(f"Cantidad de empleados leidos: {emp.cantidad_empleados()}")
print(f"Total de sueldos $ {emp.total_sueldos():,.2f}")
contadores = emp.cantidad_tipo()
print(f"Obreros: {contadores[0]}")
print(f"Administrativos: {contadores[1]}")
print(f"Vendedores: {contadores[2]}")

buscado = int(input("Ingrese el legajo a buscar: "))
encontrado = emp.buscar_por_legajo(buscado)
if encontrado:
    print(encontrado)
else:    
    print("No existe ningún empleado con ese legajo")