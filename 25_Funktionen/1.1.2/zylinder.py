def zylinder_volumen(radius, hoehe):
    return radius**2*hoehe

radius=float(input("Zylinderradius: "))
hoehe=float(input("Zylinderhöhe: "))
volumen=zylinder_volumen(radius, hoehe)
print("Das Volumen ist %6.2f"%(volumen))
