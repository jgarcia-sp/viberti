Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> text1=nltk.corpus.brown.tagged_words(tagset='universal')
>>>  def funcion_emis_transm(texto,numero,palabras):
	
SyntaxError: unexpected indent
>>> def funcion_emis_transm(texto,numero,palabras):
	"""Calcula las probabilidades de emisión y trasmisión de un texto etiquetado.
	Ambas probabilidades se devuelven como diccionario"""
	import collections,re
	from decimal import Decimal,getcontext
	getcontext().prec=numero
	text2=text1[:palabras]
	text2=[(a.lower,b)for (a,b)in text2]
	tags=[w[1] for w in text2]
	frec_tags=collections.Counter(tags)
	frec_tags1=frec_tags.most_common()
	frec_bi=collections.Counter(text2)
	frec_bi1=frec_bi.most_common()
	pal_cat=[w[0]for w in frec_bi1]
	pal=[w[0]for w in pal_cat]
	cat=[w[1]for w in pal_cat]
	frec_pal=[w[1]for w in frec_bi1]
	nppal=[w[1]for w in frec_tags1]
	prob_em=collections.defaultdict(lambda:0)
	for x in range(len(frec_bi1)):
		z=re.match(cat[x],'NOUN')
		y=re.match(cat[x],'VERB')
		w=re.match(cat[x],'.')
		v=re.match(cat[x],'ADP')
		r=re.match(cat[x],'DET')
		e=re.match(cat[x],'ADJ')
		zy=re.match(cat[x],'ADV')
		rv=re.match(cat[x],'PRON')
		ww=re.match(cat[x],'CONJ')
		wy=re.match(cat[x],'PRT')
		zz=re.match(cat[x],'NUM')
		q=re.match(cat[x],'X')
		if z:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[0])))
		elif y:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[1])))
		elif w:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[2])))
		elif v:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[3])))
		elif r:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[4])))
		elif e:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[5])))
		elif zy:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[6])))
		elif rv:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[7])))
		elif ww:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[8])))
		elif wy:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[9])))
		elif zz:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[10])))
		elif q:
			prob_em[x]=(pal_cat[x],(Decimal(frec_pal[x])/Decimal(nppal[11])))
	print(prob_em)
	bi_cat=[]
	text2.insert(0,('.','.'))
	for x in range(len(text2)-1):
		a,b=text2[x]
		c,d=text2[x+1]
		bi_cat.append((b,d))
	frec_tr=collections.Counter(bi_cat)
	prob_tr=collections.defaultdict(lambda:0)
	for x in frec_tr.keys():
		a,b=x
		prob_tr[x]=Decimal(frec_tr[x])/Decimal(frec_tags[a])
	print(prob_tr)

	
>>> funcion_emis_transm(text1,20,30)
defaultdict(<function funcion_emis_transm.<locals>.<lambda> at 0x041A64F8>, {0: ((<built-in method lower of str object at 0x0469E2A0>, 'DET'), Decimal('0.33333333333333333333')), 1: ((<built-in method lower of str object at 0x0469E2C0>, 'NOUN'), Decimal('0.083333333333333333333')), 2: ((<built-in method lower of str object at 0x0469E260>, 'NOUN'), Decimal('0.083333333333333333333')), 3: ((<built-in method lower of str object at 0x0469E3E0>, 'ADJ'), Decimal('0.5')), 4: ((<built-in method lower of str object at 0x0469E4A0>, 'NOUN'), Decimal('0.083333333333333333333')), 5: ((<built-in method lower of str object at 0x0469E5C0>, 'VERB'), Decimal('0.2')), 6: ((<built-in method lower of str object at 0x0469E620>, 'NOUN'), Decimal('0.083333333333333333333')), 7: ((<built-in method lower of str object at 0x0469E600>, 'DET'), Decimal('0.33333333333333333333')), 8: ((<built-in method lower of str object at 0x041B02F0>, 'NOUN'), Decimal('0.083333333333333333333')), 9: ((<built-in method lower of str object at 0x0469E540>, 'ADP'), Decimal('0.33333333333333333333')), 10: ((<built-in method lower of str object at 0x041B0408>, 'NOUN'), Decimal('0.083333333333333333333')), 11: ((<built-in method lower of str object at 0x0469E120>, 'ADJ'), Decimal('0.5')), 12: ((<built-in method lower of str object at 0x0469E6E0>, 'NOUN'), Decimal('0.083333333333333333333')), 13: ((<built-in method lower of str object at 0x041B0430>, 'NOUN'), Decimal('0.083333333333333333333')), 14: ((<built-in method lower of str object at 0x041B0458>, 'VERB'), Decimal('0.2')), 15: ((<built-in method lower of str object at 0x0469E720>, '.'), Decimal('0.083333333333333333333')), 16: ((<built-in method lower of str object at 0x0469E7E0>, 'DET'), Decimal('0.33333333333333333333')), 17: ((<built-in method lower of str object at 0x041B0480>, 'NOUN'), Decimal('0.083333333333333333333')), 18: ((<built-in method lower of str object at 0x0469E840>, '.'), Decimal('0.083333333333333333333')), 19: ((<built-in method lower of str object at 0x0469E8E0>, 'ADP'), Decimal('0.33333333333333333333')), 20: ((<built-in method lower of str object at 0x0469E940>, 'DET'), Decimal('0.33333333333333333333')), 21: ((<built-in method lower of str object at 0x041B04A8>, 'NOUN'), Decimal('0.083333333333333333333')), 22: ((<built-in method lower of str object at 0x0469E9A0>, 'VERB'), Decimal('0.2')), 23: ((<built-in method lower of str object at 0x0469EA60>, 'NOUN'), Decimal('0.083333333333333333333')), 24: ((<built-in method lower of str object at 0x0124A320>, '.'), Decimal('0.083333333333333333333')), 25: ((<built-in method lower of str object at 0x0469EA00>, 'DET'), Decimal('0.33333333333333333333')), 26: ((<built-in method lower of str object at 0x0469EA40>, 'NOUN'), Decimal('0.083333333333333333333')), 27: ((<built-in method lower of str object at 0x0469EAC0>, 'ADV'), Decimal('1')), 28: ((<built-in method lower of str object at 0x0469EB40>, 'VERB'), Decimal('0.2')), 29: ((<built-in method lower of str object at 0x0469EBC0>, 'ADP'), Decimal('0.33333333333333333333'))})
defaultdict(<function funcion_emis_transm.<locals>.<lambda> at 0x041A66F0>, {('.', 'DET'): Decimal('1'), ('DET', 'NOUN'): Decimal('1'), ('NOUN', 'NOUN'): Decimal('0.16666666666666666667'), ('NOUN', 'ADJ'): Decimal('0.16666666666666666667'), ('ADJ', 'NOUN'): Decimal('1'), ('NOUN', 'VERB'): Decimal('0.25'), ('VERB', 'NOUN'): Decimal('0.5'), ('NOUN', 'DET'): Decimal('0.083333333333333333333'), ('NOUN', 'ADP'): Decimal('0.083333333333333333333'), ('ADP', 'NOUN'): Decimal('0.33333333333333333333'), ('VERB', '.'): Decimal('0.25'), ('NOUN', '.'): Decimal('0.16666666666666666667'), ('.', 'ADP'): Decimal('0.33333333333333333333'), ('ADP', 'DET'): Decimal('0.33333333333333333333'), ('NOUN', 'ADV'): Decimal('0.083333333333333333333'), ('ADV', 'VERB'): Decimal('1'), ('VERB', 'ADP'): Decimal('0.25')})
>>> 
