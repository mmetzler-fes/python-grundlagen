import random
lottozahlen=[]
for i in range(49):
    lottozahlen.append(i+1)
ziehung=[]
for i in range(6):
    index=random.randint(0,len(lottozahlen))
    ziehung.append(lottozahlen[index])
    del(lottozahlen[index])
index=random.randint(0,len(lottozahlen))
zusatzzahl=lottozahlen[index]
ziehung.sort()
print("Zahlen: ")
print (ziehung)
print("Zusatzzahl: "+str(zusatzzahl))   
