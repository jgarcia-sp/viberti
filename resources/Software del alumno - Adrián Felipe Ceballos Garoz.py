>>> def viterbi(texto, prob_trans, prob_emis):
    V=[{}]
    palabras=texto.split()
    #Vamos a usar las etiquetas del Universal POS tags pq están más condensadas. Según Iván Arias Rodríguez, experto sistemas de etiquetación, "el tagset (de Corpus Brown) es un tanto extraño, con poca estructura interna
    #y con algunas etiquetas poco ortodoxas: palabras en título, titular, cita (etiqueta postpuesta a la etiqueta principal unida con el guion). Hay pocos símbolos. Las palabras extranjeras reciben una etiqueta principal
    #y se le antepona la etiqueta FW unida con el guion.
    etiquetas=['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X']
    for i in etiquetas:
            V[0][i]=prob_trans[i]*prob_emis[i][texto[0]]
    #Para la longitud de las palabras de texto y crear las dos tablas que almacenaran las probabilidades.
    for j in range(1, len(texto)):
        V.append({})
        for k in etiquetas:
            (prob, tag) = max((V[j-1][k0] * prob_trans[k0][k] * prob_emis[k][texto[j]], k0) for k0 in etiquetas)
            #Con esta línea de código compleja vamos a condensar lo siguiente: 
            #designamos la probabilidad y el etiquetado que funciona de la siguiente manera
            #la prob max de j empezara en menos 1 pq empezaremos desde la derecha si estuviesemos en pseudocodigo
            #k empieza en 0 porq es la parte que empezara desde la izquierda porque es la probabilidad en si (es la que tiene que llegar a la prob maxima)
            #multiplicamos los valores por la prob_trans y por la prob_emis Eso se recorre en K0 dentro de las etiquetas. 
            V[j][k] = prob
            #rellenar las filas y las columnas de la tabla
        combinaciones=[]
        for l in V:
            for x,k in l.items()
            #para genera una lista en clave-valor de los registros del diccionario
                if l[x]==max(j.values()):
                #values para generar una lista en valor de los registros del diccionario
                    combinaciones.append(x)
        #Obtenemos la secuencia más probable de categorias que haya dentro de V
    #Para obtener la secuencia más alta.
    smp = max(V[-1].values())

    return print('La secuencia de etiquetas es '+' '.join(combinaciones)+'con mayor probabilidad es')
    #Devuelve una tabla con la secuencia de etiquetas más probable.
