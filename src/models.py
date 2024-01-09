"""
    Ce fichier sert de lien avec la bd
"""
from connexion import connexion
from a_sous_style_bd import ASousStyleBD
from acceder_bd import AccederBD
from artiste_bd import ArtisteBD
from billet_bd import BilletBD
from evenement_bd import EvenementBD
from faire_partie_bd import FairePartieBD
from favori_bd import FavoriBD
from groupe_bd import GroupeBD
from hebergement_bd import HebergementBD
from instrument_bd import InstrumentBD
from interpreter_bd import InterpreterBD
from jouer_bd import JouerBD
from journee_bd import JourneeBD
from lieu_bd import LieuBD
from reseau_social_bd import ReseauSocialBD
from reseau_video_bd import ReseauVideoBD
from spectateur_bd import SpectateurBD
from style_musical_bd import StyleMusicalBD

import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))

A_SOUS_STYLE = ASousStyleBD(connexion)
ACCEDER = AccederBD(connexion)
ARTISTE = ArtisteBD(connexion)
BILLET = BilletBD(connexion)
EVENEMENT = EvenementBD(connexion)
FAIRE_PARTIE = FairePartieBD(connexion)
FAVORI = FavoriBD(connexion)
GROUPE = GroupeBD(connexion)
HEBERGEMENT = HebergementBD(connexion)
INSTRUMENT = InstrumentBD(connexion)
INTERPRETER = InterpreterBD(connexion)
JOUER = JouerBD(connexion)
JOURNEE = JourneeBD(connexion)
LIEU = LieuBD(connexion)
RESEAU_SOCIAL = ReseauSocialBD(connexion)
RESEAU_VIDEO = ReseauVideoBD(connexion)
SPECTATEUR = SpectateurBD(connexion)
STYLE_MUSICAL = StyleMusicalBD(connexion)

def lister_evenements_pour_groupe(id_groupe):
    """
        Retourne une liste de Evenement qui sont les évènements organisés du groupe.

        Args:
        Param: id_groupe : l'id du groupe.

        Returns:
            (List[Evenement]): la liste de Evenement qui sont les évènements organisés du groupe.
    """
    liste_evenements_du_groupe = []
    liste_evenements = EVENEMENT.get_all_evenements()
    for evenementActuel in liste_evenements:
        if evenementActuel.get_id_groupe() == id_groupe:
            liste_evenements_du_groupe.append(evenementActuel)
            print("evenement du groupe")
    return liste_evenements_du_groupe