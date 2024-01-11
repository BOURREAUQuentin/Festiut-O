import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from journee import Journee

class JourneeBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_journee(self):
        try:
            query = text("select max(idJ) as m from JOURNEE")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_journees(self):
        try:
            query = text("select idJ, dateJ from JOURNEE")
            resultat = self.__connexion.execute(query)
            liste_journees = []
            for id_journee, date in resultat:
                liste_journees.append(
                    Journee(id_journee, date)
                )
            return liste_journees
        except Exception as exp:
            print(f"Erreur lors de la récupération des journees : {exp}")
            return None

    def get_par_id_journee(self, id_journee):
        try:
            query = text("select idJ, dateJ from JOURNEE where idJ = " + str(id_journee))
            resultat = self.__connexion.execute(query)
            la_journee = None
            for id_journee, date in resultat:
                la_journee = Journee(id_journee, date)
            return la_journee
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def get_par_date_journee(self, date_journee):
        try:
            # possible car la date de la journée est unique
            query = text("select idJ, dateJ from JOURNEE where dateJ = '" + str(date_journee)+"'")
            resultat = self.__connexion.execute(query)
            la_journee = None
            for id_journee, date in resultat:
                la_journee = Journee(id_journee, date)
            return la_journee
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_journee(self, id_journee, date):
        try:
            query = text(f"insert into JOURNEE values({str(id_journee)} , {str(date)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'une journée réussie !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None