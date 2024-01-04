import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from hebergement import Hebergement

class HebergementBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_hebergement(self):
        try:
            query = text("select max(idH) as m from HEBERGEMENT")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_hebergements(self):
        try:
            query = text("select idH, nomH, adresseH, nbPlacesMaxH from HEBERGEMENT")
            resultat = self.__connexion.execute(query)
            liste_hebergements = []
            for id_hebergement, nom, adresse, nb_places_max in resultat:
                liste_hebergements.append(
                    Hebergement(id_hebergement, nom, adresse, nb_places_max)
                )
            return liste_hebergements
        except Exception as exp:
            print(f"Erreur lors de la récupération des hébergements : {exp}")
            return None

    def get_par_id_hebergement(self, id_hebergement):
        try:
            query = text("select idH, nomH, adresseH, nbPlacesMaxH from HEBERGEMENT where idH = " + str(id_hebergement))
            resultat = self.__connexion.execute(query)
            l_hebergement = None
            for id_hebergement, nom, adresse, nb_places_max in resultat:
                l_hebergement = Hebergement(id_hebergement, nom, adresse, nb_places_max)
            return l_hebergement
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_hebergement(self, id_hebergement, nom, adresse, nb_places_max):
        try:
            query = text(f"insert into HEBERGEMENT values({str(id_hebergement)} ,'{nom}','{adresse}' ,{str(nb_places_max)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un hébergement réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None