from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index(): #Webseite wird anhand eines Templates erstellt
    return render_template('index.html')

@app.route("/about")
def about(): #Statische Webseite
    page = "Wir haben diese App im Informatik-Unterricht erstellt!"
    return page

@app.route("/search") #Webseite übernimmt Parameter aus GET-Request
def search():
    args = request.args.to_dict()
    print(args)
    suche = args.get('q')
    if type(suche)==type(None):
        return "Sucheingabe fehlt"
    else:
        return render_template('search.html', suche=suche)
    