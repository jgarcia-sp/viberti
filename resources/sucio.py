

texto=open("C:/Users/Jonathan/Desktop/viterbi/resources/Fortunata_y_Jacinta.txt", mode="r", encoding="utf-8")
texto=texto.read()
import re #Ahora hemos importado el módulo para trabjar
#con Expresiones Regulares (regular expressions)
m = re.findall("(?<![.])[¿ !(\"'<-][ÁÉÍÓÚA-Z][aáéíóúa-z]+",texto)
#re.findall toma la expresión regular y
#busca aquellos patrones coincidentes con dicha expresión regular en la variable
#seleccionada - texto en este caso - y nos devuelve una lista.
print(m[:1000])
