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
    return liste_evenements_du_groupe


def lister_billets_de_spectateur(id_spectateur):
    """
        Liste les billets possédés par le spectateur avec l'id entré en paramètre.

        Args:
            id_spectateur (int): l'id du spectateur.
            
        Returns:
            (List[BILLET]) :la liste des billets possédés par l'utilisateur demandé.
    """
    liste_billets_du_spectateur = []
    liste_spectateurs = SPECTATEUR.get_all_spectateurs()
    for spectateurActuel in liste_spectateurs:
        if spectateurActuel.get_id_spectateur() == id_spectateur:
            liste_billets_du_spectateur.append(spectateurActuel)
    return liste_billets_du_spectateur


def lister_groupe_meme_style(id_groupe):
    """
        Liste les id de groupe des groupes qui ont le même style que celui entré en paramètre (recommandation selon le style d groupe actuel).
        
        Args:
            id_groupe: l'id du groupe actuel et duquel la recommandation selon le style sera appliquée.

        Args:
            (List[GROUPES]): Les groupes avec le même style que le groupe passé en paramètre.
    """
    liste_groupes_meme_style = []
    liste_groupes = GROUPE.get_all_groupes()
    for groupeActuel in liste_groupes:
        if groupeActuel.get_style(groupeActuel.get_id()) == GROUPE.get_style(id_groupe):
            liste_groupes_meme_style.append(groupeActuel)
    return liste_groupes_meme_style

def lister_evenements_par_journee(dateJournee):
    """
        Liste les événement qui ont lieu durant la date donnée.
        
        Args:
            dateJournee: La date de la journée à vérifier.

        Args:
            (List[EVENEMENT]): Les événement qui ont lieu durant dateJournee.
    """
    liste_evenements_journee= []
    liste_evenements = EVENEMENT.get_all_evenements()
    for evenementActuel in liste_evenements:
        if evenementActuel.get_id_journee() == JOURNEE.get_par_date_journee(dateJournee).get_id():
            liste_evenements_journee.append(evenementActuel)
    return liste_evenements_journee
    
            
    