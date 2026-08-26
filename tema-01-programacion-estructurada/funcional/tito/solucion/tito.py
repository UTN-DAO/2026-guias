import random

movimientos = {
    "N": lambda x, y: (x, y + 10),
    "S": lambda x, y: (x, y - 20),
    "E": lambda x, y: (x + 10, y),
    "O": lambda x, y: (x + 20, y),
}

x = random.randint(0, 400)
y = random.randint(0, 400)
print(f"Posición inicial: ({x:>3},{y:>3})")

print("Tito el robot")
print("N- Norte")
print("S- Sur")
print("E- Este")
print("O- Oeste")
print("F- Finalizar")

opcion = input("Ingrese la opción: ")
while opcion != "F":
    for letra in opcion:
        if movimientos.get(letra):
            x, y = movimientos[letra](x, y)
            print(f"Posición actual: ({x:>3},{y:>3})")
    opcion = input("Ingrese la opción: ")
    
print("Gracias")