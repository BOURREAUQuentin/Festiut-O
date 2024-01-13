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
        """Permet de connaitre l'id du prochain artiste à insérer

        Returns:
            int: l'id du prochain artiste
        """
        try:
            query = text("select max(idA) as m from ARTISTE")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None
    
    def get_all_artistes(self):
        """Permet de récupérer la liste de tous les artistes

        Returns:
            List(Artiste): la liste de tous les artises
        """
        try:
            query = text("select idA, nomA, descriptionA, lienImageA from ARTISTE")
            resultat = self.__connexion.execute(query)
            liste_artistes = []
            for id_artiste, nom, description, lien_image in resultat:
                liste_artistes.append(
                    Artiste(id_artiste, nom, description, lien_image)
                )
            return liste_artistes
        except Exception as exp:
            print(f"Erreur lors de la récupération des artistes : {exp}")
            return None
    
    def get_par_id_artiste(self, id_artiste):
        """Permet de récupérer un artiste grâce à son id

        Args:
            id_artiste (int): l'id de l'artiste

        Returns:
            Artiste: l'artiste correspondant à l'id
        """
        try:
            query = text("select idA, nomA, descriptionA, lienImageA from ARTISTE where idA = " + str(id_artiste))
            resultat = self.__connexion.execute(query)
            l_artiste = None
            for id_artiste, nom, description, lien_image in resultat:
                l_artiste = Artiste(id_artiste, nom, description, lien_image)
            return l_artiste
        except Exception as exp:
            print("la connexion a échoué !")
            return None
        
    def get_recherche_par_nom_artiste(self, nom_artiste):
        """Permet de récupérer un artiste grâce à son nom

        Args:
            nom_artiste (Strinf): Le nom de l'artiste

        Returns:
            Artiste: L'artiste correspondant au nom
        """
        try:
            query = text("select idA, nomA, descriptionA from ARTISTE where nomA LIKE '%" + nom_artiste + "%'")
            resultat = self.__connexion.execute(query)
            liste_artistes = []
            for id_artiste, nom_artiste, description_artiste in resultat:
                liste_artistes.append(
                    Artiste(id_artiste, nom_artiste, description_artiste)
                )
            return liste_artistes
        except Exception as exp:
            print(f"Erreur lors de la recherche des styles musicaux : {exp}")
            return None
    
    def inserer_artiste(self, id_artiste, nom, description, lien_image):
        """Permet d'insérer un artiste dans la base de données

        Args:
            id_artiste (int): l'id de l'artiste
            nom (String): le nom de l'artiste
            description (String): la description de l'artiste
            lien_image (String): l'image liée à l'artiste

        """
        try:
            query = text(f"insert into ARTISTE values({str(id_artiste)} ,'{nom}', '{description}', '{lien_image}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un artiste réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None