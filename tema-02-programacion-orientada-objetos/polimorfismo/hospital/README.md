## Hospital

Un hospital de nuestra ciudad necesita conocer cierta información respecto a los importes cobrados por las distintas atenciones que realiza,y requiere de un sistema orientado a objetos que le dé soporte a ello. Los datos relevantes son los siguientes:

* Del Hospital sólo interesa registrar la razón social; y una colección con todas las atenciones realizadas.
* Cada atención tiene los siguientes datos: un código numérico que identifica a cada atención; y un valor numérico que representa el tipode cobro (1: “efectivo”; 2: “tarjeta de crédito”). Las atenciones pueden ser médicas o de farmacia:
    * Una atención médica agrega los siguientes datos: el paciente atendido; y el importe de la consulta.
    * Una atención de farmacia agregan los siguientes datos: el importe total de los medicamentos vendidos en dicha atención; y un cupón de descuento que especifica el monto de descuento que se aplicaría sobre el importe total de los medicamentos; en caso que el cupón de descuento sea igual que 0, no se realizará ningún descuento; cabe aclarar que el cupón de descuento debe ser 0 o positivo.
    * Del paciente asociado a la atención médica se registran: su nombre; el síntoma que prevalece (1: “corazon”, 2: “pulmon”, 3: “otras”); y un valor booleano que representa si el paciente es habitual (true) o no (false) del hospital.
    
De cada clase de atención se debe calcular un importeACobrar en pesos, que representa lo que el hospital cobra al paciente por la atención brindada. Este cálculo dependerá del tipo de cobro de la atención y de la clase de atención brindada:

* El importe total de las atenciones médicas se calcula a partir del importe de la consulta. En caso que el paciente sea “habitual” se leaplicará un descuento del 25%. Por último, si el tipo de cobro es igual a 2 (“tarjeta de crédito”) se le incrementa al anterior importe un20% más; en caso que el cobro sea igual a 1 (“efectivo”) se le realiza un descuento del 10% sobre el anterior importe.
* El importe total de las atenciones de farmacia se calcula a partir del importe total de los medicamentos vendidos. Luego se le realiza el descuento del cupón de descuento cuyo importe está especificado. Por último, si el tipo de cobro es igual a 2 (“tarjeta de crédito”) se leincrementa al anterior importe un 30% más; en caso que el cobro sea igual a 1 (“efectivo”) se le realiza un descuento del 5% sobre elanterior importe.

Con lo expuesto anteriormente, usted deberá implementar:

* Todas las clases del modelo presentado.
* Los siguientes requerimientos de métodos:
    * Para las clases Atención, Médica, Farmacia y Paciente implementar su constructor, acceso y modificación y toString.
    * Para la clase Hospital implementar el método addAtención que agrega una atención a la colección.
* Definir e implementar los métodos importeACobrar de las atenciones, que calcule y devuelva el importe a cobrar por la atención de acuerdo a los criterios anteriormente especificados.
* En clase Hospital se requiere la implementación de los siguientes métodos:
    * importe_total_atencion_consulta: debe calcular la suma de los importes de las consultas de las atenciones médicas.
    * importe_promedio_atenciones: debe calcular el promedio de los importes a cobrar por aquellas atenciones médicas cuyo importe a cobrar se encuentre entre dos valores recibidos como parámetros.
    * codigo_primera_atencion_habitual: debe retornar el código de la primera atención médica que se haya registrado para un paciente habitual, o 0 si no existe ninguna.
   
