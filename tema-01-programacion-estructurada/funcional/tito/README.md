## Tito el robot

Desarrollar un programa controlado por menú de opciones que permita simular el desplazamiento
de un robot sobre un plano cuyo tamaño es de 400 x 400, y las posiciones válidas se identifican 
desde 0 como en un sistema de coordenadas cartesianas.
Inicialmente se genera la posición aleatoria del robot en forma de punto (x,y). Luego se presenta
un menú de opciones que permita los siguientes movimientos:
* Opción N: Girar al norte y avanzar 10 pasos
* Opción S: Girar al sur y avanzar 20 pasos
* Opción E: Girar al este y avanzar 10 pasos
* Opción O: Girar al oeste y avanzar 20 pasos
* Opcion F: Finalizar

Luego de cada movimiento el programa debe informar la posición del robot.

Alternativas:
* En lugar de ingresar cada movimiento individualmente, se puede recibir una cadena que contenga más de un movimiento, por ejemplo "NNEENSSNO".
* En el caso de que una orden de movimiento lleve al robot fuera de los márgenes del plano, el movimiento debería finalizar en el borde.

