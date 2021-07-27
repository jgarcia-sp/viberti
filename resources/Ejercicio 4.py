import time
"""print(time.time())"""
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
    for ps in datos:
        #la variable ps tiene el valor de: la iteración primera -en este momento- dentro de la lista que contiene
        #las cadenas de los nombres de los archivos dentro del directorio alojados previamente en datos.
        #La variable cadena contiene una cadena vacia.
        #La variable lectura contiene nada porque no sé qué poner.
        lectura=open(ruta+ps,"r")
        lectura1=lectura.read()
        resultado=lectura1
        return resultado
        

print(corpora("C:/Users/Jonathan/Desktop/viterbi/resources/Corpus/"))
#Al declarar esto nos dará la información alojada en C en ordenador.

"""print(time.time())"""
