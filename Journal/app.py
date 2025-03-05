from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html").read() 

@app.route("/save", methods=["POST"])
def save():
    eintrag = request.form["eintrag"]
    datum = datetime.date.today().strftime("%Y-%m-%d")

    filename = f"tagebuch_{datum}.txt"
    
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{datum}:\n{eintrag}\n\n")

    return "Eintrag gespeichert! <a href='/'>Zurück</a>"

if __name__ == "__main__":
    app.run(debug=True)