"""#Ejercicio 1. 1. (2 points) El método split se aplica a strings y devuelve una lista. Pueden comprobar su uso escribiendo
en IDLE: help(str.split). Supongamos que cadena es una variable tipo string. ¾Hay diferencias entre
cadena.split() y cadena.split(' ')? Si las hubiera indicar cuáles son.
2. (2 points) ¾A qué tipo de datos se aplicaría y qué haría [::-1]?
3. (6 points) a='newly formed bland ideas are inexpressible in an infuriating way'.
Realizar las siguientes tareas:
1. obtener una lista de palabras a partir de la cadena de caracteres;
2. encontrar la posición de 'in';
3. obtener una nueva lista de palabras eliminando 'in' mediante 'troceado' (slicing);
4. obtener una cadena nueva:
b="newly formed bland ideas are inexpressible an infuriating way"
"""
#1.
cadena="Hola, ¿cómo estás?"
print(cadena.split())
['Hola,', '¿cómo', 'estás?']
print(cadena.split(" "))
['Hola,', '¿cómo', 'estás?']
#cadena.split() y cadena.split(" ") no arroja diferencia alguna.
#2.
#A strings, listas, tuplas, diccionarios. Te devuelve la información invertida.
#3.
#1.
a='newly formed bland ideas are inexpressible in an infuriating way'
print(a.split())['newly', 'formed', 'bland', 'ideas', 'are', 'inexpressible', 'in', 'an', 'infuriating', 'way']
a=a.split( )
type(a)
<class 'list'>
print(a)
['newly', 'formed', 'bland', 'ideas', 'are', 'inexpressible', 'in', 'an', 'infuriating', 'way']
#2.
a.index("in")
6
#3.
a.remove("in")
print(a)
['newly', 'formed', 'bland', 'ideas', 'are', 'inexpressible', 'an', 'infuriating', 'way']
#4.
b=a
print(b)
"""Remitir un fichero de texto con las respuestas. Incorporar copia de la sesión de IDLE.
1. (10 points) Descarguen la obra de Melville. Realicen las siguientes tareas:
1. Abrir el chero, leerlo y guardarlo en la variable texto.
2. ¾Cuántos caracteres tiene?
3. En la variable palabras guardamos las palabras, considerando que es palabra toda secuencia de
caracteres que va entre espacios en blanco (esto no es correcto, pero sí bastante aproximado).
4. ¾Cuántas palabras hay?
5. ¾Cuántos caracteres tienen por término medio las palabras?
6. ¾Cuántas vocales tiene el texto?
7. ¾Cuántas líneas tiene el texto?"""
#1.
texto=open("C:/Users/Adrián/Desktop/Asignaturas/Computacional - 9-6/2020-2021/Ejercicios/melville_moby.txt", mode="r", encoding="utf-8")
texto=texto.read()
#2.
len(texto)
#3.
palabras=texto.split( )
#4.
len(palabras)
#5. Dividimos todos los caracteres que tiene el texto, por todas las palabras alejadas en la variable "palabras" como lista.
len(texto)/len(palabras)
#6.
voc=0 #Declaramos un contador, al que se irá sumando 1 en caso de que encontremos una vocal.
for vocal in texto: #Se crea una función para buscar las vocales del texto.
        if vocal in "aeiouAEIOU": #En caso de que se encuentre unas de las vocales
            voc = voc + 1 #Se sumará +1.

print(voc) #Al pedir que nos muestre en pantalla la variable declarada se devolverá el número de vocales obtenido en el contador.
#7.
texto.count("\n") #\n nos salta a la siguiente línea de un texto.
"""1.- Objetivo. El objetivo del ejercicio es ir aplicando a tareas lingüísticas reales lo que ya se ha visto 
en clase. Vamos a usar la edición de Fortunata y Jacinta del Proyecto Gutenberg. Tras la descarga, 
con un editor de texto, eliminar el principio y el final. Debe empezar así: "Las noticias más remotas" y
terminar así: "lo mismo da»."
2.- Tarea concreta. La tarea lingüística es: obtener una lista con las palabras del texto que son 
nombres propios.
3.- Recursos. En una situación profesional o de investigación, usaríamos un diccionario específico de
nombres propios o sofisticadas técnicas de reconocimiento de nombres de entidades. Aunque 
nuestro resultado no sea perfecto, vamos a abordar la tarea sin esos recursos, usando sólo lo que el 
núcleo básico de Pyton permite (sin recurrir a módulos) y nuestros conocimientos como lingüistas.
4.- Hint. Supongamos que en vez de un texto español se tratase de un texto en una lengua 
semánticamente desconocida de la que sabemos sus reglas de escritura. Por ejemplo: que los 
nombres propios se escriben siempre en mayúscula, que después de punto (y probablemente de ? o
!) se escribe en mayúscula, etc. Las reglas que ustedes como lingüistas conocen y aplican. 
Recomiendo encarecidamente que planteen el problema primero con lápiz y papel (qué tareas hay 
que hacer, qué resultado se espera, etc.) y sólo después emprender la escritura de código.
5.- Remitir un archivo de texto con la lista de las palabras que serían nombres propios y una copia 
de la sesión del idle que genera esa lista"""
texto=open("C:/Users/Adrián/Desktop/Asignaturas/Computacional - 9-6/2020-2021/Ejercicios/Fortunata_y_Jacinta.txt", mode="r", encoding="utf-8")
texto=texto.read()
import re #Ahora hemos importado el módulo para trabjar
#con Expresiones Regulares (regular expressions)
re.findall("[A-Z][a-záéíóú]+",texto) #re.findall toma la expresión regular y
#busca aquellos patrones coincidentes con dicha expresión regular en la variable
#seleccionada - texto en este caso - y nos devuelve una lista.
"""
import time
print(time.time())
import os
#Se importa el módulo os que sirve para trabajr con los directorios y carpetas del ordenador.
def corpora(ruta):
#Esta función toma el módulo importado os
#y al reconocernos los archivos dentro del ordenador metemos dentro de ruta
#el directorio deseado, pasando primero los datos a una lista que estará en ruta
#devolviendo finalmente los datos de esa ruta como lista.
    """
