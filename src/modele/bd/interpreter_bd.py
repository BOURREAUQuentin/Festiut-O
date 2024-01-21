import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from interpreter import Interpreter

class InterpreterBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_interpreter(self):
        """Renvoie la liste de toutes les associations interpréter

        Returns:
            List(Interpreter): la liste de toutes les associations interpréter
        """
        try:
            query = text("select idG, idSt from INTERPRETER")
            resultat = self.__connexion.execute(query)
            liste_interpreter = []
            for id_groupe, id_style_musical in resultat:
                liste_interpreter.append(
                    Interpreter(id_groupe, id_style_musical)
                )
            return liste_interpreter
        except Exception as exp:
            print(f"Erreur lors de la récupération des interpreter : {exp}")
            return None

    def get_par_id_groupe(self, id_groupe):
        """Renvoie l'association liuée avec cet id de groupe

        Args:
            id_groupe (int): l'id de groupe

        Returns:
            Interpreter: l'association correspondante
        """
        try:
            query = text("select idG, idSt from INTERPRETER where idG = " + str(id_groupe))
            resultat = self.__connexion.execute(query)
            les_interpreter_groupe = []
            for id_groupe, id_style_musical in resultat:
                les_interpreter_groupe.append(Interpreter(id_groupe, id_style_musical))
            return les_interpreter_groupe
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def get_par_id_style_musical(self, id_style_musical):
        """Renvoie l'association liée avec cet id de style musical

        Args:
            id_style_musical (int): l'id du style

        Returns:
            Interpreter: l'association correspondante
        """
        try:
            query = text("select idG, idSt from INTERPRETER where idSt = " + str(id_style_musical))
            resultat = self.__connexion.execute(query)
            les_interpreter_style_musical = []
            for id_groupe, id_style_musical in resultat:
                les_interpreter_style_musical.append(Interpreter(id_groupe, id_style_musical))
            return les_interpreter_style_musical
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_jouer(self, id_groupe, id_style_musical):
        """Ajoute une association Interpreter dans la bd

        Args:
            id_groupe (int): l'id du groupe
            id_style_musical (int): l'id du style musical

        Returns:
            _type_: _description_
        """
        try:
            query = text(f"insert into INTERPRETER values({str(id_groupe)} , {str(id_style_musical)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un interpreter réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None
        
    def supprimer_avec_id_groupe(self, id_groupe):
        """Supprime l'association interpreter dans la bd avec l'id du groupe

        Args:
            id_groupe (int): l'id du groupe
        """
        try:
            query = text("delete from INTERPRETER where idG = " + str(id_groupe))
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Suppression de interpreter réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None