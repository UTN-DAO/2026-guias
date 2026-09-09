
cantidad = {"X":0, "H": 0, "K": 0}
nombres =  {"X":"Córdoba", "H":"Chubut", "K":"Catamarca"}

archivo = open("cp.csv")
for linea in archivo:
    datos = linea.split(";")
    provincia = datos[0]
    cantidad[provincia] += 1
    
for provincia, cant in cantidad.items():
    print(f"Códigos de {nombres[provincia]}: {cant}")
    