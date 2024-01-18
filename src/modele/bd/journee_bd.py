from datetime import datetime
import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from journee import Journee
from groupe import Groupe

class JourneeBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_journee(self):
        """Calcul le prochain id de la journée dans la bd

        Returns:
            int: l'id de la prochaine journée
        """
        try:
            query = text("select max(idJ) as m from JOURNEE")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_journees(self):
        """Renvoie la liste de toutes les journées de la bd

        Returns:
            List(Journee): la liste de toutes les journées
        """
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
        """Renvoie la journée avec cet id

        Args:
            id_journee (int): l'id de la journée

        Returns:
            Journee: la journée correspondante
        """
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
        """Renvoie la journée avec cet date

        Args:
            date_journee (String): la date de la journée

        Returns:
            Journee: la journée correspondante
        """
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
    
    def get_groupes_par_journee(self, journee_billetterie):
        """Renvoie la liste de tous les groupes qui performent cette journée

        Args:
            journee_billetterie (String): le jour

        Returns:
            List(Group): la liste des groupes
        """
        try:
            date_journee = '2024-07-18'
            if journee_billetterie == "Dimanche":
                date_journee = '2024-07-19'
            if journee_billetterie == "Dimanche" or journee_billetterie == "Samedi":
                query = text("select idG, nomG, courteDescriptionG, longueDescriptionG, lienImageG from JOURNEE natural join EVENEMENT natural join GROUPE where dateJ = '" + str(date_journee) + "' limit 8")
                resultat = self.__connexion.execute(query)
                les_groupes_cette_journee = []
                for id_groupe, nom_groupe, courte_description_groupe, longue_description_groupe, lien_image_groupe in resultat:
                    les_groupes_cette_journee.append(Groupe(id_groupe, nom_groupe, courte_description_groupe, longue_description_groupe, lien_image_groupe))
                return les_groupes_cette_journee
            else: # cas où c'est le week-end
                query = text("select DISTINCT idG, nomG, courteDescriptionG, longueDescriptionG, lienImageG from GROUPE natural join EVENEMENT limit 8")
                resultat = self.__connexion.execute(query)
                les_groupes_ce_week_end = []
                for id_groupe, nom_groupe, courte_description_groupe, longue_description_groupe, lien_image_groupe in resultat:
                    les_groupes_ce_week_end.append(Groupe(id_groupe, nom_groupe, courte_description_groupe, longue_description_groupe, lien_image_groupe))
                return les_groupes_ce_week_end
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_journee(self, id_journee, date):
        """Ajoute une journée dans la bd

        Args:
            id_journee (int): l'id de la journée
            date (String): la date
        """
        try:
            query = text(f"insert into JOURNEE values({str(id_journee)} , {str(date)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'une journée réussie !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
    
    def get_dico_journees(self):
        try:
            query = text("select idJ, dateJ from JOURNEE")
            resultat = self.__connexion.execute(query)
            dico_journees = {}
            for id_journee, date in resultat:
                # conversion de la date du 2024-07-18 en datetime comme dateJ dans la bd
                if date == datetime.strptime("2024-07-18", "%Y-%m-%d").date():
                    dico_journees["Samedi"] = str(date)
                else:
                    dico_journees["Dimanche"] = str(date)
            return dico_journees
        except Exception as exp:
            print(exp)
            print("la connexion a échoué !")
            return None
