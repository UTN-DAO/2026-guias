## Solución

La simulación está programada en la función simulacion(). Dado que los resultados son numerosos, la función no los retorna sino que los imprime directamente al terminar los cálculos.

Para el conteo de tiradas clasificado por color, el problema principal es el de conocer el color de cada número en una ruleta real. El algoritmo de determinación del color es el siguiente:

- Los números 10 y 28 son negros.
- Los otros números son negros si la suma de sus dígitos es par.
- La suma de los digitos no es la suma simple, si al sumar los dígitos del número el resultado es mayor a 9, deben volver a sumarse los digitos de dicho resultado hasta reducir a un único dígito.

Para ello el programa inicia generando una lista con los colores de los números, almacenando en la misma una tupla en la que el primer elemento es un número y el segundo el color asociado al mismo. En dicha lista las tuplas se almacenan de forma que cada número está almacenado en la lista en su mismo índice, por ejemplo, el número 10 esta almacenado como (10,"N") en la posición 10. La lista es creada en la función generar_ruleta.

Para el cálculo del color la función get_color recibe un número y devuelve el color correspondiente al parámetro.

Finalmente la función reducir_numero recibe un número entero y calcula la suma de sus dígitos. La función se llama recursivamente cuando la suma obtenida es mayor a 9 y por lo tanto es un número de más de un dígito.


