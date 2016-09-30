from flask import Flask, render_template, request
PASSWORDS = {}

app = Flask(__name__)
username = ""
password = ""

@app.route('/')
@app.route("/login")
def go():
    print request.headers
    print app
    return render_template("web.html")

@app.route("/authenticate", methods = ["GET", "POST"])
def auth():
    print request.args
    if request.form["username"] == "Will" and request.form['password'] == "password":
        return render_template("temp.html", title = "logged in", result = "congrats, you logged in")
    return render_template("temp.html", title = "failure", result = "Get your act together!")

if(__name__ == "__main__"):
    app.debug = True
    app.run();
