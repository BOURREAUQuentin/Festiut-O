from io import BytesIO
import os
import sys
from flask import jsonify, render_template, send_file, url_for, redirect, request
from flask import request
from .app import app
from .models import GROUPE, ARTISTE
from flask import jsonify, render_template, url_for, redirect, request, redirect, url_for
@app.route("/")
def accueil():
    """
        Nous montre la premiere page la du lancement du site
    """
    return render_template("accueil.html", page_home=True)

@app.route("/les-groupes")
def les_groupes():
    print(ARTISTE.get_all_artistes())
    liste_groupes=GROUPE.get_all_groupes()
    print(GROUPE.get_all_groupes())
    return render_template("les_groupes.html", page_les_groupes=True, liste_groupes=liste_groupes)