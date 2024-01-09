from io import BytesIO
import os
import sys
from flask import jsonify, render_template, send_file, url_for, redirect, request
from flask import request
from .app import app
from .models import lister_evenements_pour_groupe
from flask import jsonify, render_template, url_for, redirect, request, redirect, url_for
@app.route("/")
def accueil():
    """
        Nous montre la premiere page la du lancement du site
    """
    liste_evenements = lister_evenements_pour_groupe(1)
    print(liste_evenements)
    return render_template("accueil.html", page_home=True)