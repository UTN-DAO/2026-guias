from rich import print

# Sintaxis
# lambda argumentos : expresion

# Defino una función lambda llamada cuadrado
# que devuelve el numero pasado, al cuadrado
cuadrado = lambda x : x**2

print (cuadrado(3))

# Defino una función lambda, llamada cuadrado_mayor_diez
# que devuelve verdadero o falso según el cuadrado del 
# numero pasado sea mayor a diez o no.
cuadrado_mayor_diez = lambda x : True if x**2 > 10 else False

print (cuadrado_mayor_diez(2))
print (cuadrado_mayor_diez(3))
print (cuadrado_mayor_diez(4))
print (cuadrado_mayor_diez(5))
