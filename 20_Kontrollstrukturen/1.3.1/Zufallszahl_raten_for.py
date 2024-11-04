import random
x=random.random()
zahl=int(x*10)+1
erfolg=False
for versuche in range(1,6):
    eingabe=input("Rate meine Zahl zwischen 1 und 10: ")
    versuche+=1
    if zahl>int(eingabe):
        print("Meine Zahl ist größer")
    elif zahl<int(eingabe):
        print("Meine Zahl ist kleiner")
    else:
        print("Super. Richtig geraten in %d Versuchen"%(versuche))
        erfolg=True
        break
if not erfolg:
    print("Du hast das Spiel leider verloren")

    
