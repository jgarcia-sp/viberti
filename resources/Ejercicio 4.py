import time
print(time.time())
import os
#Se importa el módulo os que sirve para trabajr con los directorios y carpetas del ordenador.
def corpora(ruta):
    lista_final=[]
    x=os.listdir(ruta)
    lista_de_los_nombres=x
    for nombre_fichero in lista_de_los_nombres:
        fichero_abierto=open(ruta+nombre_fichero, "r")#open es una función
        fichero_leido=fichero_abierto.read()
        lista_final.append(fichero_leido)
    return lista_final     

print(corpora("C:/Users/Jonathan/Desktop/viterbi/resources/Corpus/"))
#Al declarar esto nos dará la información alojada en C en ordenador.

print(time.time())

input("Pulsa una tecla para continuar\n")
