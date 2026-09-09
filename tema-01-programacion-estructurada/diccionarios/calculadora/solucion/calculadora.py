def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return float('inf') if b == 0 else a / b

operaciones = {
    "+": suma,
    "-": resta,
    "*": multiplicacion,
    "/": division,
}

while True:
    linea = input("Operación (vacío para salir): ")
    if not linea:
        break

    partes = linea.split()
    if len(partes) != 3:
        print("Formato inválido. Use: operando operador operando")
        continue

    operando1 = float(partes[0])
    operador  = partes[1]
    operando2 = float(partes[2])

    funcion = operaciones.get(operador)
    if funcion:
        print("Resultado:", funcion(operando1, operando2))
    else:
        print("Operador no válido")
