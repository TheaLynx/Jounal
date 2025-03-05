from flask import Flask, render_template, request
import datetime

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

    return "Eintrag gespeichert!"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
