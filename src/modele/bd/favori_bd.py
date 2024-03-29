import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from favori import Favori

class FavoriBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_favori(self):
        """Renvoie la liste de tous les favoris existants"""
        try:
            query = text("select idS, idG from FAVORI")
            resultat = self.__connexion.execute(query)
            liste_favori = []
            for id_spectateur, id_groupe in resultat:
                liste_favori.append(
                    Favori(id_spectateur, id_groupe)
                )
            return liste_favori
        except Exception as exp:
            print(f"Erreur lors de la récupération des favori : {exp}")
            return None
    
    def get_par_id_spectateur(self, id_spectateur):
        """Renvoie les favoris du spectateur correspondant

        Args:
            id_spectateur (int): l'id du spectateur

        Returns:
            Favori: le favori correspondant
        """
        try:
            query = text("select idS, idG from FAVORI where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            les_favori_spectateur = []
            for id_spectateur, id_groupe in resultat:
                les_favori_spectateur.append(Favori(id_spectateur, id_groupe))
            return les_favori_spectateur
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_groupe(self, id_groupe):
        """Retourne la liste des favoris correspondant au groupe

        Args:
            id_groupe (int): l'id du groupe

        Returns:
            List(Favori): la liste des favoris correspondant au groupe
        """
        try:
            query = text("select idS, idG from FAVORI where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            les_favori_groupe = []
            for id_spectateur, id_groupe in resultat:
                les_favori_groupe.append(Favori(id_spectateur, id_groupe))
            return les_favori_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_favori(self, id_spectateur, id_groupe):
        """Ajoute un favoris dans la bd

        Args:
            id_spectateur (int): l'id du spectateur
            id_groupe (int): l'id du groupe
        """
        try:
            query = text(f"insert into FAVORI values({str(id_spectateur)} , {str(id_groupe)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un favori réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
        
    def supprimer_avec_id_spectateur(self, id_spect):
        """Supprime le favori dans la bd

        Args:
            id_spect (int): l'id du spectateur du groupe
        """
        try:
            query = text("delete from FAVORI where idS = " + str(id_spect))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression du favoris réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
        
    def supprimer_avec_id_groupe(self, id_groupe):
        """Supprime l'association favori dans la bd avec l'id du groupe

        Args:
            id_groupe (int): l'id du groupe
        """
        try:
            query = text("delete from FAVORI where idG = " + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression de favori réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None