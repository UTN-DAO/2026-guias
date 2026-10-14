### Semáforo con modo peatonal

Implementar con el patrón **State** un semáforo de tráfico con los estados **Rojo**,
**Verde** y **Amarillo**. El cambio de estado debe quedar encapsulado en cada estado (el
contexto no decide las transiciones).

Agregar un **modo peatonal**: al activarlo, la transición desde Rojo debe pasar primero por
un cuarto estado **Peatonal** que habilita el cruce de las personas y luego continuar el
ciclo vehicular. El semáforo debe exponer operaciones para activar y desactivar el modo
peatonal.

Puntos a resolver:

* Definir la interfaz `Estado` y las clases concretas `Rojo`, `Peatonal`, `Verde` y
  `Amarillo`, cada una con su transición.
* Definir el contexto `Semaforo` que delega en el estado actual.
* Resolver el modo peatonal sin una cadena de `if/elif` dentro del contexto: la decisión
  de pasar por `Peatonal` debe vivir en el estado `Rojo`.
* Ejecutar la simulación y mostrar la secuencia de estados en consola.
