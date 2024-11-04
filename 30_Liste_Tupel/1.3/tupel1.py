import math
def abstand(x, y):
    differenz=[]
    abstand=0
    for i in range(len(x)):
        differenz.append(y[i]-x[i])
        abstand+=math.sqrt(differenz[i]**2)
    return differenz, abstand

x=(1,2,3)
y=(-1,2,2)
ergebnis=abstand(x,y)
print("Differenzvektor: ",ergebnis[0])
print("Abstand: ",ergebnis[1])

