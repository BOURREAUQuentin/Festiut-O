from datetime import datetime
import os
import sys
from .app import app
from .models import GROUPE, SPECTATEUR, BILLET, ACCEDER, JOURNEE, PANIER, FAIRE_PARTIE, ARTISTE, INSTRUMENT, ACHETER, spectateur_est_connecte, inserer_le_spectateur, ajouter_billet_panier, supprimer_billet_panier, au_moins_deux_artistes_dans_groupe, lister_groupes_meme_style, lister_evenements_pour_groupe, lister_evenements_par_journee
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
    return render_template("accueil.html", page_home=True, connecte=spectateur_est_connecte(le_spectateur_connecte))

@app.route("/les-groupes")
def les_groupes():
    liste_groupes=GROUPE.get_all_groupes()
    print(le_spectateur_connecte.get_nom_utilisateur())
    return render_template("les_groupes.html", page_les_groupes=True, liste_groupes=liste_groupes, connecte=spectateur_est_connecte(le_spectateur_connecte))

@app.route("/login", methods=['GET', 'POST'])
def login():
    """
        permet de se diriger vers la page login (connexion/inscription)
    """
    return render_template("login_signup.html", page_login_signup=True, connecte=spectateur_est_connecte(le_spectateur_connecte))

@app.route("/deconnexion")
def deconnexion():
    """
        permet de se déconnecter (revient à l'accueil)
    """
    le_spectateur_connecte.set_all(-1, "", "", "", "", "", "", "", "N")
    return redirect(url_for("accueil"))

@app.route("/connexion", methods=["GET", "POST"])
def connecter():
    username = request.form.get('username')
    password = request.form.get("password")
    liste_spectateurs = SPECTATEUR.get_all_spectateurs()
    if liste_spectateurs:
        spectateur_trouve = None
        for spectateur in liste_spectateurs:
            if (spectateur.get_nom_utilisateur() == username or spectateur.get_mail() == username) and spectateur.get_mdp() == password:
                spectateur_trouve = spectateur
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
            print("oui")
            return redirect(url_for("accueil"))
        return redirect(url_for("login"))
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
        print(mail)
        date_naissance = request.form.get("date_naissance")
        date_objet = datetime.strptime(date_naissance, '%d/%m/%Y')
        # Formater la nouvelle date selon le format souhaité (dans la bd aaaa-mm-jj)
        date_naissance_nouveau_format = date_objet.strftime('%Y-%m-%d')
        print(date_naissance_nouveau_format)
        telephone = request.form.get("telephone")
        username = request.form.get("username")
        password = request.form.get("password")
        liste_spectateurs = SPECTATEUR.get_all_spectateurs()

        for spectateur in liste_spectateurs:
            if username == spectateur.get_nom_utilisateur():
                return jsonify({"error": "exists-nomutilisateur"})
            if mail == spectateur.get_mail():
                return jsonify({"error": "exists-mail"})
        inserer_le_spectateur(nom, prenom, mail, date_naissance_nouveau_format, telephone, username, password)
        le_spectateur_connecte.set_all(SPECTATEUR.get_prochain_id_spectateur() - 1,
                                       nom, prenom, mail, date_naissance_nouveau_format, telephone, username, password, "N")
        return jsonify({"success": "registered"})
    return redirect(url_for("login"))

@app.route("/panier")
def panier():
    dico_billets_panier_spectateur = PANIER.get_all_billets_panier_spectateur(le_spectateur_connecte.get_id())
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
    return render_template("panier.html", page_panier=True, liste_billets=dico_billets_panier_spectateur,
                           liste_journees=liste_journees_panier_spectateur, liste_groupes_samedi=liste_groupes_samedi,
                           liste_groupes_week_end=liste_groupes_week_end, liste_groupes_dimanche=liste_groupes_dimanche, connecte=spectateur_est_connecte(le_spectateur_connecte))

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
                           liste_groupes_week_end=liste_groupes_week_end, liste_groupes_dimanche=liste_groupes_dimanche, connecte=spectateur_est_connecte(le_spectateur_connecte))

