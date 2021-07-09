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
