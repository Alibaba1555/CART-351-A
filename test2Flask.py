from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>Go to /cat/spunky OR /cat/bernard <name> to try Cat-Latin!</h2>"

@app.route("/cat/<name>")
def cat_latin(name):
    if not name.lower().endswith("y"):
        converted = name + "y"
    else:
        converted = name[:-1] + "iful"
    return render_template("cat.html", original=name, converted=converted)

if __name__ == "__main__":
    app.run(debug=True)
