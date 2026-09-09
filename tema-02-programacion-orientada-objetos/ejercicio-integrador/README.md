## Caso de estudio

### Empresa de transporte de cargas

Una empresa de transporte de cargas necesita un software que la ayude a organizarse con la carga de las camiones que maneja. La empresa puede recibir packings, cajas sueltas y bidones que transportan líquido.

* Un packing es una estructura de madera que arriba tiene un montón de cajas, se envuelve todo con plástico para que no se desbanden las cajas. Todas las cajas tiene el mismo peso. 
    * El peso de un packing es (peso de cada caja * cantidad de cajas) + peso de la estructura de madera que va abajo. 
    * Para cada packing se informa qué llevan las cajas, p.ej. Material de construcción.
* De cada caja suelta se informa el peso individualmente, son todas distintas.
* El peso de un bidón es su capacidad en litros por la densidad (o sea, cuántos kg pesa un litro) del líquido que se le carga. Los bidones van siempre llenos hasta el tope.

Cada camión puede llevar hasta una carga máxima medida en kg. Además, cada camión puede: estar disponible para la carga (en cuyo caso ya puede tener
cosas cargadas), estar en reparación, o estar de viaje.
Algunos requerimientos:

* Subir una carga al camión, donde la carga puede ser un packing, una caja suelta, o un bidón. 
    * Considerar que no se puede saturar un camión con más peso de lo que su carga máxima permite.
* Bajar una carga del camión, 
    * siempre que el camión se encuentre disponible con cargas y que a su vez la carga se encuentre presente dentro de él.
* Conocer el total de cargas de un camión en todo momento y su peso.
* Permitir modificar el estado de un camión, sea porque 
    * entro en reparación, 
    * salió de reparación, 
    * está en viaje o 
    * de regreso.
* Obtener el listado de cargas contenidas, como string, para imprimir por pantalla.
* Saber si un camión está listo para partir, que es:
    * Si está disponible para la carga, 
    * y el peso total de lo que tiene cargado es de al menos 75% de su carga máxima.

![Modelo][imagen]

[imagen]: modelo.png