@app.route("/groupe_details/<id_groupe>")
def groupe_details(id_groupe):
    liste_artistes_groupe = []
    if au_moins_deux_artistes_dans_groupe:
        liste_artistes_groupe = FAIRE_PARTIE.get_artistes_par_id_groupe(id_groupe)
    return render_template("groupe_details.html", page_groupe_details=True, groupe=GROUPE.get_par_id_groupe(id_groupe),
                           liste_artistes=liste_artistes_groupe, liste_evenements_groupe=lister_evenements_pour_groupe(id_groupe),
                           liste_groupes_meme_style=lister_groupes_meme_style(id_groupe), connecte=spectateur_est_connecte(le_spectateur_connecte))

@app.route("/artiste_details/<id_artiste>")
def artiste_details(id_artiste):
    return render_template("artiste_details.html", page_artiste_details=True, artiste=ARTISTE.get_par_id_artiste(id_artiste),
                           liste_instruments_artiste=INSTRUMENT.get_par_id_artiste(id_artiste), connecte=spectateur_est_connecte(le_spectateur_connecte))

@app.route("/planning")
def planning():
    dico_journees = JOURNEE.get_dico_journees()
    liste_evenements_samedi = []
    liste_evenements_dimanche = []
    for journee, date_journee in dico_journees.items():
        if journee == "Samedi":
            liste_evenements_samedi = lister_evenements_par_journee(date_journee)
        else:
            liste_evenements_dimanche = lister_evenements_par_journee(date_journee)
    return render_template("planning.html", page_planning=True, liste_evenements_samedi=liste_evenements_samedi,
                           liste_evenements_dimanche=liste_evenements_dimanche, connecte=spectateur_est_connecte(le_spectateur_connecte))

@app.route("/profil")
def profil():
    """
    Permet de se diriger vers la page de profil (infos et billets achetés)
    """
    dico_billets_achete_spectateur = ACHETER.get_all_billets_achete_spectateur(le_spectateur_connecte.get_id())
    liste_journees_achete_spectateur = ACCEDER.get_les_journees_achete_spectateur(le_spectateur_connecte.get_id())
    liste_groupes_samedi = []
    liste_groupes_week_end = []
    liste_groupes_dimanche = []
    # test de quels jours le spectateur a acheté
    for index_journee in range(len(liste_journees_achete_spectateur)):
        if liste_journees_achete_spectateur[index_journee] == "Samedi":
            liste_groupes_samedi = JOURNEE.get_groupes_par_journee(liste_journees_achete_spectateur[index_journee])
        elif liste_journees_achete_spectateur[index_journee] == "Week-end":
            liste_groupes_week_end = JOURNEE.get_groupes_par_journee(liste_journees_achete_spectateur[index_journee])
        else:
            liste_groupes_dimanche = JOURNEE.get_groupes_par_journee(liste_journees_achete_spectateur[index_journee])
    return render_template("profil.html", page_profil=True, liste_billets=dico_billets_achete_spectateur,
                           liste_journees=liste_journees_achete_spectateur, liste_groupes_samedi=liste_groupes_samedi,
                           liste_groupes_week_end=liste_groupes_week_end, liste_groupes_dimanche=liste_groupes_dimanche, connecte=spectateur_est_connecte(le_spectateur_connecte))

@app.route("/admin")
def admin():
    dico_journees = JOURNEE.get_dico_journees()
    liste_evenements_samedi = []
    liste_evenements_dimanche = []
    for journee, date_journee in dico_journees.items():
        if journee == "Samedi":
            liste_evenements_samedi = lister_evenements_par_journee(date_journee)
        else:
            liste_evenements_dimanche = lister_evenements_par_journee(date_journee)
    return render_template("admin.html", page_admin=True, liste_evenements_samedi=liste_evenements_samedi,
                           liste_groupes=GROUPE.get_all_groupes(), liste_artistes=ARTISTE.get_all_artistes(),
                           liste_evenements_dimanche=liste_evenements_dimanche, connecte=spectateur_est_connecte(le_spectateur_connecte))
