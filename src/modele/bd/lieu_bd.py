import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from lieu import Lieu

class LieuBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_lieu(self):
        try:
            query = text("select max(idL) as m from LIEU")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_lieux(self):
        try:
            query = text("select idL, nomL, adresseL, nbMaxSpecL from LIEU")
            resultat = self.__connexion.execute(query)
            liste_lieux = []
            for id_lieu, nom, adresse, nb_max_spectateurs in resultat:
                liste_lieux.append(
                    Lieu(id_lieu, nom, adresse, nb_max_spectateurs)
                )
            return liste_lieux
        except Exception as exp:
            print(f"Erreur lors de la récupération des lieux : {exp}")
            return None

    def get_par_id_lieu(self, id_lieu):
        try:
            query = text("select idL, nomL, adresseL, nbMaxSpecL from LIEU where idL = " + str(id_lieu))
            resultat = self.__connexion.execute(query)
            le_lieu = None
            for id_lieu, nom, adresse, nb_max_spectateurs in resultat:
                le_lieu = Lieu(id_lieu, nom, adresse, nb_max_spectateurs)
            return le_lieu
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def inserer_lieu(self, id_lieu, nom, adresse, nb_max_spectateurs):
        try:
            query = text(f"insert into LIEU values({str(id_lieu)} ,'{nom}', '{adresse}', {str(nb_max_spectateurs)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un lieu réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None