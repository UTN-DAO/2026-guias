import random

numeros = [random.randint(1, 20) for _ in range(10)]
conjunto = set(numeros)

print("Lista original:", numeros)
print("Conjunto:", conjunto)
print("Tamaño original:", len(numeros))
print("Sin repetidos:", len(conjunto))