Con esta función ponemos la ruta del directorio como variable (ruta)
y listas todos los documentos dentro del directorio
"""
    datos=os.listdir(ruta)
    return datos

corpora("C:\\")
#Al declarar esto nos dará la información alojada en C en ordenador.
print(time.time())"""
"""Los puzzles de palabras suelen (o solían o suelen en otros países) ser entretenimientos frecuentes. Incluso
hay aplicaciones para algunos de ellos. Uno bastante popular es el target puzzle. Si no lo conocen, pueden
ver sus características en la web. En el capítulo 2 del Book de NLTK viene incluso una implementación.
Para construir un puzzle interesante, o para obtener todas las palabras permitidas por uno concreto,
necesitamos (i) una gran base de datos léxica, y (ii) un programa.
1. (1 point) La base de datos léxica vamos a obtenerla del Corpus de Referencia del Español Actual.
Descargar la lista total de frecuencias de la web de la RAE. En Python, abrir el
fichero, obtener las palabras y guardarlas en una variable cuyo contenido pueden guardar en un fichero para
usos posteriores.
2. (2 points) Construir una función para que, dados (i) un puzzle cuyas 9 letras son introducidas por el
usuario desde el teclado, y (ii) la base de palabras del CREA, se obtengan todas las palabras posibles
de acuerdo a las reglas del puzzle.
No copiar la implementación del NLTK, ni ninguna de las miles que existen en la red.
3. (2 points) Soundex es un algoritmo para representar nombres. Si no lo conoce, lea sus reglas en la web.
Escribir en la forma de script una implementación de Soundex adaptado al español. El usuario escribe
por teclado un nombre y le devuelve el resultado."""

texto=open("C:/Users/Adrián/Desktop/Asignaturas/Computacional - 9-6/2020-2021/Ejercicios/CREA_total.txt", mode="r", encoding="ANSI")
texto=texto.read()
import re
from nltk import FreqDist
palabras=texto.split( )
palabras=re.findall("[a-zA-Z]+",texto)
len(palabras)
palabras=list(set(palabras))#Con esto se eliminan los elementos repetidos de una lista,
#pero para que no se pase a tipo de datos set y siga siendo una lista declaramos list,
#y seguirá siendo una lista.
len(palabras)
def puzzledeletras():
    """Con esta función se resolverá un puzzle previamente dado por el usuario con las palabras del CREA que hemos importado"""
	letras=input("Por favor, selecciona 8 letras para empezar el puzzle.\n")#Al usar input pedimos unos datos al usuario.
	letraobligatoria=input("Por favor, ahora elija una letra obligatoria al puzzle\n")
	letrasdelpuzzle=nltk.FreqDist(letras+letraobligatoria)
	_letraobligatoria_=letraobligatoria
	listadepalabras=palabras
	for palabra in listadepalabras:#Con este buble creamos las normas del puzzle y lo resolvemos con el nltk.FreqDist
		if len(palabra)>=6:
			if _letraobligatoria_:
				nltk.FreqDist(palabra)<=letrasdelpuzzle
	return letrasdelpuzzle
