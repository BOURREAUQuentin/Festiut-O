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
        try:
            query = text("select max(idRV) as m from RESEAU_VIDEO")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None

    def get_all_reseaux_videos(self):
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
        try:
            query = text(f"insert into RESEAU_VIDEO values({str(id_reseau_video)} ,'{nom}', '{lien}', {str(id_groupe)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un réseau vidéo réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None