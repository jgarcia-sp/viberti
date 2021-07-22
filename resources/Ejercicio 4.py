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
    cadena = ""
    for ps in datos:
        cadena += ps
        
        if type(ps) == type("str"):
            datosseleccionados=[]
            datosseleccionados.append(ps)
            return datosseleccionados

print(corpora("C:/Users/Jonathan/Desktop/viterbi/resources/Corpus"))
#Al declarar esto nos dará la información alojada en C en ordenador.

print(time.time())
