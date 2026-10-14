### Un sistema, varios patrones: pedidos

Integrar **varios patrones** en un mismo sistema, aprovechando que cada uno resuelve un
eje de variación distinto. Dominio: los pedidos de una distribuidora.

Se pide modelar:

* **State** — un pedido evoluciona por estados `Nuevo`, `Confirmado`, `Entregado` y
  `Cancelado`. Solo las transiciones válidas están permitidas; el resto se rechaza con
  una excepción. El estado decide la transición, no la fachada.
* **Strategy** — el recargo de envío se calcula con una familia de estrategias
  (`RecargoFijo`, `RecargoPorZona`). El pedido delega en la estrategia.
* **Observer** — cada pedido es un *sujeto*: al cambiar de estado notifica a sus vistas
  (`Auditoria`, `NotificadorCliente`) sin conocerlas. Suscribir una vista nueva no toca
  al pedido.
* **Facade** — `FachadaPedidos` expone la API de ABM (`crear_pedido`, `avanzar`, `listar`),
  valida, elige la estrategia y conecta los observadores. El cliente no ve el subsistema.

Puntos a resolver:

* Identificar en el código **qué eje** resuelve cada patrón y **dónde está la costura**
  (por ejemplo, el punto donde la fachada conecta los observadores).
* Verificar que agregar un estado o una vista nueva **no obliga a tocar** las clases
  existentes.
* Como extensión: reemplazar la elección de estrategia de la fachada por una **Factory**
  (`FabricaRecargos.crear(zona)`) y explicar qué se gana.
