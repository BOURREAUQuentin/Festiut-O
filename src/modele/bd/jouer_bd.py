import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from jouer import Jouer

class JouerBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_jouer(self):
        try:
            query = text("select idA, idI from JOUER")
            resultat = self.__connexion.execute(query)
            liste_jouer = []
            for id_artiste, id_instrument in resultat:
                liste_jouer.append(
                    Jouer(id_artiste, id_instrument)
                )
            return liste_jouer
        except Exception as exp:
            print(f"Erreur lors de la récupération des jouer : {exp}")
            return None

    def get_par_id_artiste(self, id_artiste):
        try:
            query = text("select idA, idI from JOUER where idA = " + str(id_artiste))
            resultat = self.__connexion.execute(query)
            les_jouer_artiste = []
            for id_artiste, id_instrument in resultat:
                les_jouer_artiste.append(Jouer(id_artiste, id_instrument))
            return les_jouer_artiste
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def get_par_id_instrument(self, id_instrument):
        try:
            query = text("select idA, idI from JOUER where idI = " + str(id_instrument))
            resultat = self.__connexion.execute(query)
            les_jouer_instrument = []
            for id_instrument, id_instrument in resultat:
                les_jouer_instrument.append(Jouer(id_instrument, id_instrument))
            return les_jouer_instrument
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_jouer(self, id_artiste, id_instrument):
        try:
            query = text(f"insert into JOUER values({str(id_artiste)} , {str(id_instrument)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un jouer réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None