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
        try:
            query = text("select idG, idSt from INTERPRETER")
            resultat = self.__connexion.execute(query)
            lisste_interpreter = []
            for id_groupe, id_style_musical in resultat:
                lisste_interpreter.append(
                    Interpreter(id_groupe, id_style_musical)
                )
            return lisste_interpreter
        except Exception as exp:
            print(f"Erreur lors de la récupération des interpreter : {exp}")
            return None

    def get_par_id_groupe(self, id_groupe):
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
        try:
            query = text(f"insert into INTERPRETER values({str(id_groupe)} , {str(id_style_musical)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un interpreter réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None