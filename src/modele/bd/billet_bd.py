import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from billet import Billet

class BilletBD:
    def __init__(self, connexion):
        self.__connexion = connexion
    
    def get_prochain_id_billet(self):
        """Permet de savoir l'id du prochain billet à insérer

        Returns:
            int: l'id du prochain billet
        """
        try:
            query = text("select max(idB) as m from BILLET")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None
    
    def get_all_billets(self):
        """Renvoie tous les billets dans la bd

        Returns:
            List(Billet): la liste de tous les billets
        """
        try:
            query = text("select idB, prixB from BILLET")
            resultat = self.__connexion.execute(query)
            liste_billets = []
            for id_billet, prix in resultat:
                liste_billets.append(
                    Billet(id_billet, prix)
                )
            return liste_billets
        except Exception as exp:
            print(f"Erreur lors de la récupération des billets : {exp}")
            return None
    
    def get_par_id_billet(self, id_billet):
        """Renvoie le billet avec l'id correspondant

        Args:
            id_billet (int): l'id du billet

        Returns:le billet correspondant à l'id
        """
        try:
            query = text("select idB, prixB from BILLET where idB = " + str(id_billet))
            resultat = self.__connexion.execute(query)
            le_billet = None
            for id_billet, prix in resultat:
                le_billet = Billet(id_billet, prix)
            return le_billet
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_billet(self, id_billet, prix):
        """Ajoute un billet dans la bd

        Args:
            id_billet (int): l'id du billet
            prix (String): le prix du billet
        """
        try:
            query = text(f"insert into BILLET values({str(id_billet)} ,{str(prix)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Billet vendu !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None