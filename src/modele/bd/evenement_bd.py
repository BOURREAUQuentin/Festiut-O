import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from evenement import Evenement
from groupe import Groupe
from lieu import Lieu

class EvenementBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_evenement(self):
        """Permet de calculer l'id du prochain événement à insérer

        Returns:
            int: l'id du prochain événement
        """
        try:
            query = text("select max(idE) as m from EVENEMENT")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_evenements(self):
        """Renvoie la liste de tous les événements dans la bd

        Returns:
            List(Evenement): la liste de tous les événements de la bd
        """
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
        """Renvoie l'événement qui correspond à l'id

        Args:
            id_evenement (int): l'id de l'évenement

        Returns:
            Evenement: l'événement correspondant à l'id
        """
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
        """Ajoute un événement dans la bd

        Args:
            id_evenement (int): l'id de l'événement
            nom (String): le nom de l'événement
            description (String): la description de l'événement
            heure_debut (DateTime): l'heure de début de l'évenement
            duree (DateTime): la durée de l'évenement
            tpsMontage (DateTime): le temps de montage de l'évenement
            tpsDemontage (DateTime): le temps de démontage de l'évenement
            id_lieu (int): l'id du lieu de l'évenement
            id_journee (int): l'id de la journée
            id_groupe (int): l'id du groupe
        """
        try:
            query = text(f"insert into EVENEMENT values({str(id_evenement)} ,'{nom}', '{description}', {str(heure_debut)}, {str(duree)}, {str(tpsMontage)}, {str(tpsDemontage)}, {str(id_lieu)}, {str(id_journee)}, {str(id_groupe)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un évènement réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
    
    def get_all_evenements_pour_planning(self, dateJournee):
        """
        Retourne une liste de tuple contenant Evenement, Groupe, Lieu triés par heureDebutE croissant
        pour être affiché dans la page planning

        Returns:
            List[tuple(Evenement, Groupe, Lieu)]: liste de tuple contenant Evenement, Groupe, Lieu
            triés par heureDebutE croissant pour être affiché dans la page planning
        """
        try:
            query = text("select idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE, idL, idJ, idG, nomG, courteDescriptionG, longueDescriptionG, lienImageG, nomL, adresseL, nbMaxSpecL from EVENEMENT natural join GROUPE natural join LIEU order by heureDebutE ASC")
            resultat = self.__connexion.execute(query)
            liste_evenements_planning = []
            for id_evenement, nom, description, heure_debut, duree, tpsMontage, tpsDemontage, id_lieu, id_journee, id_groupe, nom_groupe, courte_description_groupe, longue_description_groupe, lien_image_groupe, nom_lieu, adresse_lieu, nb_max_spect_lieu in resultat:
                liste_evenements_planning.append(
                    (Evenement(id_evenement, nom, description, heure_debut, duree, tpsMontage, tpsDemontage, id_lieu, id_journee, id_groupe),
                     Groupe(id_groupe, nom_groupe, courte_description_groupe, longue_description_groupe, lien_image_groupe),
                     Lieu(id_lieu, nom_lieu, adresse_lieu, nb_max_spect_lieu))
                )
            return liste_evenements_planning
        except Exception as exp:
            print(f"Erreur lors de la récupération des évènements/groupes/lieux : {exp}")
            return None

    def supprimer_avec_id_groupe(self, id_groupe):
        """Supprime l'evenement dans la bd avec l'id du groupe

        Args:
            id_groupe (int): l'id du groupe
        """
        try:
            query = text("delete from EVENEMENT where idG = " + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression de evenement réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
        
    def supprimer_evenement(self, id_evenement):
        """Supprime l'evenement dans la bd avec cet id

        Args:
            id_evenement (int): l'id de l'evenement a supprimer
        """
        try:
            query = text("delete from EVENEMENT where idE = " + str(id_evenement))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression de evenement réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None