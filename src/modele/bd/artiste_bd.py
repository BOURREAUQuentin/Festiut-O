import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from artiste import Artiste

class ArtisteBD:
    def __init__(self, connexion):
        self.__connexion = connexion
    
    def get_prochain_id_artiste(self):
        try:
            query = text("select max(idA) as m from ARTISTE")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None
    
    def get_all_artistes(self):
        try:
            query = text("select idA, nomA, descriptionA from ARTISTE")
            resultat = self.__connexion.execute(query)
            liste_artistes = []
            for id_artiste, nom, description in resultat:
                liste_artistes.append(
                    Artiste(id_artiste, nom, description)
                )
            return liste_artistes
        except Exception as exp:
            print(f"Erreur lors de la récupération des artistes : {exp}")
            return None
    
    def get_par_id_artiste(self, id_artiste):
        try:
            query = text("select idA, nomA, descriptionA from ARTISTE where idA = " + str(id_artiste))
            resultat = self.__connexion.execute(query)
            le_spectateur = None
            for id_artiste, nom, description in resultat:
                le_spectateur = Artiste(id_artiste, nom, description)
            return le_spectateur
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def inserer_artiste(self, id_artiste, nom, description):
        try:
            query = text(f"insert into ARTISTE values({str(id_artiste)} ,'{nom}', '{description}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un artiste réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None