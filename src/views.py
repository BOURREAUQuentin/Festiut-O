from io import BytesIO
import os
import sys
from flask import jsonify, render_template, send_file, url_for, redirect, request
from flask import request
from .app import app
from .models import GROUPE, SPECTATEUR, BILLET, ACCEDER, JOURNEE, PANIER, FAIRE_PARTIE, inserer_le_spectateur, ajouter_billet_panier, supprimer_billet_panier, au_moins_deux_artistes_dans_groupe, lister_groupes_meme_style, lister_evenements_pour_groupe
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
    liste_groupes=GROUPE.get_all_groupes()
    return render_template("les_groupes.html", page_les_groupes=True, liste_groupes=liste_groupes)

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
  
@app.route("/panier")
def panier():
    liste_billets_panier_spectateur = PANIER.get_all_billets_panier_spectateur(le_spectateur_connecte.get_id())
    liste_journees_panier_spectateur = ACCEDER.get_les_journees_panier_spectateur(le_spectateur_connecte.get_id())
    liste_groupes_samedi = []
    liste_groupes_week_end = []
    liste_groupes_dimanche = []
    # test de quels jours le spectateur a dans son panier
    for index_journee in range(len(liste_journees_panier_spectateur)):
        if liste_journees_panier_spectateur[index_journee] == "Samedi":
            liste_groupes_samedi = JOURNEE.get_groupes_par_journee(liste_journees_panier_spectateur[index_journee])
        elif liste_journees_panier_spectateur[index_journee] == "Week-end":
            liste_groupes_week_end = JOURNEE.get_groupes_par_journee(liste_journees_panier_spectateur[index_journee])
        else:
            liste_groupes_dimanche = JOURNEE.get_groupes_par_journee(liste_journees_panier_spectateur[index_journee])
    return render_template("panier.html", page_panier=True, liste_billets=liste_billets_panier_spectateur,
                           liste_journees=liste_journees_panier_spectateur, liste_groupes_samedi=liste_groupes_samedi,
                           liste_groupes_week_end=liste_groupes_week_end, liste_groupes_dimanche=liste_groupes_dimanche)

@app.route("/billetterie")
def billetterie():
    liste_billets = BILLET.get_all_billets()
    liste_journees = ACCEDER.get_les_journees_billetterie()
    # la suite car la liste_journees contient uniquement 3 valeurs (Samedi, Week-end, Dimanche) car le festival dure 2 jours
    liste_groupes_samedi = JOURNEE.get_groupes_par_journee(liste_journees[0])
    liste_groupes_week_end = JOURNEE.get_groupes_par_journee(liste_journees[1])
    liste_groupes_dimanche = JOURNEE.get_groupes_par_journee(liste_journees[2])
    return render_template("billetterie.html", page_billetterie=True, liste_billets=liste_billets,
                           liste_journees=liste_journees, liste_groupes_samedi=liste_groupes_samedi,
                           liste_groupes_week_end=liste_groupes_week_end, liste_groupes_dimanche=liste_groupes_dimanche)

@app.route("/groupe_details/<id_groupe>")
def groupe_details(id_groupe):
    liste_artistes_groupe = []
    if au_moins_deux_artistes_dans_groupe:
        liste_artistes_groupe = FAIRE_PARTIE.get_artistes_par_id_groupe(id_groupe)
    return render_template("groupe_details.html", page_groupe_details=True, groupe=GROUPE.get_par_id_groupe(id_groupe),
                           liste_artistes=liste_artistes_groupe, liste_evenements_groupe=lister_evenements_pour_groupe(id_groupe),
                           liste_groupes_meme_style=lister_groupes_meme_style(id_groupe))
