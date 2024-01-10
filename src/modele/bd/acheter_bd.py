import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from acheter import Acheter

class AcheterBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_acheter(self):
        try:
            query = text("select idB, idS from ACHETER")
            resultat = self.__connexion.execute(query)
            lisste_faire_partie = []
            for id_billet, id_spectateur in resultat:
                lisste_faire_partie.append(
                    Acheter(id_billet, id_spectateur)
                )
            return lisste_faire_partie
        except Exception as exp:
            print(f"Erreur lors de la récupération des faire_partie : {exp}")
            return None

    def get_par_id_billet(self, id_billet):
        try:
            query = text("select idB, idS from ACHETER where idB = " + str(id_billet))
            resultat = self.__connexion.execute(query)
            les_faire_partie_groupe = []
            for id_billet, id_spectateur in resultat:
                les_faire_partie_groupe.append(Acheter(id_billet, id_spectateur))
            return les_faire_partie_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_spectateur(self, id_spectateur):
        try:
            query = text("select idB, idS from ACHETER where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            les_faire_partie_artiste = []
            for id_billet, id_spectateur in resultat:
                les_faire_partie_artiste.append(Acheter(id_billet, id_spectateur))
            return les_faire_partie_artiste
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def payer_billet(self, id_billet, id_spectateur):
        try:
            query = text(f"insert into ACHETER values({str(id_billet)} , {str(id_spectateur)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un acheter réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
