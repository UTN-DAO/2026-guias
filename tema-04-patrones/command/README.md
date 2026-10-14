### Circuito de alta de clientes

Modelar con el patrón **Command** el proceso de alta de clientes de una entidad financiera.
El circuito cambia según el **segmento** del cliente:

* **Persona**: validar documentación, asignar límite y registrar/notificar.
* **Pyme**: lo anterior más verificar la situación fiscal.
* **Corporativo**: lo anterior más evaluar garantías.

Puntos a resolver:

* Definir la interfaz `Comando` con `ejecutar()` y una clase concreta por cada paso.
* Definir los **receptores** (`Solicitud`, `RepositorioClientes`, `Notificador`) que conocen
  las operaciones concretas.
* Definir el **invocador** `ProcesadorCircuito`, que recorre una secuencia de comandos y llama
  siempre a `ejecutar()`, sin conocer los tipos concretos, y deja un **registro de auditoría**.
* Armar la secuencia de pasos según el segmento en una función externa `circuito_para(...)`.
  ¿Por qué esa decisión no debería estar dentro del invocador?

Extensiones:

* Agregar un segmento nuevo (por ejemplo `minorista`) con su propia secuencia, **sin modificar**
  los comandos existentes.
* Incorporar un comando `EnviarAlOrganismoDeControl` que se ejecute solo para clientes
  corporativos y quede registrado en la auditoría.
* Modelar el procesamiento **por lotes**: encolar los comandos y ejecutarlos al final del día.
  ¿Qué ventaja aporta tratarlos como objetos?
