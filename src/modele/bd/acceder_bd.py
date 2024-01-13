from datetime import datetime
import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from acceder import Acceder

class AccederBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_acceder(self):
        """Fonction qui permet de récupérer tous les "accéder".

        Returns:
            List(acceder_bd): La liste accéder.
        """
        try:
            query = text("select idB, idJ from ACCEDER")
            resultat = self.__connexion.execute(query)
            liste_acceder = []
            for id_billet, id_journee in resultat:
                liste_acceder.append(
                    Acceder(id_billet, id_journee)
                )
            return liste_acceder
        except Exception as exp:
            print(f"Erreur lors de la récupération des acceder : {exp}")
            return None

    def get_par_id_billet(self, id_billet):
        """Fonction qui permet de récupérer un accès grâce à un bittet

        Args:
            id_billet (int): Le billet

        Returns:
            List(Acceder): La liste des accès permis par le billet.
        """
        try:
            query = text("select idB, idJ from ACCEDER where idB = " + str(id_billet))
            resultat = self.__connexion.execute(query)
            les_acceder_billet = []
            for id_billet, id_journee in resultat:
                les_acceder_billet.append(Acceder(id_billet, id_journee))
            return les_acceder_billet
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_journee(self, id_journee):
        """Permet de recupérer les accès de la journée

        Args:
            id_journee (int): l'id de la journée

        Returns:
            List(Acceder): La list des accès de la journée
        """
        try:
            query = text("select idB, idJ from ACCEDER where idJ = " + str(id_journee))
            resultat = self.__connexion.execute(query)
            les_acceder_journee = []
            for id_billet, id_journee in resultat:
                les_acceder_journee.append(Acceder(id_billet, id_journee))
            return les_acceder_journee
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_les_journees_billetterie(self):
        """Recupère les journées accessibles par rapport au billet

        Returns:
            List(String): la liste des accès selon les billets (week-end,samedi,dimanche)
        """
        try:
            query = text("select idB, count(idJ) nbJ, dateJ from ACCEDER natural join JOURNEE group by idB")
            resultat = self.__connexion.execute(query)
            liste_journees = []
            for _, nb_journees_accessible, date_journee in resultat:
                if nb_journees_accessible > 1:
                    liste_journees.append("Week-end")
                else:
                    # conversion de la date du 2024-07-18 en datetime comme dateJ dans la bd
                    if date_journee == datetime.strptime("2024-07-18", "%Y-%m-%d").date():
                        liste_journees.append("Samedi")
                    else:
                        liste_journees.append("Dimanche")
            return liste_journees
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_acceder(self, id_billet, id_journee):
        """Permet d'ajouter un accès dans la base de données

        Args:
            id_billet (int): le billet associé à l'accès
            id_journee (int): la journée à laquelle il faut accéder
        """
        try:
            query = text(f"insert into ACCEDER values({str(id_billet)} , {str(id_journee)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un acceder réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None