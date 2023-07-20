# IMC
El índice de masa corporal es una razón matemática que asocia la masa y la talla de un individuo


El código que proporcionas calcula el Índice de Masa Corporal (IMC) de una persona en base a la estatura (en centímetros) y el peso (en kilogramos) ingresados por el usuario. A continuación, te explico cómo funciona:

A = int(input('Ingrese su estatura (en centimetros) : ')): Solicita al usuario que ingrese su estatura en centímetros y lo almacena en la variable A.

B = int(input('Ingrese su peso (en kilogramos) : ')): Solicita al usuario que ingrese su peso en kilogramos y lo almacena en la variable B.

C = (B/(A*A))*10000: Calcula el IMC dividiendo el peso (B) entre la estatura al cuadrado en metros (A*A) y luego multiplicándolo por 10000 para convertirlo a unidades de IMC estándar. El resultado se almacena en la variable C.

print("Tu IMC es: ",C): Muestra el IMC calculado.

Después de calcular el IMC, el código evalúa diferentes condiciones para determinar en qué rango de IMC se encuentra el usuario y muestra un mensaje correspondiente:

a. Si el IMC está entre 18 y 25 (ambos inclusive), se muestra "Esta en su peso ideal".
b. Si el IMC es menor que 18, se muestra "Usted tiene bajo peso".
c. Si el IMC es mayor que 25, se muestra "Usted tiene sobrepeso".

El IMC es una medida utilizada para evaluar si una persona tiene un peso adecuado en relación con su estatura. Es importante tener en cuenta que el IMC es solo una medida aproximada y no tiene en cuenta otros factores como la composición corporal o la distribución de la grasa en el cuerpo. Para obtener una evaluación más completa de la salud, se recomienda consultar a un profesional de la salud.
