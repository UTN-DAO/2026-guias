paises = {
    "BR": "Brasil",
    "AR": "Argentina",
    "CO": "Colombia",
    "PE": "Perú",
    "VE": "Venezuela",
    "CL": "Chile",
    "EC": "Ecuador",
    "BO": "Bolivia",
    "PY": "Paraguay",
    "UY": "Uruguay",
}

codigo = input("Código del país (vacío para salir): ")
while codigo:
    nombre = paises.get(codigo.upper())
    if nombre:
        print(nombre)
    else:
        print("País no encontrado")
    codigo = input("Código del país (vacío para salir): ")
