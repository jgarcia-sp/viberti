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
