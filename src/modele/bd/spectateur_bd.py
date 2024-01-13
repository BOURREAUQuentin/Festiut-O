import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from spectateur import Spectateur

class SpectateurBD:
    def __init__(self, connexion):
        self.__connexion = connexion
    
    def get_prochain_id_spectateur(self):
        """Calcul l'id duprochain spectateur de la bd

        Returns:
            int: l'id du prochain spectateur
        """
        try:
            query = text("select max(idS) as m from SPECTATEUR")
            resultat = self.__connexion.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as exp:
            print("La connexion a échoué !")
            return None
    
    def get_all_spectateurs(self):
        """Renvoie la liste de tous les spectateurs de la bd

        Returns:
            List(Spectateur): la liste de tous les spectateurs
        """
        try:
            query = text("select idS, nomS, prenomS, mailS, dateNaissS, telS, nomUtilisateurS, mdpS, adminS from SPECTATEUR")
            resultat = self.__connexion.execute(query)
            liste_spectateurs = []
            for id_spectateur, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp, admin in resultat:
                liste_spectateurs.append(
                    Spectateur(id_spectateur, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp, admin)
                )
            return liste_spectateurs
        except Exception as exp:
            print(f"Erreur lors de la récupération des spectateurs : {exp}")
            return None
    
    def get_par_id_spectateur(self, id_spectateur):
        """Renvoie le spectateur avec cet id

        Args:
            id_spectateur (int): l'id spectateur

        Returns:
            Spectateur: le spectateur avec cet id
        """
        try:
            query = text("select idS, nomS, prenomS, mailS, dateNaissS, telS, nomUtilisateurS, mdpS, adminS from SPECTATEUR where idS = " + str(id_spectateur))
            resultat = self.__connexion.execute(query)
            le_spectateur = None
            for id_spectateur, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp, admin in resultat:
                le_spectateur = Spectateur(id_spectateur, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp, admin)
            return le_spectateur
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def inserer_spectateur(self, id_spectateur, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp):
        """Ajoute un spectateur dans le bd

        Args:
            id_spectateur (int): l'id du spectateur
            nom (String): le nom du spectateur
            prenom (String): le prenom du spectateur
            mail (String): le mail du spectateur
            date_naissance (DateTime): le date de naissance du spectateur
            tel (String): le telephone du spectateur
            nom_utilisateur (String): le nom utilisateur du spectateur
            mdp (String): le mot de passe du spectateur

        Returns:
            _type_: _description_
        """
        try:
            # met automatiquement N pour l'admin car on ne peut créer un admin sur l'application (uniquement en sql auparavant)
            query = text(f"insert into SPECTATEUR values({str(id_spectateur)} ,'{nom}', '{prenom}' ,'{mail}' ,{str(date_naissance)} ,{str(tel)} ,'{nom_utilisateur}' ,'{mdp}' ,'N')")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un spectateur réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None