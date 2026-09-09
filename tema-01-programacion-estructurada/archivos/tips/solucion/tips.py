# Vamos a hacer un análisis sobre las propinas,
# segun el archivo tips, obtenido de los registros
# de una pizzería en New York

# El archivo contiene los siguientes campos, separados por comas
# -----------------------------------
# "total_bill" -> Total del servicio,
# "tip" -> Propina,
# "sex" -> Sexo del cliente,
# "smoker" -> El cliente es fumador,
# "day" -> Día (Juev, Vie, Sab, Dom),
# "time" -> Horario,
# "size" -> Tamaño de la mesa (comensales)

# Vamos a tener que procesar el archivo tips.csv y obtener 
# los siguientes resultado:
# ¿Quién paga más propinas?¿Hombres o mujeres?
# ¿Cuáles son los días más 'lentos', con menos propinas?
# ¿Cuál es el promedio de las propinas?
# ¿Cuándo se vendió la orden más grande (qué día y en qué turno)?

propinas_hombres = propinas_mujeres = 0
propina_fumador = propina_no_fumador = 0
propinas_acum = [0]*4
propina_promedio = 0
cant_operaciones = 0
dia_orden_mayor = None
turno_orden_mayor = None
monto_orden_mayor = None

#################################################################################
# Para utilizar la librería mejorada de consola (rich) primero hay que instalarla
# utilizando el comando pip install rich
#################################################################################

from rich import print
from rich.console import Console
from rich.panel import Panel

c = Console()
c.clear()

first_row = True
with open("tips.csv","r") as file:
    for fila in file:
        # Debo saltear el primer registro ya que contiene los titulos
        if first_row:
            first_row = False # Indicar que ya no estoy en la primera fila
        else:
            cant_operaciones += 1
            # Hacer todo el procesamiento
            # Ahora debo separar la fila leída en sus componentes
            campos = fila[:-1].split(",")
            # print(campos)
            # Saco los campos que necesito
            total = float(campos[0])
            propina = float(campos[1])
            sexo = campos[2]
            dia = campos[4]
            horario = campos[5]

            # Acumular por separado las propinas de hombres y mujeres
            if sexo == 'Hombre': 
                propinas_hombres += propina
            else:
                propinas_mujeres += propina

            # Obtener los datos de la mayor orden
            # Cuándo? Cuando sea la primera o sea mayor a la anterior
            if monto_orden_mayor == None or total > monto_orden_mayor:
                monto_orden_mayor = total
                dia_orden_mayor = dia
                turno_orden_mayor = horario

            # Solo trabajo 4 días así que puedo acumular las propinas en un
            # vector de 4 elementos, relacionados a Jue, Vie, Sab, Dom
            if dia == 'Juev':
                propinas_acum[0] += propina
            elif dia == 'Vie':
                propinas_acum[1] += propina
            elif dia == 'Sab':
                propinas_acum[2] += propina
            else:
                propinas_acum[3] += propina

# Calcular la propina promedio
propina_promedio = (propinas_hombres+propinas_mujeres)/cant_operaciones

# Recorrer el vector de propinas y ver cual es el menor
menor_indice = 0  # Voy a suponer que es el primero
menor_propina = propinas_acum[0]
menor_dia = ""

for i in range(len(propinas_acum)):
    if propinas_acum[i] < menor_propina:
        menor_propina = propinas_acum[i]
        menor_indice = i
# Cuando termine tengo que ver a qué dia corresponde ese índice
if menor_indice == 0:
    menor_dia = "Jueves"
elif menor_indice == 1:
    menor_dia = "Viernes"
elif menor_indice == 2:
    menor_dia = "Sábado"
else:
    menor_dia = "Domingo"

c.print(Panel("Análisis de propinas en New York"))

print (f"[white bold on green]Propinas de los hombres:[/] {propinas_hombres:.2f}")
print (f"[white bold on green]Propinas de las mujeres:[/] {propinas_mujeres:.2f}")
print (f"[white bold on green]Propina promedio:[/] {propina_promedio:.2f}")
print (f"La mayor venta fué de [on green]{monto_orden_mayor}[/] y se realizó un [on green]{dia_orden_mayor}[/] en el turno [on green]{turno_orden_mayor}[/]")
print (f"Los días más lentos son los [on green]{menor_dia}[/] con solamente [on green]{menor_propina}[/] de propina")

c.print(Panel("Fin de la ejecución"))
