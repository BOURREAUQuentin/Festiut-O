import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from heberger import Heberger

class HebergerBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_heberger(self):
        """Renvoie la liste de toutes les associations hebergement

        Returns:
            List(Heberger): la liste des associations hebergements 
        """
        try:
            query = text("select idH, idG from HEBERGER")
            resultat = self.__connexion.execute(query)
            lisste_heberger = []
            for id_hebergement, id_groupe in resultat:
                lisste_heberger.append(
                    Heberger(id_hebergement, id_groupe)
                )
            return lisste_heberger
        except Exception as exp:
            print(f"Erreur lors de la récupération des heberger : {exp}")
            return None
    
    def get_par_id_hebergement(self, id_hebergement):
        """Renvoie l'association d'hebergement avec cet id

        Args:
            id_hebergement (int): l'id de l'hebergement

        Returns:
            int: l'association de l'hebergement avec cet id
        """
        try:
            query = text("select idH, idG from HEBERGER where idH = " + str(id_hebergement))
            resultat = self.__connexion.execute(query)
            les_heberger_hebergement = []
            for id_hebergement, id_groupe in resultat:
                les_heberger_hebergement.append(Heberger(id_hebergement, id_groupe))
            return les_heberger_hebergement
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_groupe(self, id_groupe):
        """Renvoie l'association d'hebergement relié avec cet id de groupe

        Args:
            id_hebergement (int): l'id du groupe lié

        Returns:
            int: l'association de l'hebergement lié avec cet id
        """
        try:
            query = text("select idH, idG from HEBERGER where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            les_heberger_groupe = []
            for id_hebergement, id_groupe in resultat:
                les_heberger_groupe.append(Heberger(id_hebergement, id_groupe))
            return les_heberger_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_heberger(self, id_hebergement, id_groupe):
        """Ajoute une association heberger dans la bd

        Args:
            id_hebergement (int): l'id de l'hebergement
            id_groupe (int): l'id du groupe
        """
        try:
            query = text(f"insert into HEBERGER values({str(id_hebergement)} , {str(id_groupe)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un heberger réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
        
    def supprimer_avec_id_groupe(self, id_groupe):
        """Supprime l'association heberger dans la bd avec l'id du groupe

        Args:
            id_groupe (int): l'id du groupe
        """
        try:
            query = text("delete from HEBERGER where idG = " + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression de heberger réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None