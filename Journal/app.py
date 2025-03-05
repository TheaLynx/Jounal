from flask import Flask, render_template, render_template_string, request
import datetime
import os

app = Flask(__name__)

TAGEBUCH_DATEI = "tagebuch.txt"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["GET", "POST"])
def save():
    eintrag = request.form["eintrag"]
    datum = datetime.date.today().strftime("%Y-%m-%d")

    filename = f"tagebuch_{datum}.txt"
    
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{datum}:\n{eintrag}\n\n")

    return "Eintrag gespeichert!"

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "").lower()
    if not query:
        return "Bitte gib ein Stichwort ein!"

    ergebnisse = []
    if os.path.exists(TAGEBUCH_DATEI):
        with open(TAGEBUCH_DATEI, "r", encoding="utf-8") as file:
            einträge = file.read().split("\n\n") 

            for eintrag in einträge:
                if query in eintrag.lower():
                    ergebnisse.append(eintrag)

    if ergebnisse:
        return "<h2>Gefundene Einträge:</h2><pre>" + "\n\n".join(ergebnisse) + "</pre><a href='/'>Zurück</a>"
    else:
        return "Kein Eintrag gefunden. <a href='/'>Zurück</a>"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
