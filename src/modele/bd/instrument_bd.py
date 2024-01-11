import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from instrument import Instrument

class InstrumentBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_instrument(self):
        try:
            query = text("select max(idI) as m from INSTRUMENT")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_instruments(self):
        try:
            query = text("select idI, nomI from INSTRUMENT")
            resultat = self.__connexion.execute(query)
            liste_instruments = []
            for id_instrument, nom in resultat:
                liste_instruments.append(
                    Instrument(id_instrument, nom)
                )
            return liste_instruments
        except Exception as exp:
            print(f"Erreur lors de la récupération des instruments : {exp}")
            return None

    def get_par_id_instrument(self, id_instrument):
        try:
            query = text("select idI, nomI from INSTRUMENT where idI = " + str(id_instrument))
            resultat = self.__connexion.execute(query)
            l_instrument = None
            for id_instrument, nom in resultat:
                l_instrument = Instrument(id_instrument, nom)
            return l_instrument
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_instrument(self, id_instrument, nom):
        try:
            query = text(f"insert into INSTRUMENT values({str(id_instrument)} ,'{nom}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un instrument réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None