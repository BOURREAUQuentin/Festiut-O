import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from acheter import Acheter
from billet import Billet

class AcheterBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_acheter(self):
        """Récupère tous les achats effectués

        Returns:
            List(Acheter):la liste d'achats (Acheter)
        """
        try:
            query = text("select idB, idS, quantiteB from ACHETER")
            resultat = self.__connexion.execute(query)
            liste_acheter = []
            for id_billet, id_spectateur, quantite_billet in resultat:
                liste_acheter.append(
                    Acheter(id_billet, id_spectateur, quantite_billet)
                )
            return liste_acheter
        except Exception as exp:
            print(f"Erreur lors de la récupération des faire_partie : {exp}")
            return None

    def get_par_id_billet(self, id_billet):
        """Récupère les achats effectués selon le billet

        Args:
            id_billet (int): l'id du billet 

        Returns:
            List(Acheter): la liste des achats associés au billet
        """
        try:
            query = text("select idB, idS, quantiteB from ACHETER where idB = " + str(id_billet))
            resultat = self.__connexion.execute(query)
            liste_acheter_billet = []
            for id_billet, id_spectateur, quantite_billet in resultat:
                liste_acheter_billet.append(Acheter(id_billet, id_spectateur, quantite_billet))
            return liste_acheter_billet
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_spectateur(self, id_spectateur):
        """Récupère les achats selon le spectateur

        Args:
            id_spectateur (int): l'id du spectateur

        Returns:
            List(Acheter): la liste des achats du spectateur
        """
        try:
            query = text("select idB, idS, quantiteB from ACHETER where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            liste_acheter_spectateur = []
            for id_billet, id_spectateur, quantite_billet in resultat:
                liste_acheter_spectateur.append(Acheter(id_billet, id_spectateur, quantite_billet))
            return liste_acheter_spectateur
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def get_billet_deja_achete(self, id_billet, id_spectateur):
        try:
            query = text("select idB, idS, quantiteB from ACHETER where idB = "+ str(id_billet) + " and idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            if len(resultat) > 0:
                # si le spectateur a déjà payé ce billet
                return True
            return False
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def payer_billet(self, id_billet, id_spectateur, quantite_billet):
        """Fonction qui permet d'insérer un achat dans la base de données

        Args:
            id_billet (int): L'id du billet
            id_spectateur (int): L'id du spectateur
            quantite_billet (int): la quantité à insérer

        Returns:
            _type_: _description_
        """
        try:
            query = text(f"insert into ACHETER values({str(id_billet)} , {str(id_spectateur)}, {str(quantite_billet)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un acheter réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def update_quantite_billet_achete(self, id_billet, id_spectateur, quantite_billet):
        try:
            query = text("update ACHETER set quantiteB = quantiteB +" + str(quantite_billet) + " where idB = " + str(id_billet) + " and idS = " + str(id_spectateur))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Modification de la quantité réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
    
    def get_all_billets_achete_spectateur(self, id_spectateur):
        """
        Retourne le dictionnaire des billets achetés par le spectateur avec
        comme clé le Billet et comme valeur la quantité de ce billet.

        Args:
        Param: id_spectateur : l'id du spectateur.

        Returns:
            (dict(Billet, int)) : le dictionnaire des billets achetés par le spectateur avec
            comme clé le Billet et comme valeur la quantité de ce billet.
        """
        try:
            query = text("select idB, prixB, quantiteB from BILLET natural join ACHETER where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            dico_billets_achete_spectateur = set()
            for id_billet, prix_billet, quantite_billet in resultat:
                dico_billets_achete_spectateur.add(Billet(id_billet, prix_billet), quantite_billet)
            return dico_billets_achete_spectateur
        except Exception as exp:
            print("la connexion a échoué !")
            return None
