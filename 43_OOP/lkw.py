class Fahrzeug:
    kilometerstand=0
    
    def __init__(self, marke):
        self.marke = marke

    def fahre(self, strecke):
        self.kilometerstand+=strecke
        return f"{self.marke} fährt {strecke} km."
    
    def ausgabe_kilometerstand(self):
        print(f"{self.marke}, Kilometerstand: {self.kilometerstand} km")

class Auto(Fahrzeug):
    def __init__(self, marke, modell):
        super().__init__(marke)
        self.modell = modell

    def hupen(self):
        return f"{self.marke} {self.modell} hupt: Honk! Honk!"

class LKW(Auto):
    def __init__(self, marke, modell, maxgewicht):
        super().__init__(marke, modell)
        self.maxgewicht= maxgewicht
        
# Objektinstanzierung
mein_auto = Auto("Toyota", "Camry")
dein_auto = Auto("Mercedes", "E300")
# Code-Ausgabe
dein_auto.fahre(200)
dein_auto.fahre(150)
dein_auto.ausgabe_kilometerstand()
print(mein_auto.fahre(100))
print(mein_auto.hupen())
print(mein_auto.fahre(200))
mein_auto.ausgabe_kilometerstand()
print(dein_auto.hupen())

lkw1=LKW("Daimler","xy",1000)
print(lkw1.fahre(500))
print(lkw1.hupen())
