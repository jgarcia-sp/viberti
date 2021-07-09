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
