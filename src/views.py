from io import BytesIO
import os
import sys
from flask import jsonify, render_template, send_file, url_for, redirect, request
from flask import request
from .app import app
from .models import GROUPE, SPECTATEUR, inserer_le_spectateur
from flask import jsonify, render_template, url_for, redirect, request, redirect, url_for
from spectateur import Spectateur

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

le_spectateur_connecte = Spectateur(-1, "", "", "", "", "", "", "", "N")

@app.route("/")
def accueil():
    """
        Nous montre la premiere page la du lancement du site
    """
    return render_template("accueil.html", page_home=True)

@app.route("/les-groupes")
def les_groupes():
    return render_template("les_groupes.html", page_les_groupes=True)

@app.route("/login", methods=['GET', 'POST'])
def login():
    """
        permet de se diriger vers la page login (connexion)
    """
    return render_template("login.html", page_login=True)

@app.route("/inscription")
def inscription():
    """
        Permet de se diriger vers la page inscription
    """
    return render_template("inscription.html", page_inscription=True)

@app.route("/les-parcours", methods=["GET", "POST"])
def connecter():
    """
        récupère les champs entrés dans la page de connexion et vérifie
        si l'utilisateur à déjà un compte :
        s'il a un compte, on le dirige vers la page des parcours.
        sinon on le redirige sur la page connexion.
    """
    username = request.form.get("username")
    password = request.form.get("password")
    liste_spectateurs = SPECTATEUR.get_all_spectateurs()
    if liste_spectateurs:
        spectateur_trouve = next(
            (spectateur for spectateur in liste_spectateurs
             if (username == spectateur.get_nom_utilisateur() or username == spectateur.get_mail())
             and password == spectateur.get_mdp()), None)
        if spectateur_trouve:
            le_spectateur_connecte.set_all(spectateur_trouve.get_id(),
                                   spectateur_trouve.get_nom(),
                                   spectateur_trouve.get_prenom(),
                                   spectateur_trouve.get_mail(),
                                   spectateur_trouve.get_date_naissance(),
                                   spectateur_trouve.get_telephone(),
                                   spectateur_trouve.get_nom_utilisateur(),
                                   spectateur_trouve.get_mdp(),
                                   spectateur_trouve.get_admin())
            return redirect(url_for("accueil"))
    return redirect(url_for("login"))

@app.route("/inscription", methods=["GET", "POST"])
def inscrire():
    """
    Permet d'inscrire le spectateur (utilisateur) qui n'a pas de compte
    """
    if request.method == "POST":
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        mail = request.form.get("mail")
        date_naissance = request.form.get("date_naissance")
        telephone = request.form.get("telephone")
        username = request.form.get("username")
        password = request.form.get("password")
        liste_spectateurs = SPECTATEUR.get_all_spectateurs()

        for spectateur in liste_spectateurs:
            if username == spectateur.get_nom_utilisateur() or mail == spectateur.get_mail():
                # erreur car y'a déjà un spectateur portant ce username ou ce mail (gérer l'erreur)
                #return jsonify({"error": "exists"})
                pass
        inserer_le_spectateur(nom, prenom, mail, date_naissance, telephone, username, password)
        le_spectateur_connecte.set_all(SPECTATEUR.get_prochain_id_spectateur() - 1,
                                   nom, prenom, mail, date_naissance, telephone, username, password, "N")
        return redirect(url_for("accueil"))
    return render_template("login.html", page_login=True)

@app.route("/billetterie")
def billetterie():

    return render_template("billetterie.html", page_billetterie=True)