"""(100 points) La tarea consiste en escribir un script en el que el usuario introduzca por teclado (i) la
ruta y nombre del chero de Fortunata y Jacinta y (ii) un número n. El programa tiene que escribir
en pantalla las n palabras más frecuentes en el formato: número de orden, palabra, frecuencia absoluta,
frecuencia relativa.
Para determinar las palabras usen split().
Seleccionen sólo las palabras con caracteres alfabéticos y normalicen a minúsculas. Realicen estas dos
operaciones usando una list comprehension.
Cuenten las palabras con Counter del módulo collections. Así pueden usar most_common(n)
Remitir el script como chero de texto primerapellido_segundoapellido.py"""
def contarpalabras():
    from collections import Counter
    ruta= input("Por favor, introduce la ruta del fichero de Fortunata y Jacinta (trate que sea un documento utf-8). \n")
    n= input("Por favor, introduce el número de palabras que quiere ver. \n")
    texto= open(ruta, mode="r", encoding="utf-8")
    texto=texto.read()
    texto=texto.lower()
    texto=Counter(texto.split())
    palabras=texto.most_common(n)
    return palabras
"""1. (1 point) Para que el texto quede justicado por la derecha, a veces hay que romper una palabra con
un guión.
1. Escribir una expresión regular que identique todas y sólo las palabras rotas por guión al nal de
línea.
2. Escribir código para obtener las palabras originales eliminando el guión."""
mport re
texto=open("C:/Users/Adrián/Desktop/Asignaturas/Computacional - 9-6/2020-2021/Ejercicios/Fortunata_y_Jacinta.txt", mode="r", encoding="utf-8")
texto=texto.read()
texto=str(re.findall(r"\w+-\w+", texto))
palabrassinguion=texto.replace("-", "")

"""1. (100 points) Si abren el texto de Fortunata y Jacinta en un editor de texto, verán que los renglones no
están justicados por la derecha. Cada línea tiene distinta longitud.
Las noticias más remotas que tengo de la persona que lleva este nombre
me las ha dado Jacinto María Villalonga, y alcanzan al tiempo en que
este amigo mío y el otro y el de más allá, Zalamero, Joaquinito Pez,
Alejandro Miquis, iban a las aulas de la Universidad. No cursaban todos
el mismo año, y aunque se reunían en la cátedra de Camús, separábanse en
la de Derecho Romano: el chico de Santa Cruz era discípulo de Novar, y
Villalonga de Coronado. Ni tenían todos el mismo grado de aplicación:
Zalamero, juicioso y circunspecto como pocos, era de los que se ponen en
la primera fila de bancos, mirando con faz complacida al profesor
mientras explica, y haciendo con la cabeza discretas señales de
asentimiento a todo lo que dice. Por el contrario, Santa Cruz y
A veces se requiere que el texto esté justicado por la derecha. Un texto justicado de aspecto profesional
tiene que usar guiones para dividir palabras largas y evitar así demasiados espacios en blanco. Pero
guionar correctamente exige contar con un silabicador. En su ausencia, vamos a justicar el texto de
la forma más razonable.
En un texto justicado todas las líneas (i) tienen la misma longitud, (ii) no pueden empezar ni terminar
con espacios, (ii) los espacios en blanco entre palabras están uniformemente repartidos (no pueden estar
todos los espacios entre dos palabras).
Estas son las primeras 10 líneas del texto justicado con una anchura de 70 caracteres por línea:
Las noticias más remotas que tengo de la persona que lleva este nombre
me las ha dado Jacinto María Villalonga, y alcanzan al tiempo en que
este amigo mío y el otro y el de más allá, Zalamero, Joaquinito Pez,
Alejandro Miquis, iban a las aulas de la Universidad. No cursaban
todos el mismo año, y aunque se reunían en la cátedra de Camús,
separábanse en la de Derecho Romano: el chico de Santa Cruz era
discípulo de Novar, y Villalonga de Coronado. Ni tenían todos el mismo
grado de aplicación: Zalamero, juicioso y circunspecto como pocos, era
de los que se ponen en la primera fila de bancos, mirando con faz
complacida al profesor mientras explica, y haciendo con la cabeza
Tarea: escribir un script para justicar texto. El usuario debe poder introducir (i) el nombre del chero
de texto (digamos: fichero.txt) y (ii) el número de caracteres para cada línea. El script no tiene
salida de datos en pantalla, sino que escribe en un nuevo chero (fichero_justificado.txt) el texto
justicado"""

