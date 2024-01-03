import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from style_musical import StyleMusical

class StyleMusicalBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_style_musical(self):
        try:
            query = text("select max(idSt) as m from STYLE_MUSICAL")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_styles_musicaux(self):
        try:
            query = text("select idSt, nomSt, caracteristiquesSt from STYLE_MUSICAL")
            resultat = self.__connexion.execute(query)
            liste_styles_musicaux = []
            for id_style_musical, nom, caracteristiques in resultat:
                liste_styles_musicaux.append(
                    StyleMusical(id_style_musical, nom, caracteristiques)
                )
            return liste_styles_musicaux
        except Exception as exp:
            print(f"Erreur lors de la récupération des styles musicaux : {exp}")
            return None

    def get_par_id_style_musical(self, id_style_musical):
        try:
            query = text("select idSt, nomSt, caracteristiquesSt from STYLE_MUSICAL where idSt = " + str(id_style_musical))
            resultat = self.__connexion.execute(query)
            le_style_musical = None
            for id_style_musical, nom, caracteristiques in resultat:
                le_style_musical = StyleMusical(id_style_musical, nom, caracteristiques)
            return le_style_musical
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_style_musical(self, id_style_musical, nom, caracteristiques):
        try:
            query = text(f"insert into STYLE_MUSICAL values({str(id_style_musical)} ,'{nom}', '{caracteristiques}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un style musical réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None