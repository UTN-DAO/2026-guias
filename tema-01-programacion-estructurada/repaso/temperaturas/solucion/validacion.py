def ingresar_numero_entre(mensaje, minimo, maximo):
    
    valor = float(input(mensaje))
    while not minimo <= valor <= maximo:
        print(f"Debe ingresar un valor entre {minimo} y {maximo}")
        valor = float(input(mensaje))

    return valor    
    
    
    