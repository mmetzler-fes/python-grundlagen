import math
def vektor_einlesen():
    n=int(input("Anzahl der Vektor-Dimensionen n="))
    if n<1:
        print ("Fehler - mindestens 1 Dimension")
        return None
    vektor=[]
    for i in range(n):
        text="Dimension ("+str(i+1)+"): "
        vektor.append(int(input(text)))
    return vektor

def abstand(x, y):
    differenz=[]
    abstand=0
    for i in range(len(x)):
        differenz.append(y[i]-x[i])
        abstand+=math.sqrt(differenz[i]**2)
    return differenz, abstand

x=vektor_einlesen()
y=vektor_einlesen()
if len(x)!=len(y) or x==None or y==None:
    print("Falsche Eingabe")
else:
    differenz, abstand = abstand(x,y)
    print("Differenzvektor: ",differenz)
    print("Abstand: ",abstand)



