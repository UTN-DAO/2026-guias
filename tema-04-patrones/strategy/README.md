### Cálculo del coste de envío

Implementar con el patrón **Strategy** el cálculo del coste de un envío. Un paquete tiene un
**peso** (kg) y una **distancia** (km), y existen varias políticas de cálculo:

* **Estándar**: tarifa base 5 + 1 por kg + 0,05 por km.
* **Exprés**: tarifa base 10 + 2 por kg + 0,12 por km.
* **Tarifa plana**: 9,99 sin importar peso ni distancia.

Puntos a resolver:

* Definir la interfaz `EstrategiaEnvio` con el método `calcular(paquete)`.
* Definir el contexto `CalculadorEnvio`, que recibe una estrategia y la puede cambiar con
  `set_estrategia(...)`.
* Calcular el mismo paquete con las tres estrategias y mostrar los resultados.
* Agregar una cuarta estrategia **Por volumen** (base 3 + 0,02 por volumen + 0,03 por km,
  con volumen = peso × 100), **sin modificar** `CalculadorEnvio`. ¿Por qué no hace falta
  tocarlo?
* Implementar además una variante **sin herencia**: un diccionario que asocie el nombre de la
  estrategia con la función que la calcula, y usarlo para calcular el mismo paquete.
