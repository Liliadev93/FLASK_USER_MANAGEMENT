from flask import Flask, render_template, request, redirect, url_for
from db import lister_users, ajouter_user, supprimer_user

app = Flask(__name__)


@app.route("/")
def routePrincipale():
    return "Hello World"


@app.route("/users")
def routeUsers():
    users = lister_users()
    return render_template("users.html", users=users)


@app.route("/ajouter", methods=["GET", "POST"])
def routeAjouter():
    if request.method == "POST":
        ajouter_user(request.form["nom"], request.form["prenom"], request.form["mail"])
        return redirect(url_for("routeUsers"))
    return render_template("ajouter.html")


@app.route("/supprimer/<id>")
def routeSupprimer(id):
    supprimer_user(id)
    return redirect(url_for("routeUsers"))