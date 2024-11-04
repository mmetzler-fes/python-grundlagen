import random
x=random.random()
zahl=int(x*10)+1
versuche=0
while True:
    eingabe=input("Rate meine Zahl zwischen 1 und 10: ")
    versuche+=1
    if zahl>int(eingabe):
        print("Meine Zahl ist größer")
    elif zahl<int(eingabe):
        print("Meine Zahl ist kleiner")
    else:
        print("Super. Richtig geraten in %d Versuchen"%(versuche))
        break
    
    
