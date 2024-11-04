import PySimpleGUI as sg

# In dieser Funktion wird die eigentliche Berechung durchgeführt.
# Aufruf der Funktion durch Klick auf die Schaltfläche
# In dieser Funktion wird die Umrechnung durchgeführt => hier programmieren

# Hier beginnt das Hauptprogramm mit der Benutzeroberfläche
# nur verändern, wen man weiß, was man tut ;-)
def verdoppeln(zahl):
    return 2*zahl

layout = []
layout.append([[sg.Text('Zahl Eingeben:')]+[sg.InputText(key='eingabe')]])
layout.append([[sg.Text('Verdopplung der Zahl:')]+[sg.Text(key='ausgabe')]])
layout.append([sg.Button('Berechnen', key='berechnen')])
layout.append([sg.Button('Quit')])
window = sg.Window('Beispiel-GUI: Rechner', layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'berechnen':
        eingabe = value["eingabe"]
        try:
           eingabe=float(eingabe)
        except ValueError:
           window['eingabe'].update("Gebe korrekte Zahl ein!")
           continue
        ergebnis=verdoppeln(eingabe)
        window['ausgabe'].update(ergebnis)
        continue

window.close()