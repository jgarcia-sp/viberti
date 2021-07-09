"""
Teoria #Teoría de HMM y Viterbi.
La desambiguaci´on precisa (i) construir un modelo (hallar las probabilidades
de transici´on y de emisi´on en una base de datos) y (ii) aplicarlo a las nuevas
cadenas de texto. La primera tarea es relativamente f´acil. La segunda puede
resultar m´as laboriosa. Por ello recomiendo encarecidamente que se pongan ya
con la implementaci´on del algoritmo de Viterbi. El pseudoc´odigo del algoritmo
pueden encontrarlo en Jurafsky, en la Wikipedia en ingl´es y en infinidad de
p´aginas web. Incluso pueden encontrar implementaciones en Python. Construir
su propia funci´on a partir del pseudoc´odigo es la mejor manera de entender y
aprender. Siguen algunas observaciones. Se entender´an mejor si tienen el ejemplo
de Jurafsky y el pseudoc´odigo del algoritmo delante.
1.- A la funci´on hay que pasarle: (i) las probabilidades de transici´on entre
categor´ıas, (ii) las probabilidades de emisi´on, (iii) la cadena de texto a etiquetar.
Las probabilidades de transici´on, obtenidas a partir de una base de datos
ya etiquetada, por ejemplo con Freeling, pueden estar en un diccionario, por
ejemplo: probabilidades transicion[(’D’,’N’)]=0.003. Las claves son tuplas
de etiquetas y el valor es la probabilidad. En el ejemplo, encontramos que
en la base de datos la probabilidad de que a un Determinante le siga un Nombre
es de 0.003.
Las probabilidades de emisi´on, obtenidas a partir de la misma base de datos,
pueden estar tambi´en en un diccionario. Por ejemplo:
probabilidades emision[(’D’,’la’)]=0.004
indicar´ıa que hemos encontrado en la base de datos que un Determinante se
realiza como ’la’ con la probabilidad 0.004.
La cadena a etiquetar puede ser un string, en cuyo caso hay que segmentarlo
en palabras o enviar ya una lista de palabras –digamos cadena–.
La funci´on necesita tambi´en tener todas las categor´ıas empleadas en el
etiquetado –digamos categorias–. Se pueden pasar como una lista o extraerla a
partir de las claves de los diccionarios anteriores.
2.- A partir de la longitud de las palabras (los datos de observaci´on) y de la
longitud de las categor´ıas hay que rellenar dos tablas: (a) una almacenar´a las
probabilidades y (b) otra almacenar´a los punteros hacia atr´as para ir guardando
el camino de m´axima probabilidad. Esta parte es la m´as nueva para nostros.
Para almacenar valores num´ericos en una tabla (a) creamos un diccionario
–digamos tabla– por defecto con lambda:0. Para la tabla (b) lo que queremos
es guardar el valor de una determinada celda –digamos fila j, columna k–, es
1decir una tupa (j,k). Creamos un diccionario por defecto –digamos back– con
lambda:().
3.- Empezamos rellenando la primera columna: las probabilidades de emisi´on
de la primera palabra para cada una de las categor´ıas. En este caso vamos a
simplificar las probabilidades de transici´on asumiendo que todas las categor´ıas
tienen la misma probabilidad de ser iniciales de cadena. El valor ser´a simplemente
el de las probabilidades de emisi´on. Los punteros hacia atr´as en este caso
ser´an al inicio.
¿C´omo procedemos en nuestra escritura de c´odigo? Supongamos que hemos
asignado la longitud de las categor´ıas a la variable lc. Podemos iniciar
el rellenado de ambos diccionarios as´ı:
for j in range(lc):
tabla[(1,j)]=probabilidades_emision[(categorias[j],cadena[0])]
back[(1,j)]=(0,j)
4.- Ya tenemos los valores de la primera palabra. A partir de aqu´ı procedemos
a rellenar todas las restantes celdas. Lo hacemos con dos bucles. El bucle externo
recorre todas las palabras de la cadena a partir de la segunda -la primera ya
est´a-. Hacemos un recorrido num´erico: si l es la longitud de la cadena, nuestro
recorrido ser´a por el rango(2,l+1). El bucle interno recorre todas las categor´ıas.
Podr´ıa ser algo como esto:
for j in range(2,l+1):
for k in range(lc):
Ahora tienen que rellenar el valor de cada celda para tabla y back. Para
cada categor´ıa, el valor es el m´aximo de multiplicar (a) las probabildades de
emisi´on por (b) las probabilidades de transici´on.
El valor (a) es el que obtenemos en el diccionario y es fijo para categor´ıa y
palabra.
El valor (b) hay que computarlo a partir del diccionario de transiciones
y de los valores de la celda que corresponde a cada categor´ıa en la situaci´on
inmediatamente anterior. Es decir, hay que introducir otro bucle que recorra
todas las celdas inmediatamente anteriores (los valores de todas las categor´ıas
para la palabra inmediatamente anterior) y que multiplique su valor por el de las
transiciones del diccionario. De todos los valores nos quedamos con el m´aximo.
La celda de la que procede el m´aximo es la que guardamos en back.
5.- Una vez finalizado el proceso, la secuencia de categor´ıas m´as probables
se obtiene a partir de las celdas de back empezando desde el final."""
