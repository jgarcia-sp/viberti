Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio nº1
>>> import re
>>> with open("C:/Users/fdes2/Dropbox/Suryà Works/UCA/2º Año/2º Semestre/Lingüística Computacional/Prácticas/Entrega 1/novelas/isla del tesoro.txt",'r',encoding='utf8') as f:
	txt1=f.read()

	
>>> with open("C:/Users/fdes2/Dropbox/Suryà Works/UCA/2º Año/2º Semestre/Lingüística Computacional/Prácticas/Entrega 1/novelas/treasure island.txt",'r',encoding='utf8') as f:
	txt2=f.read()

	
>>> texto1=re.findall(r"\w+",txt1)
>>> texto2=re.findall(r"\w+",txt2)
>>> #Bucle for:
>>> texto_alineado=[]
>>> for x in range(min(len(texto1),len(texto2))):
		       texto_alineado.append((texto1[x],texto2[x]))

		       
>>> texto_alineado[:10]
[('LA', 'TREASURE'), ('ISLA', 'ISLAND'), ('DEL', 'by'), ('TESORO', 'Robert'), ('La', 'Louis'), ('Guardia', 'Stevenson'), ('Blanca', 'TREASURE'), ('Es', 'ISLAND'), ('el', 'To'), ('título', 'S')]
>>> #Lista de Comprensión:
>>> texto_alineado=[(texto1[x],texto2[x]) for x in range(min(len(texto1),len(texto2)))]
>>> texto_alineado[:10]
[('LA', 'TREASURE'), ('ISLA', 'ISLAND'), ('DEL', 'by'), ('TESORO', 'Robert'), ('La', 'Louis'), ('Guardia', 'Stevenson'), ('Blanca', 'TREASURE'), ('Es', 'ISLAND'), ('el', 'To'), ('título', 'S')]
>>> #Ejercicio nº2
>>> #	Entre estas dos líneas de comandos la diferencia está en el orden en que se aplican las funciones:
>>> #	En "sorted(set(w.lower() for w in text))", el primer paso es convertir todos los elementos de "text" a minúscula utilizando "w.lower()" además de un bucle "for" . En segundo lugar, se transforma la lista de elementos ya en minúscula a conjunto, eliminando así las palabras que estuvieran repetidas. En tercer y último lugar, todos los elementos se ordenan alfabéticamente con la función "sorted()".
>>> #	En "sorted(w.lower() for w in set(text))", el primer paso es hacer un conjunto de "text" (si no hay elementos iguales, estos permanecen igual solo que pueden estar desordenados). A continuación, convierte todos los elementos del conjunto a minúscula (con "w.lower" y bucle "for"). Por último, los elementos del conjunto pasados posteriormente a minúscula se ordenan alfabéticamente.
>>> text=['Ante','ante','bajo','Bajo','Con','Desde','desde','En','Entre']
>>> sorted(set(w.lower() for w in text))
['ante', 'bajo', 'con', 'desde', 'en', 'entre']
>>> sorted(w.lower() for w in set(text))
['ante', 'ante', 'bajo', 'bajo', 'con', 'desde', 'desde', 'en', 'entre']
>>> #Ejercicio nº3
>>> #	“x.isupper()” no es igual a “not x.islower()” debido a que tanto "x.islower()" como "x.isupper()" con una palabra con letras en mayúsculas y minúsculas dan negativo. Al usar “not x.islower()” el resultado es positivo por estar invirtiendo el resultado de “x.islower()”, que en este caso sería negativo porque “Hola” no tiene todas las letras en minúscula.
>>> y='hola'
>>> y.isupper()
False
>>> y.islower()
True
>>> not y.islower()
False
>>> not y.isupper()
True
>>> x='Hola'
>>> x.isupper()
False
>>> x.islower()
False
>>> not x.islower()
True
>>> not x.isupper()
True
>>> #Ejercicio nº4
>>> #	Teniendo x=set(sorted(texto)) y z=(sorted(set(texto)), x no es igual a z por el orden en que se ejecutan las funciones. x ordena alfabéticamente la variable ‘texto’ y entonces lo convierte en un conjunto, desordenando los elementos que contiene. z en primer lugar hace un conjunto con los elementos de ‘texto’ y entonces los ordena alfabéticamente. Además, x es una variable tipo conjunto, mientras que z es una variable tipo lista.
>>> texto=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
>>> x=set(sorted(texto))
>>> x
{'Viernes', 'Sábado', 'Miércoles', 'Lunes', 'Martes', 'Jueves', 'Domingo'}
>>> z=sorted(set(texto))
>>> z
['Domingo', 'Jueves', 'Lunes', 'Martes', 'Miércoles', 'Sábado', 'Viernes']
>>> #Ejercicio nº5
>>> from os import listdir
>>> ruta='C:/Users/fdes2/Dropbox/Suryà Works/UCA/2º Año/2º Semestre/Lingüística Computacional/Prácticas/Entrega 1/novelas/'
>>> libros=listdir(ruta)
>>> textos=[]
>>> for x in libros:
	f=open(ruta+x,'r',encoding='utf8')
	textos.append(f.read())
	f.close

	
<built-in method close of _io.TextIOWrapper object at 0x02FEB3B0>
<built-in method close of _io.TextIOWrapper object at 0x02FEB5B0>
<built-in method close of _io.TextIOWrapper object at 0x02FEB3B0>
<built-in method close of _io.TextIOWrapper object at 0x02FEB5B0>
>>> big_text=textos[0]
>>> for x in range(1,len(textos)):
	big_text=big_text+textos[x]

	
>>> type(big_text)
<class 'str'>
>>> big_text[:50]
'\ufeff                          LA ISLA DEL TESORO\n\n   '
>>> #Ejercicio nº6
>>> def líneas_en_blanco(texto):
	"""esta función te da el nº de líneas en blanco de un texto (string)"""
	txt1=texto.split('\n')
	counter=0
	for x in txt1:
		if len(x)==0:
			counter+=1
	return(counter)

>>> with open('C:/Users/fdes2/Desktop/alvarez_memorias.txt','r',encoding='utf8') as s:
	texto_memorias=s.read()

	
>>> líneas_en_blanco(texto_memorias)
856
>>> 
