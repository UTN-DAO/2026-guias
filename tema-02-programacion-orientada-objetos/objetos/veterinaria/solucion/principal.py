from cliente import Cliente
from mascota import Mascota

def main():
    
    clientes = []
    
    
    num = int(input("Ingrese el número del cliente (fin con 0): "))
    while (num != 0):
        nom = input("Ingrese el nombre del cliente: ")
        ant = int(input("Ingrese la antigüedad: "))
        nomm = input("Ingrese el nombre de la mascota: ")
        edad = int(input("Ingrese la edad: "))
        
        mascota = Mascota(nomm, edad)
        cliente = Cliente(num, nom, ant, mascota)
        
        clientes.append(cliente)
        
        num = int(input("Ingrese el número del cliente: "))
        
    
    cantidad = len(clientes)
    if cantidad > 0:
        print("\n\nResultados")
        print(f"Cantidad de clientes: {cantidad}")
    
        promedio = sum(list(map(lambda c: c.mascota.edad, clientes))) / cantidad
        print(f"Promedio de edad de las mascotas: {promedio}")
        
        cant_mas_5 = len(list(filter(lambda c: c.antiguedad > 5,clientes)))
        print(f"Hay {cant_mas_5} clientes con más de 5 años de antigüedad")
        
        clientes_mas_5 = filter(lambda c: c.mascota.edad > 5,clientes)
        print("Clientes con mascotas de más de 5 años de edad:")
        for c in clientes_mas_5:
            print(c)
    else:
        print("No ingresó ningún cliente")
        
        
if __name__ == "__main__":
    main()