def justificartexto():
	texto=input("Introduzcs el nombre del fichero donde este el texto.\n")
	numero=input("Introduzca el numero de caracteres que quiere que aparezca en cada linea.\n")
	texto_justificado=texto.ljust(numero, "")
	return texto_justificado.close()
""" (10 points) Descargar el corpus Brown en formato raw. Escribir una expresión regular para obtener las
palabras del corpus."""
import nltk
nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
import re
[a-zA-Z´&á-ú]+#Esta es la RE para sacar palabras del corpus Brown.
"""(10 points) El corpus Brown está etiquetado y analizado por lingüistas. La forma que tiene cuando se
descarga es así:
For/in the/at first/od time/nn in/in history/nn ,/, the/at U.S./np has/hvz
produced/vbn a/at society/nn in/in which/wdt less/ap than/in
one-tenth/nn of/in the/at people/nns turn/vb out/rp so/ql much/ap
food/nn that/cs the/at Government's/nn$-tl most/ql embarrassing/vbg
problem/nn is/bez how/wrb to/to dispose/vb inconspicuously/rb
of/in 100/cd million/cd tons/nns of/in surplus/nn farm/nn produce/nn ./.
NLTK tiene un método (raw) que nos da todo el texto del corpus en su forma original. También tiene
otro método (words) que permite obtener las palabras. Aparentemente es una lista, pero si examinan el
tipo les dice que es:
<class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>
En realidad las palabras del corpus se pueden obtener mediante una expresión regular. La tarea consiste
en escribir una expresión regular para obtener las palabras del corpus a partir del texto original completo
obtenido con raw.
Pueden usar las palabras que se obtienen con words para comparar el resultado de su expresión regular.
Su expresión regular estará bien cuando se obtengan con ella exactamente las palabras que se obtienen
con words."""
from nltk.corpus import brown
brown.words()
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
[a-zA-Z´&á-ú]+

>>> def nombreyedad():
	a= input("Dígame su nombre \n")
	if a=="":
		a= input("Por favor, inserte su nombre \n")

		

>>> def nombreyedad():
	a= input("Dígame su nombre \n")
	if a=="":
		a= input("Por favor, inserte su nombre \n")
	while a=="":
		a= input("Por favor, inserte su nombre \n")
		
	return print("Muchas gracias")

>>> def nombreyedad():
	import re
	a= input("Dígame su nombre \n")
	if a=="":
		a= input("Por favor, inserte su nombre \n")
	while a=="":
		a= input("Por favor, inserte su nombre \n")
	b= input("Ahora, dígame su edad en números \m")
	if b=="" or b==re.match("(?:[A-Za-z]+)")
		b= input("Por favor, inserte su edad con números \n")
	while b=="" or b==re.match("(?:[A-Za-z]+)")
		b= input("Por favor, inserte su edad con número \n")
		
	return print("Muchas gracias")
SyntaxError: invalid syntax
>>> def nombreyedad():
	import re
	a= input("Dígame su nombre \n")
	if a=="":
		a= input("Por favor, inserte su nombre \n")
	while a=="":
		a= input("Por favor, inserte su nombre \n")
	b= input("Ahora, dígame su edad en números \m")
	if b=="" or b==re.match("(?:[A-Za-z]+)"):
		b= input("Por favor, inserte su edad con números \n")
	while b=="" or b==re.match("(?:[A-Za-z]+)"):
		b= input("Por favor, inserte su edad con número \n")
		
	return print("Muchas gracias")

>>> a= ["manzana", "pera", "melocoton", "albaricoque"]
>>> a.sort()
>>> print(a)
['albaricoque', 'manzana', 'melocoton', 'pera']
>>> a= {"profesor1":"Paco",
    "profesor2":"Miguel",
    "profesor3":"Jose"}
