# Vamos a utilizar el paquete RICH para mejorar las salidas por pantalla
#
# instalar con pip install rich
#
# Esto reemplaza el print original con una versión mejorada
from rich import print
from rich.pretty import pprint
from rich.console import Console
from rich.panel import Panel
import rich.box

def comp_listas():
    mi_lista = [1,2,3,4,5,6,7,8,9,10]

    sig3 = []
    for nro in mi_lista:
        if nro%2 == 0:
            sig3.append(nro)

    print ("[bold on blue]Lista original:[/]", mi_lista)
    print ("[bold on green]Pares (tradicional):[/]", sig3)

    pares = ["Item="+str(item**2) for item in mi_lista if item%3 == 0] 
    print ("[bold on red]Cubos múltiplos de tres (comprensión):[/]", pares)



    pares = [nro for nro in mi_lista if nro%2 == 0]
    sig1 = [nro+1 for nro in mi_lista if nro%2 == 0]
    sig2 = [nro+1 for nro in pares]

    

    print ("[bold on blue]Lista original:[/]", mi_lista)
    print ("[bold on red]Numeros pares:[/]", pares)
    print ("[bold on red]Siguiente al par v1:[/]", sig1)
    print ("[bold on red]Siguiente al par v2:[/]", sig2)
    print ("[bold on red]Siguiente al par v3:[/]", sig3)


def comp_dict():
    persons = [
    {
        'name': 'Alice',
        'age': 30,
        'title': 'Data Scientist'
    },
    {
        'name': 'Bob',
        'age': 35,
        'title': 'Data Engineer'
    },
    {
        'name': 'Chris',
        'age': 33,
        'title': 'Machine Learning Engineer'
    }
    ]
    # Obtener aquellas entradas que tengan Data en su titulo
    # Metodo iterativo
    data1 = {}
    for p in persons:
        if 'Data' in p['title']:
            data1[p['name']] = p['title']
    
    print ("Método iterativo:",data1)
    
    # Metodo por comprension
    data2 = {p['name']:p['title'] for p in persons if 'Data' in p['title']}
    print ("Por comprension:",data2)
    


if __name__ == '__main__':
    c = Console()
    c.clear()
    c.print(Panel("Ejemplos de comprensión con LISTAS",box=rich.box.DOUBLE))
    comp_listas()
    c.print(Panel("Ejemplos de comprensión con DICCIONARIOS",box=rich.box.DOUBLE))
    comp_dict()
