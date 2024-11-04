import sqlite3
test_vokabeln=[['Haus','EN', 'house'], \
               ['warten','EN', 'wait'],\
               ['Zeit','EN','time']]

connection = sqlite3.connect('vokabel.db')

with open('static/schema_vokabel_db.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for liste in test_vokabeln:
    cur.execute("INSERT INTO vokabeln (name, language, vokabel) VALUES (?, ?, ?)",
            (liste[0], liste[1], liste[2])
            )

connection.commit()
connection.close()