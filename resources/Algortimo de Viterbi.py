Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def viterbi(texto, prob_trans, prob_emis):
    V=[{}]
    palabras=texto.split()
    #Vamos a usar las etiquetas del Universal POS tags pq están más condensadas. Según Iván Arias Rodríguez, experto sistemas de etiquetación, "el tagset (de Corpus Brown) es un tanto extraño, con poca estructura interna
    #y con algunas etiquetas poco ortodoxas: palabras en título, titular, cita (etiqueta postpuesta a la etiqueta principal unida con el guion). Hay pocos símbolos. Las palabras extranjeras reciben una etiqueta principal
    #y se le antepona la etiqueta FW unida con el guion.
    etiquetas=['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X']
    for i in etiquetas:
            V[0][i]=prob_trans[i]*prob_emis[i][texto[0]]
    #Para la longitud de las palabras de texto y crear las dos tablas que almacenaran las probabilidades.
    for j in range(1, len(texto)):
        V.append({})
        for k in etiquetas:
            (prob, tag) = max((V[j-1][k0] * prob_trans[k0][k] * prob_emis[k][texto[j]], k0) for k0 in etiquetas)
            #Con esta línea de código compleja vamos a condensar lo siguiente: 
            #designamos la probabilidad y el etiquetado que funciona de la siguiente manera
            #la prob max de j empezara en menos 1 pq empezaremos desde la derecha si estuviesemos en pseudocodigo
            #k empieza en 0 porq es la parte que empezara desde la izquierda porque es la probabilidad en si (es la que tiene que llegar a la prob maxima)
            #multiplicamos los valores por la prob_trans y por la prob_emis Eso se recorre en K0 dentro de las etiquetas. 
            V[j][k] = prob
            #rellenar las filas y las columnas de la tabla
        combinaciones=[]
        for l in V:
            for x,k in l.items()
            #para genera una lista en clave-valor de los registros del diccionario
                if l[x]==max(j.values()):
                #values para generar una lista en valor de los registros del diccionario
                    combinaciones.append(x)
        #Obtenemos la secuencia más probable de categorias que haya dentro de V
    #Para obtener la secuencia más alta.
    smp = max(V[-1].values())

    return print('La secuencia de etiquetas es '+' '.join(combinaciones)+'con mayor probabilidad es')
    #Devuelve una tabla con la secuencia de etiquetas más probable.
