import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from panier import Panier
from billet import Billet

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
    
    def get_billet_deja_dans_panier(self, id_billet, id_spectateur):
        try:
            query = text("select idB, idS, quantiteB from PANIER where idB = "+ str(id_billet) + " and idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            if len(resultat) > 0:
                # si le spectateur a déjà ce billet dans son panier
                return True
            return False
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def update_quantite_billet_panier(self, id_billet, id_spectateur, quantite_billet):
        try:
            query = text("update PANIER set quantiteB = quantiteB +" + str(quantite_billet) + " where idB = " + str(id_billet) + " and idS = " + str(id_spectateur))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Modification de la quantité réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
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
    
    def get_prix_total_billet_par_id_spectateur(self, id_billet, id_spectateur):
        """
        Retourne le prix total d'un billet (suivant la quantité) sur le panier d'un spectateur.

        Args:
        Param: id_billet : l'id du billet.
        Param: id_spectateur : l'id du spectateur.

        Returns:
            (int) : le prix total d'un billet (suivant la quantité) sur le panier d'un spectateur.
        """
        try:
            query = text("select quantiteB*prixB from PANIER natural join BILLET where idB = " + str(id_billet) + " and idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            prix_total_billet = 0
            for prix_total in resultat:
                prix_total_billet = prix_total
            return prix_total_billet
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def get_prix_total_panier_par_id_spectateur(self, id_spectateur):
        """
        Retourne le prix total du panier d'un spectateur.


        Args:
        Param: id_spectateur : l'id du spectateur.


        Returns:
            (int) : le prix total du panier d'un spectateur.
        """
        try:
            query = text("select idB from PANIER where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            prix_total_panier = 0
            for id_billet in resultat:
                prix_total_panier += self.get_prix_total_billet_par_id_spectateur(id_billet, id_spectateur)
            return prix_total_panier
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_all_billets_panier_spectateur(self, id_spectateur):
        """
        Retourne le dictionnaire des billets dans le panier du spectateur avec
        comme clé le Billet et comme valeur la quantité de ce billet.

        Args:
        Param: id_spectateur : l'id du spectateur.

        Returns:
            (dict(Billet, int)) : le dictionnaire des billets dans le panier du spectateur avec
            comme clé le Billet et comme valeur la quantité de ce billet.
        """
        try:
            query = text("select idB, prixB, quantiteB from BILLET natural join PANIER where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            dico_billets_panier_spectateur = set()
            for id_billet, prix_billet, quantite_billet in resultat:
                dico_billets_panier_spectateur.add(Billet(id_billet, prix_billet), quantite_billet)
            return dico_billets_panier_spectateur
        except Exception as exp:
            print(f"Erreur lors de la récupération des billets dans le panier du spectateur : {exp}")
            return None