>>> print(a)
{'profesor1': 'Paco', 'profesor2': 'Miguel', 'profesor3': 'Jose'}
>>> a="Me voy a pedir dos pizzas: una pepperoni, otra con carrillada y otra cuatro quesos"
>>> b=a.split()
>>> len(b) in  range"carrillada"
SyntaxError: invalid syntax
>>> b.index("carrillada")
10
>>> b.remove("carrillada") insert("piña")
SyntaxError: invalid syntax
>>> """La posición 10 de b es igual a "piña"""
'La posición 10 de b es igual a "piña'
>>> b[10]="piña"
>>> print(b)
['Me', 'voy', 'a', 'pedir', 'dos', 'pizzas:', 'una', 'pepperoni,', 'otra', 'con', 'piña', 'y', 'otra', 'cuatro', 'quesos']
>>> b.remove("piña")
>>> print(b)
['Me', 'voy', 'a', 'pedir', 'dos', 'pizzas:', 'una', 'pepperoni,', 'otra', 'con', 'y', 'otra', 'cuatro', 'quesos']
>>> b[10].append("piña")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b[10].append("piña")
AttributeError: 'str' object has no attribute 'append'
>>> b.append(["piña"])[10]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    b.append(["piña"])[10]
TypeError: 'NoneType' object is not subscriptable
>>> b.append"piña"
SyntaxError: invalid syntax
>>> b.append("piña")
>>> print(b)
['Me', 'voy', 'a', 'pedir', 'dos', 'pizzas:', 'una', 'pepperoni,', 'otra', 'con', 'y', 'otra', 'cuatro', 'quesos', ['piña'], 'piña']
>>> b.remove(["piña"])
>>> print(b)
['Me', 'voy', 'a', 'pedir', 'dos', 'pizzas:', 'una', 'pepperoni,', 'otra', 'con', 'y', 'otra', 'cuatro', 'quesos', 'piña']
>>> b.insert(10, "piña")
>>> print(b)
['Me', 'voy', 'a', 'pedir', 'dos', 'pizzas:', 'una', 'pepperoni,', 'otra', 'con', 'piña', 'y', 'otra', 'cuatro', 'quesos', 'piña']
>>> b.pop()
'piña'
>>> print(b)
['Me', 'voy', 'a', 'pedir', 'dos', 'pizzas:', 'una', 'pepperoni,', 'otra', 'con', 'piña', 'y', 'otra', 'cuatro', 'quesos']
>>> b.pop(3)
'pedir'
>>> print(b)
['Me', 'voy', 'a', 'dos', 'pizzas:', 'una', 'pepperoni,', 'otra', 'con', 'piña', 'y', 'otra', 'cuatro', 'quesos']
>>> b[::-1]
['quesos', 'cuatro', 'otra', 'y', 'piña', 'con', 'otra', 'pepperoni,', 'una', 'pizzas:', 'dos', 'a', 'voy', 'Me']
>>> c=1231231
>>> c
1231231
>>> type(c)
<class 'int'>
>>> c[::-1]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c[::-1]
TypeError: 'int' object is not subscriptable
>>> d="caca"
>>> d[::-1]
'acac'
>>> e={"profesor1":"Paco"}
>>> e[::-1]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    e[::-1]
TypeError: unhashable type: 'slice'
>>> f=("falla","Cuerno")
>>> f[::-1]
('Cuerno', 'falla')
>>> g=1,23123123
>>> g
(1, 23123123)
>>> type(g)
<class 'tuple'>
>>> g=141.2333
>>> type(g)
<class 'float'>
>>> g[::-1]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    g[::-1]
TypeError: 'float' object is not subscriptable
>>> #La función [::-1] para hacer un cambio de sentido es
#posible en tuplas, listas, strings. Diccionarios, floats e int no lo soportan.
"""E.R. para link https://+\w+.[\w]+/"""
