import PySimpleGUI as sg

# In dieser Funktion wird die eigentliche Berechung durchgeführt.
# Aufruf der Funktion durch Klick auf die Schaltfläche
# In dieser Funktion wird die Umrechnung durchgeführt => hier programmieren
def verdoppeln(zahl):
    return 2*zahl


# Hier beginnt das Hauptprogramm mit der Benutzeroberfläche
# nur verändern, wen man weiß, was man tut ;-)
    
layout = []
layout.append([[sg.Text('Zahl eingeben')]+[sg.InputText(key='zahl')]])
layout.append([[sg.Text('Verdoppelung der Zahl:')]+[sg.Text(key='ergebnis')]])
layout.append([sg.Button('Berechnen', key='berechnen')])
layout.append([sg.Button('Quit')])
window = sg.Window('Beispiel-GUI: Rechner', layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'berechnen':
        zahl = value["zahl"]
        try:
            zahl=float(zahl)
        except ValueError:
            zahl=0.0
        ergebnis=verdoppeln(zahl)
        window['ergebnis'].update(ergebnis)
        continue

window.close()