### ABM de personas tras una fachada

Implementar con el patrón **Facade** una **FachadaPersonas** que ofrezca una interfaz
unificada de ABM (**a**ltas, **b**ajas, **m**odificaciones y consultas) sobre un
subsistema de persistencia en SQLite.

El subsistema está formado por varias clases que el servicio **no debe conocer**:

* `ConexionBD` — abre/cierra la conexión y ejecuta sentencias.
* `ConstructorSQL` — arma las sentencias `INSERT`, `UPDATE`, `DELETE` y `SELECT`.
* `Validador` — aplica reglas de negocio (campos obligatorios, edad no negativa).
* `Auditoria` — registra cada operación realizada.

Puntos a resolver:

* Definir cada clase del subsistema por separado.
* Definir `FachadaPersonas` con los métodos `alta`, `baja`, `modificar` y `listar`,
  que coordinan internamente el subsistema. El servicio nunca ve SQL ni `sqlite3`.
* Definir `ServicioPersonas`, un cliente que use **solo** la fachada.
* Justificar: si mañana se cambia SQLite por PostgreSQL, ¿qué clases habría que tocar?
  ¿Por qué el servicio no se modifica?
