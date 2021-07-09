""" (10 points) Descargar el corpus Brown en formato raw. Escribir una expresión regular para obtener las
palabras del corpus."""
import nltk
nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
import re
[a-zA-Z´&á-ú]+#Esta es la RE para sacar palabras del corpus Brown.
