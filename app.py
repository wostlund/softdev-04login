from flask import Flask, render_template, request, url_for, session, redirect
import utils.login
import hashlib

app = Flask(__name__)
app.secret_key = "Rosebud"

@app.route('/')
def foo():
    if len(session.keys()) != 0:
        return redirect(url_for("loggedIn"))
    return render_template("home.html")

@app.route("/reg", methods=['POST'])
def register():
    if len(session.keys()) != 0:
        return redirect(url_for("loggedIn"))
    h = hashlib.md5()
    mark = utils.login.createDict()
    if request.form["user"] in mark:
        return render_template("home.html", message="username already taken")
    h.update(request.form["password"])
    utils.login.addUser(request.form["user"], h.hexdigest())
    return render_template("home.html", title="Login", message="Successfully registered")

@app.route("/authenticate", methods=['POST'])
def auth():
    if len(session.keys()) != 0:
        return redirect(url_for("loggedIn"))
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
        session[app.secret_key] = users 
        return redirect(url_for("loggedIn"))

@app.route("/loggedIn")
def loggedIn():
    if len(session.keys()) == 0:
        return redirect(url_for("foo"))
    return render_template("log.html", user = session[app.secret_key])

@app.route("/logout")
def logout():
    session.pop(app.secret_key)
    return redirect(url_for("foo"))

if(__name__ == "__main__"):
    app.debug = True
    app.run();
