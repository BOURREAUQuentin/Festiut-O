import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from panier import Panier

class PanierBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_panier(self):
        """Renvoie la liste de tous les paniers dans la bd

        Returns:
            List(Panier): la liste de tous les paniers
        """
        try:
            query = text("select idB, idS, quantiteB from PANIER")
            resultat = self.__connexion.execute(query)
            liste_panier = []
            for id_billet, id_spectateur, quantite_billet in resultat:
                liste_panier.append(
                    Panier(id_billet, id_spectateur, quantite_billet)
                )
            return liste_panier
        except Exception as exp:
            print(f"Erreur lors de la récupération des panier : {exp}")
            return None

    def get_par_id_billet(self, id_billet):
        """Renvoie le Panier correspondant à cet id

        Args:
            id_billet (int): l'id du billet

        Returns:
            Panier: le panier correspondant
        """
        try:
            query = text("select idB, idS, quantiteB from PANIER where idB = " + str(id_billet))
            resultat = self.__connexion.execute(query)
            liste_panier_billet = []
            for id_billet, id_spectateur, quantite_billet in resultat:
                liste_panier_billet.append(Panier(id_billet, id_spectateur, quantite_billet))
            return liste_panier_billet
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_spectateur(self, id_spectateur):
        """Renvoi le panier correspondant à cet id specteur

        Args:
            id_spectateur (int): l'id du spectateur

        Returns:
            Panier: le Panier correspondant
        """
        try:
            query = text("select idB, idS, quantiteB from PANIER where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            liste_panier_spectateur = []
            for id_billet, id_spectateur, quantite_billet in resultat:
                liste_panier_spectateur.append(Panier(id_billet, id_spectateur, quantite_billet))
            return liste_panier_spectateur
        except Exception as exp:
            print("la connexion a échoué !")
            return None
 
    def ajouter_panier(self, id_billet, id_spectateur, quantite_billet):
        """Ajoute un Panier dans la bd

        Args:
            id_billet (int: l'id du panier
            id_spectateur (int): l'id du spectateur
            quantite_billet (int): la quantité de billets
        """
        try:
            query = text(f"insert into PANIER values({str(id_billet)}, {str(id_spectateur)}, {str(quantite_billet)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un panier réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def supprimer_billet(self, id_billet, id_spectateur):
        """Supprime un panier dans la bd

        Args:
            id_billet (int): l'id du bilet
            id_spectateur (int): l'id du spectateur correspondant
        """
        try:
            query = text("delete from PANIER where idB = " + str(id_billet) + " and idS = " + str(id_spectateur))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression d'un billet du panier réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
    
    def modifier_quantite_billet(self, id_billet, id_spectateur, nouvelle_quantite_billet):
        """Modifie le Panier dans la bd

        Args:
            id_billet (int): l'id du billet
            id_spectateur (int): l'id spectateur
            nouvelle_quantite_billet (int): la nouvelle quantité de billet

        Returns:
            _type_: _description_
        """
        try:
            query = text("update PANIER set quantiteB = "+ nouvelle_quantite_billet + " where idB = " + str(id_billet) + " and idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
        except Exception as exp:
            print("la connexion a échoué !")
            return None
