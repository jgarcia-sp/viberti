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
