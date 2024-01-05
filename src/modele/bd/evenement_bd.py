import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from evenement import Evenement

class EvenementBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_evenement(self):
        try:
            query = text("select max(idE) as m from EVENEMENT")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_evenements(self):
        try:
            query = text("select idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE, idL, idJ, idG from EVENEMENT")
            resultat = self.__connexion.execute(query)
            liste_evenements = []
            for id_evenement, nom, description, heure_debut, duree, tpsMontage, tpsDemontage, id_lieu, id_journee, id_groupe in resultat:
                liste_evenements.append(
                    Evenement(id_evenement, nom, description, heure_debut, duree, tpsMontage, tpsDemontage, id_lieu, id_journee, id_groupe)
                )
            return liste_evenements
        except Exception as exp:
            print(f"Erreur lors de la récupération des évènements : {exp}")
            return None

    def get_par_id_evenement(self, id_evenement):
        try:
            query = text("select idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE, idL, idJ, idG from EVENEMENT where idE = " + str(id_evenement))
            resultat = self.__connexion.execute(query)
            l_evenement = None
            for id_evenement, nom, description, heure_debut, duree, tpsMontage, tpsDemontage, id_lieu, id_journee, id_groupe in resultat:
                l_evenement = Evenement(id_evenement, nom, description, heure_debut, duree, tpsMontage, tpsDemontage, id_lieu, id_journee, id_groupe)
            return l_evenement
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_evenement(self, id_evenement, nom, description, heure_debut, duree, tpsMontage, tpsDemontage, id_lieu, id_journee, id_groupe):
        try:
            query = text(f"insert into EVENEMENT values({str(id_evenement)} ,'{nom}', '{description}', {str(heure_debut)}, {str(duree)}, {str(tpsMontage)}, {str(tpsDemontage)}, {str(id_lieu)}, {str(id_journee)}, {str(id_groupe)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un évènement réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None