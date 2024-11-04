def liste_namen(*args):
	ergebnis=[]
	for element in args:
		ergebnis.append(element)
	return ergebnis

liste=liste_namen("Martin", "Hans", "Fritz", "Heinz")
print (liste)
