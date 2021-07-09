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
