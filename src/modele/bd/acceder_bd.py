import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from acceder import Acceder

class AccederBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_acceder(self):
        try:
            query = text("select idB, idJ from ACCEDER")
            resultat = self.__connexion.execute(query)
            liste_acceder = []
            for id_billet, id_journee in resultat:
                liste_acceder.append(
                    Acceder(id_billet, id_journee)
                )
            return liste_acceder
        except Exception as exp:
            print(f"Erreur lors de la récupération des acceder : {exp}")
            return None

    def get_par_id_billet(self, id_billet):
        try:
            query = text("select idB, idJ from ACCEDER where idB = " + str(id_billet))
            resultat = self.__connexion.execute(query)
            les_acceder_billet = []
            for id_billet, id_journee in resultat:
                les_acceder_billet.append(Acceder(id_billet, id_journee))
            return les_acceder_billet
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_journee(self, id_journee):
        try:
            query = text("select idB, idJ from ACCEDER where idJ = " + str(id_journee))
            resultat = self.__connexion.execute(query)
            les_acceder_journee = []
            for id_billet, id_journee in resultat:
                les_acceder_journee.append(Acceder(id_billet, id_journee))
            return les_acceder_journee
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_acceder(self, id_billet, id_journee):
        try:
            query = text(f"insert into ACCEDER values({str(id_billet)} , {str(id_journee)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un acceder réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None