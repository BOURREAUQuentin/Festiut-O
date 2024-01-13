import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from groupe import Groupe
from style_musical import StyleMusical

class GroupeBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_groupe(self):
        """Permet de calculer le prochain id du groupe à ajouter dans la bd

        Returns:
            int: l'id du prochain groupe
        """
        try:
            query = text("select max(idG) as m from GROUPE")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_groupes(self):
        """Renvoie la liste de tous les groupes

        Returns:
            List(Group): la liste de tous les groupes
        """
        try:
            query = text("select idG, nomG, courteDescriptionG, longueDescriptionG, lienImageG from GROUPE")
            resultat = self.__connexion.execute(query)
            liste_groupes = []
            for id_groupe, nom, courte_description, longue_description, lien_image in resultat:
                liste_groupes.append(
                    Groupe(id_groupe, nom, courte_description, longue_description, lien_image)
                )
            return liste_groupes
        except Exception as exp:
            print(f"Erreur lors de la récupération des groupes : {exp}")
            return None

    def get_par_id_groupe(self, id_groupe):
        """Renvoie le groupe avec cet id

        Args:
            id_groupe (int): l'id du groupe recherché

        Returns:
            int: le groupe avec cet id
        """
        try:
            query = text("select idG, nomG, courteDescriptionG, longueDescriptionG, lienImageG from GROUPE where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            le_groupe = None
            for id_groupe, nom, courte_description, longue_description, lien_image in resultat:
                le_groupe = Groupe(id_groupe, nom, courte_description, longue_description, lien_image)
            return le_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_groupe(self, id_groupe, nom, courte_description, longue_description, lien_image):
        """Ajoute un groupe dans la bd

        Args:
            id_groupe (int): l'id du groupe
            nom (String): le nom du groupe
            courte_description (String): la description courte du groupe
            longue_description (String): la description longue du groupe
            lien_image (String): le lien de l'image du groupe

        Returns:
            _type_: _description_
        """
        try:
            query = text(f"insert into GROUPE values({str(id_groupe)} ,'{nom}', '{courte_description}', '{longue_description}', '{lien_image}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un groupe réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
        
    def get_style(self, id_groupe):
        """Renvoie le style du groupe

        Args:
            id_groupe (int): l'id du groupe 

        Returns:
            Style: le style du groupe
        """
        try:
            query = text("select idSt from INTERPRETER where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            le_style = None
            for id_style in resultat:
                le_style = StyleMusical(id_style)
            return le_style
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def supprimer_groupe(self, id_groupe):
        """Supprime groupe dans la bd

        Args:
            id_groupe (int): l'id du groupe
        """
        try:
            query = text("delete from GROUPE where idG = " + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression du groupe réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None