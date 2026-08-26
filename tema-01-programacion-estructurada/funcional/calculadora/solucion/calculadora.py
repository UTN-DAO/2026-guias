
operaciones = [
    lambda a,b: 0,
    lambda a,b: a + b,
    lambda a,b: a - b,
    lambda a,b: a * b,
    lambda a,b: a / b if b else 0,
               ]

print("Calculadora básica")
print("1- Sumar")
print("2- Restar")
print("3- Multiplicar")
print("4- Dividir")
print("0- Salir")

opcion = int(input("Ingrese la opción: "))
while opcion:
    a = float(input("Ingrese el primer operando: "))
    b = float(input("Ingrese el segundo operando: "))
    resultado = operaciones[opcion](a,b)
    print("El resultado es:", resultado)
    opcion = int(input("Ingrese la opción: "))
    
print("Gracias")