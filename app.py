from flask import Flask, render_template, request
import utils.login
import hashlib

app = Flask(__name__)

@app.route('/')
def foo():
    return render_template("home.html")

@app.route("/reg", methods=['POST'])
def register():
    h = hashlib.md5()
    mark = utils.login.createDict()
    if request.form["user"] in mark:
        return render_template("home.html", message="username already taken")
    h.update(request.form["password"])
    utils.login.addUser(request.form["user"], h.hexdigest())
    return render_template("home.html", title="Login", message="successfully registered")

@app.route("/authenticate", methods=['POST'])
def auth():
    a = utils.login.createDict()
    users = request.form["user"]
    passw = request.form["password"]
    h =hashlib.md5()
    h.update(passw)
    if users not in a.keys():
        return render_template("home.html",message="Incorrect username")
    elif h.hexdigest() != a[users]:
        return render_template("home.html",message="Incorrect password")
    else:
        return render_template("home.html",message="Successfully logged in")

if(__name__ == "__main__"):
    app.debug = True
    app.run();
