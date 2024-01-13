import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from faire_partie import FairePartie
from artiste import Artiste

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
    
    def get_artistes_par_id_groupe(self, id_groupe):
        try:
            query = text("select idA, nomA, descriptionA, lienImageA from FAIRE_PARTIE natural join ARTISTE where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            liste_artistes_groupe = []
            for id_artiste, nom, description, lien_image in resultat:
                liste_artistes_groupe.append(Artiste(id_artiste, nom, description, lien_image))
            return liste_artistes_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None
        
    def supprimer_avec_id_groupe(self, id_groupe):
        """Supprime l'association faire partie dans la bd avec l'id du groupe

        Args:
            id_groupe (int): l'id du groupe
        """
        try:
            query = text("delete from FAIRE_PARTIE where idG = " + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression de faire partie réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None