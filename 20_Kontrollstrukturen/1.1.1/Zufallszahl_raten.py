import random
x=random.random()
zahl=int(x*10)+1
eingabe=input("Rate meine Zahl zwischen 1 und 10: ")
if zahl>int(eingabe):
    print("Meine Zahl ist größer")
elif zahl<int(eingabe):
    print("Meine Zahl ist kleiner")
else:
    print("Super. Richtig geraten")
step=2; start=1; end=10
for i in range(start,end,step):
    print(i)
    
    
