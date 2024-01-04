import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/python/'))

from a_sous_style import ASousStyle

class ASousStyleBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_a_sous_style(self):
        try:
            query = text("select idSt1, idSt2 from A_SOUS_STYLE")
            resultat = self.__connexion.execute(query)
            liste_a_sous_style = []
            for id_style_principal, id_sous_style in resultat:
                liste_a_sous_style.append(
                    ASousStyle(id_style_principal, id_sous_style)
                )
            return liste_a_sous_style
        except Exception as exp:
            print(f"Erreur lors de la récupération des a_sous_style : {exp}")
            return None

    def get_par_id_style_principal(self, id_style_principal):
        try:
            query = text("select idSt1, idSt2 from A_SOUS_STYLE where idSt1 = " + str(id_style_principal))
            resultat = self.__connexion.execute(query)
            les_a_sous_style_style_principal = []
            for id_style_principal, id_sous_style in resultat:
                les_a_sous_style_style_principal.append(ASousStyle(id_style_principal, id_sous_style))
            return les_a_sous_style_style_principal
        except Exception as exp:
            print("la connexion a échoué !")
            return None

    def get_par_id_sous_style(self, id_sous_style):
        try:
            query = text("select idSt1, idSt2 from A_SOUS_STYLE where idSt2 = " + str(id_sous_style))
            resultat = self.__connexion.execute(query)
            les_a_sous_style_sous_style = []
            for id_style_principal, id_sous_style in resultat:
                les_a_sous_style_sous_style.append(ASousStyle(id_style_principal, id_sous_style))
            return les_a_sous_style_sous_style
        except Exception as exp:
            print("la connexion a échoué !")
            return None
    
    def ajouter_a_sous_style(self, id_style_principal, id_sous_style):
        try:
            query = text(f"insert into A_SOUS_STYLE values({str(id_style_principal)} , {str(id_sous_style)})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            print("Ajout d'un a_sous_style réussi !")
        except Exception as exp:
            print("La connexion a échoué !")
            return None