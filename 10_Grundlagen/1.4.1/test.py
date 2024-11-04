spielstand = [[1,0,2],[1,2,0],[2,0,1]]
gewinner=0

def pruefeTicTacToe(spielstand):
    vektoren=[]
    for i in range(3):
        vektoren.append([spielstand[i][0], spielstand[i][1], spielstand[i][2]] ) #Zeile hinzufügen
        vektoren.append([spielstand[0][i], spielstand[1][i], spielstand[2][i]]) #Spalte hinzufügen
    #Diagonalen hinzufügen
    vektoren.append([spielstand[0][0],spielstand[1][1],spielstand[2][2]])
    vektoren.append([spielstand[2][0],spielstand[1][1],spielstand[0][2]])
    for vektor in vektoren:
        print (vektor)
        gewinner=pruefeVektor(vektor)
        if(gewinner!=0):
            return gewinner
    return 0

def pruefeVektor(vektor):
    if (vektor[0]==vektor[1] and vektor[0]==vektor[2]):
        return vektor[0]
    else:
        return 0
 
gewinner= pruefeTicTacToe(spielstand)
if (gewinner!=0):
   print("Gewinner ist Spieler %s"%(gewinner))


    

        
             
        