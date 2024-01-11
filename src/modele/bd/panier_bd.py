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
        try:
            query = text("select idB, idS from PANIER")
            resultat = self.__connexion.execute(query)
            liste_panier = []
            for id_billet, id_spectateur in resultat:
                liste_panier.append(
                    Panier(id_billet, id_spectateur)
                )
            return liste_panier
        except Exception as exp:
            print(f"Erreur lors de la récupération des panier : {exp}")
            return None

    def get_par_id_billet(self, id_billet):
        try:
            query = text("select idB, idS from PANIER where idB = " + str(id_billet))
            resultat = self.__connexion.execute(query)
            liste_panier_billet = []
            for id_billet, id_spectateur in resultat:
                liste_panier_billet.append(Panier(id_billet, id_spectateur))
            return liste_panier_billet
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_spectateur(self, id_spectateur):
        try:
            query = text("select idB, idS from PANIER where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            liste_panier_spectateur = []
            for id_billet, id_spectateur in resultat:
                liste_panier_spectateur.append(Panier(id_billet, id_spectateur))
            return liste_panier_spectateur
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def payer_billet(self, id_billet, id_spectateur):
        try:
            query = text(f"insert into PANIER values({str(id_billet)} , {str(id_spectateur)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un panier réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def supprimer_billet(self, id_billet, id_spectateur):
        try:
            query = text("delete from PANIER where idB = " + str(id_billet) + " and idS = " + str(id_spectateur))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression d'un billet du panier réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
