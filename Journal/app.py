from flask import Flask, render_template, request
import datetime
import os
import glob

app = Flask(__name__)

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


    return "Eintrag gespeichert! <a href='/'>Zurück</a>"

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "").lower()
    if not query:
        return "Bitte gib ein Stichwort ein! <a href='/'>Zurück</a>"

    ergebnisse = []
    for file in glob.glob("tagebuch_*.txt"):  
        with open(file, "r", encoding="utf-8") as f:
            einträge = f.read().split("\n\n") 

            for eintrag in einträge:
                if query in eintrag.lower():
                    ergebnisse.append(f"<strong>{file}</strong><br>{eintrag}")

    if ergebnisse:
        return "<h2>Gefundene Einträge:</h2><pre>" + "<br><br>".join(ergebnisse) + "</pre><a href='/'>Zurück</a>"
    else:
        return "Kein Eintrag gefunden. <a href='/'>Zurück</a>"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
