import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from reseau_social import ReseauSocial

class ReseauSocialBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_reseau_social(self):
        try:
            query = text("select max(idRS) as m from RESEAU_SOCIAL")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_reseaux_sociaux(self):
        try:
            query = text("select idRS, nomRS, lienRS, idG from RESEAU_SOCIAL")
            resultat = self.__connexion.execute(query)
            liste_reseaux_sociaux = []
            for id_reseau_social, nom, lien, id_groupe in resultat:
                liste_reseaux_sociaux.append(
                    ReseauSocial(id_reseau_social, nom, lien, id_groupe)
                )
            return liste_reseaux_sociaux
        except Exception as exp:
            print(f"Erreur lors de la récupération des réseaux sociaux : {exp}")
            return None

    def get_par_id_reseau_social(self, id_reseau_social):
        try:
            query = text("select idRS, nomRS, lienRS, idG from RESEAU_SOCIAL where idRS = " + str(id_reseau_social))
            resultat = self.__connexion.execute(query)
            le_reseau_social = None
            for id_reseau_social, nom, lien, id_groupe in resultat:
                le_reseau_social = ReseauSocial(id_reseau_social, nom, lien, id_groupe)
            return le_reseau_social
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def get_par_id_groupe(self, id_groupe):
        try:
            query = text("select idRS, nomRS, lienRS, idG from RESEAU_SOCIAL where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            liste_reseaux_sociaux_groupe = None
            for id_reseau_social, nom, lien, id_groupe in resultat:
                liste_reseaux_sociaux_groupe = ReseauSocial(id_reseau_social, nom, lien, id_groupe)
            return liste_reseaux_sociaux_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_reseau_social(self, id_reseau_social, nom, lien, id_groupe):
        try:
            query = text(f"insert into RESEAU_SOCIAL values({str(id_reseau_social)} ,'{nom}', '{lien}', {str(id_groupe)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un réseau social réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None