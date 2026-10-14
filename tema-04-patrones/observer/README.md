### Lista de precios que avisa a sus vistas

Implementar con el patrón **Observer** una lista de precios. El modelo (`ListaPrecios`,
el *sujeto*) guarda producto → precio y, cada vez que un precio cambia, **notifica** a
todos los observadores registrados.

Se pide:

* Definir la interfaz `Observer` con un método `update(sujeto)`.
* Definir la clase `Subject` con `attach`, `detach` y `notify`.
* Definir `ListaPrecios` con operaciones para actualizar y quitar precios.
* Crear **al menos dos observadores** distintos, por ejemplo:
  * `Cliente` — imprime un aviso de que la lista cambió.
  * `Auditoria` — registra cada cambio.
* Mostrar que el modelo **no conoce** a sus observadores: agregar un observador nuevo no
  modifica `ListaPrecios`.

Punto extra: ¿qué diferencia hay entre `attach`/`detach` y simplemente guardar la lista
de vistas dentro del modelo?
