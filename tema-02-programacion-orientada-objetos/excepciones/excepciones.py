"""
Pruebas de excepciones
"""
import traceback

# División por cero

#a = 10 / 0

# Ahora con excepciones

def rutina_con_excepciones():
    try:
        a = 10
        b = 0
        c = a / b
    except ZeroDivisionError as e:
        print ("Ha ocurrido un problema:",e)
    else:
        print(a,"dividido",b,"es",c)
    finally:
        print("Esto se ejecuta haya o no excepciones")


    try:
        una_instruccion_absurda()
    except Exception as e:
        print ("Captura CUALQUIER excepción, por ejemplo una función inexistente", e)

    try:
        m = open("no_ta_file.txt")
        texto = m.read()
        print (texto)
    except FileNotFoundError as e:
        print ("El archivo no existe:", e)
        '''
        Si importamos el módulo traceback, podemos tener acceso
        a información del estado de ejecución al momento de dispararse
        una excepción, y realizar acciones con esa información,
        por ejemplo imprimir la pila de llamada.'''
        print (traceback.print_stack())

if __name__ == '__main__':
    rutina_con_excepciones()

