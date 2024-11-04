from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('vokabel.db')
    return conn

@app.route('/')
def index(): #Webseite wird anhand eines Templates erstellt
    conn = get_db_connection()
    vokabeln = conn.execute('SELECT rowid, * FROM vokabeln').fetchall()
    payload=[]
    for vokabel in vokabeln:
        payload.append({'rowid': vokabel[0],'name': vokabel[1], 'language': vokabel[2], 'vokabel': vokabel[3]})
    print(payload)
    conn.close()
    return render_template('index.html', payload=payload)

@app.route("/vokabel/add", methods=['POST'])
def add():
    conn = get_db_connection()
    args = request.form.to_dict()
    print(args)
    sql="INSERT INTO vokabeln VALUES('"+str(args.get('name'))+"','EN','"+str(args.get('vokabel'))+"');"
    print(sql)
    conn.execute(sql)
    conn.commit()
    return index()

@app.route("/vokabel/input")
def list(): 
    return index()

@app.route("/vokabel/learn")
def learn(): 
    return render_template('learn.html')

@app.route('/vokabel/delete/<rowid>')
def delete(rowid): 
    conn = get_db_connection()
    sql='DELETE FROM vokabeln WHERE ROWID='+str(rowid)
    print(sql)
    conn.execute(sql)
    conn.commit()
    return index()

#Noch nicht verwendet...
@app.route("/search, methods=['GET']") #Webseite übernimmt Parameter aus GET-Request
def search():
    args = request.args.to_dict()
    suche = args.get('search')
    if type(suche)==type(None):
        return "Sucheingabe fehlt"
    else:
        return render_template('search.html', suche=suche)
    