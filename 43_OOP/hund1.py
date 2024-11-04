

class Hund:
    def __init__(self, name, alter):
        self.name=name
        self.alter=alter
    
    def print(self):
        print(f"Name: {self.name}, Alter: {self.alter} Jahre")
        
    def laufe(self):
        print(f"{self.name} läuft...")
    
    def print_alter(self):
        print(f"Alter: {self.alter}")
        
hund1=Hund("Toby",3)
hund2=Hund("Max",4)
hund1.print()
hund1.laufe()
hund2.print_alter()
