import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from faire_partie import FairePartie

class FairePartieBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_faire_partie(self):
        try:
            query = text("select idG, idA from FAIRE_PARTIE")
            resultat = self.__connexion.execute(query)
            lisste_faire_partie = []
            for id_groupe, id_artiste in resultat:
                lisste_faire_partie.append(
                    FairePartie(id_groupe, id_artiste)
                )
            return lisste_faire_partie
        except Exception as exp:
            print(f"Erreur lors de la récupération des faire_partie : {exp}")
            return None

    def get_par_id_groupe(self, id_groupe):
        try:
            query = text("select idG, idA from FAIRE_PARTIE where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            les_faire_partie_groupe = []
            for id_groupe, id_artiste in resultat:
                les_faire_partie_groupe.append(FairePartie(id_groupe, id_artiste))
            return les_faire_partie_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_artiste(self, id_artiste):
        try:
            query = text("select idG, idA from FAIRE_PARTIE where idA = " + str(id_artiste))
            resultat = self.__connexion.execute(query)
            les_faire_partie_artiste = []
            for id_groupe, id_artiste in resultat:
                les_faire_partie_artiste.append(FairePartie(id_groupe, id_artiste))
            return les_faire_partie_artiste
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_faire_partie(self, id_groupe, id_artiste):
        try:
            query = text(f"insert into FAIRE_PARTIE values({str(id_groupe)} , {str(id_artiste)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un faire_partie réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None