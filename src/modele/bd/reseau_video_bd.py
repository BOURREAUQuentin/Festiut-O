import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from reseau_video import ReseauVideo

class ReseauVideoBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_prochain_id_reseau_video(self):
        """Calcul l'id du prochain réseau vidéo de la bd

        Returns:
            int: le prochain idreseau video
        """
        try:
            query = text("select max(idRV) as m from RESEAU_VIDEO")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_reseaux_videos(self):
        """Renvoie la liste de tous les réseaux videos

        Returns:
            List(ReseauVideo): la liste de réseaux vidéos
        """
        try:
            query = text("select idRV, nomRV, lienRV, idG from RESEAU_VIDEO")
            resultat = self.__connexion.execute(query)
            liste_reseaux_videos = []
            for id_reseau_video, nom, lien, id_groupe in resultat:
                liste_reseaux_videos.append(
                    ReseauVideo(id_reseau_video, nom, lien, id_groupe)
                )
            return liste_reseaux_videos
        except Exception as exp:
            print(f"Erreur lors de la récupération des réseaux vidéos : {exp}")
            return None

    def get_par_id_reseau_video(self, id_reseau_video):
        """Renvoie le reseau vidéo avec cet id

        Args:
            id_reseau_video (int): l'id du reseau video

        Returns:
            ReseauVideo: le reseau vidéo avec cet id
        """
        try:
            query = text("select idRV, nomRV, lienRV, idG from RESEAU_VIDEO where idRV = " + str(id_reseau_video))
            resultat = self.__connexion.execute(query)
            le_reseau_video = None
            for id_reseau_video, nom, lien, id_groupe in resultat:
                le_reseau_video = ReseauVideo(id_reseau_video, nom, lien, id_groupe)
            return le_reseau_video
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def get_par_id_groupe(self, id_groupe):
        """Renvoie le reseau vidéo avec cet id de groupe

        Args:
            id_groupe (int): l'id du groupe

        Returns:
            ReseauVideo: le reseau vidéo avec cet  de groupe
        """
        try:
            query = text("select idRV, nomRV, lienRV, idG from RESEAU_VIDEO where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            liste_reseaux_videos_groupe = None
            for id_reseau_video, nom, lien, id_groupe in resultat:
                liste_reseaux_videos_groupe = ReseauVideo(id_reseau_video, nom, lien, id_groupe)
            return liste_reseaux_videos_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_reseau_video(self, id_reseau_video, nom, lien, id_groupe):
        """Ajoute un reseau video dans le bd

        Args:
            id_reseau_video (int): l'id du reseau video
            nom (String): le nom du reseau video
            lien (String): le lien du reseau video
            id_groupe (int): l'id du groupe associé

        Returns:
            _type_: _description_
        """
        try:
            query = text(f"insert into RESEAU_VIDEO values({str(id_reseau_video)} ,'{nom}', '{lien}', {str(id_groupe)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un réseau vidéo réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
        
    def supprimer_avec_id_groupe(self, id_groupe):
        """Supprime le reseau video dans la bd avec l'id du groupe

        Args:
            id_groupe (int): l'id du groupe
        """
        try:
            query = text("delete from RESEAU_VIDEO where idG = " + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression du reseau video réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None