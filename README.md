# tkinter-sqlite
Resolucion de un Examen final de  INSTITUTO TECNOLOGICO DE SOLEDAD ATLANTICO

Esto es un parcial que le hice a un estudiante llamado Edwin Rubiano con la cedula 1140882562, con la materia de progracmacion del profesor LUIS EDUARDO LOBO PEDRAZA. Debido que esta persona me quedo mal en el pago hago publico el codigo de la solucion del parcial.

EJERCICIO 1.

Realice un programa que le permita cotizar el valor de la construcción oficinas modulares. Los
representantes de ventas visitan a los clientes quienes muestran el sitio donde se van a construir
dichas oficinas y además le dicen el número de oficinas, mesas sillas y elementos adicionales
(repisas, tapetes, papeleras, archivadores y bibliotecas). Cuando el representante va a registrar la
orden del pedido lo hace a través de una codificación que maneja la empresa de construcción de
oficinas modulares. Siempre se inicia colocando la letra P, para especificar que es un nuevo, después
se colocan las áreas en las cuales se van a colocar las oficinas seguida de sus dimensiones, cada área
se inicia con la letra A, seguida por su dimensión en centímetros, dando el ancho y largo del área,
por ejemplo, si la dimensión del espacio es 4 metros de ancho por 4 metros de largo se coloca
A400x400; seguido a esto y dentro de paréntesis se colocan cuantas oficinas estarán en ese espacio
para esto se coloca la letra O seguido del número de oficinas y seguido los elementos de las oficinas,
estos incluyen como se mencionó: Mesas (M), Sillas (S), Repisas (R), Tapetes (T), Papeleras (P),
Archivadores (A), Bibliotecas (B), estos elementos se colocan precedidos por la inicial del elemento
y seguido de la cantidad de ese elemento, por ejemplo, si son 4 sillas S4. Se pueden codificar varias
áreas, si es así se coloca un punto y coma (;) y luego se codifica el área y los elementos. Esto lo realiza
el representante de ventas a través de una GUI que cuenta con un cuadro de texto donde coloca la
codificación según el pedido del cliente. Cuando el representante de ventas solicite a través de la
GUI la cotización el sistema debe mostrar una interfaz mostrando un valor base que corresponde a
costo de partida de cualquier proyecto (el cual se debe multiplicar por el área del espacio de la
oficina), más el valor por cada oficina. Para los elementos se deben mostrar las distintas opciones
que se tengan para que con base en cada elemento seleccionado se calcule el valor final de la
cotización.

...



EJECICIO 2

Realice un programa que le permita registrar los resultados de varias ligas de futbol, se desea
calcular la posición final de cada equipo. En cada liga se le dan 3 puntos al equipo ganador, un punto
en caso de empate, y 0 puntos al que pierde.
La posición de cada equipo en la liga se determina de la siguiente manera:
a.
 Mayor número de puntos obtenido en todos los juegos;
b.
 Mayor diferencia de goles en todos los juegos;
c.
 Mayor número de goles anotados; y
d.
 Mayor número de goles anotados como visitante
Si dos o más equipos están igualados en los criterios básicos de arriba, su posición será determinada
por el orden lexicográfico del nombre del equipo.
Se trabaja con un archivo de entrada con el siguiente formato
L X vs. Y V K
Donde L y V son los nombres de los equipos X y Y son los goles de cada equipo y K es la fecha jugada.
En el archivo inicia con el número N de partidos disputados, el nombre de la liga, las siguientes N
líneas contiene la información de los encuentros de esa fecha, se continua con el siguiente número
de partidos nombre de la liga y fechas, y luego las N líneas, se finaliza cuando se encentra el final del
archivo.
A continuación, se muestra un ejemplo de la entrada y la salida.


.....
