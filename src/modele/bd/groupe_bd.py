import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from groupe import Groupe
from style_musical import STYLE

class GroupeBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_groupe(self):
        try:
            query = text("select max(idG) as m from GROUPE")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_groupes(self):
        try:
            query = text("select idG, nomG, descriptionG from GROUPE")
            resultat = self.__connexion.execute(query)
            liste_groupes = []
            for id_groupe, nom, description in resultat:
                liste_groupes.append(
                    Groupe(id_groupe, nom, description)
                )
            return liste_groupes
        except Exception as exp:
            print(f"Erreur lors de la récupération des groupes : {exp}")
            return None

    def get_par_id_groupe(self, id_groupe):
        try:
            query = text("select idG, nomG, descriptionG from GROUPE where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            le_groupe = None
            for id_groupe, nom, description in resultat:
                le_groupe = Groupe(id_groupe, nom, description)
            return le_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_groupe(self, id_groupe, nom, description):
        try:
            query = text(f"insert into GROUPE values({str(id_groupe)} ,'{nom}', '{description}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un groupe réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
        
    def get_style(self, id_groupe):
        try:
            query = text("select idSt from INTERPRETER where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            le_style = None
            for id_style in resultat:
                le_style = Style(id_style)
            return le_style
        except Exception as exp:
            print("la connexion a échoué !")
            return None