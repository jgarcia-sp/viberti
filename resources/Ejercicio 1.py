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
