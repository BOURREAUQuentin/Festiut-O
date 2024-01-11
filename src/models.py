"""
    Ce fichier sert de lien avec la bd
"""
from connexion import connexion
from a_sous_style_bd import ASousStyleBD
from acceder_bd import AccederBD
from acheter_bd import AcheterBD
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
from panier_bd import PanierBD
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
ACHETER = AcheterBD(connexion)
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
PANIER = PanierBD(connexion)
RESEAU_SOCIAL = ReseauSocialBD(connexion)
RESEAU_VIDEO = ReseauVideoBD(connexion)
SPECTATEUR = SpectateurBD(connexion)
STYLE_MUSICAL = StyleMusicalBD(connexion)

def inserer_le_spectateur(nom, prenom, mail, date_naissance,tel, nom_utilisateur, mdp):
    """
        Cette permet d'appeler la fonction pour insérer un nouveau spectateur (utilisateur).
    """
    SPECTATEUR.inserer_spectateur(SPECTATEUR.get_prochain_id_spectateur(), nom, prenom,
                                  mail, date_naissance, tel, nom_utilisateur, mdp)

def lister_evenements_pour_billet(id_billet):
    """
        Retourne une liste de Evenement qui sont les évènements accessibles avec l'id billet.

        Args:
        Param: id_billet : l'id du billet.

        Returns:
            (List[Evenement]): la liste de Evenement qui sont les évènements accessibles avec l'id billet.
    """
    liste_evenements_avec_billet = []
    liste_acceder_avec_billet = ACCEDER.get_par_id_billet(id_billet)
    liste_id_journees_avec_billet = []
    for accederActuel in liste_acceder_avec_billet:
        liste_id_journees_avec_billet.append(accederActuel.get_id_journee())    
    liste_evenements = EVENEMENT.get_all_evenements()
    for evenementActuel in liste_evenements:
        for id_journee_avec_billet in liste_id_journees_avec_billet:
            if evenementActuel.get_id_journee() == id_journee_avec_billet:
                liste_evenements_avec_billet.append(evenementActuel)
    return liste_evenements_avec_billet

def lister_groupes_favoris_pour_spectateur(id_spectateur):
    """
        Retourne une liste de Groupe qui sont les groupes en favoris du spectateur (utilisateur connecté).

        Args:
        Param: id_spectateur : l'id du spectateur.

        Returns:
            (List[Evenement]): la liste de Groupe qui sont les groupes en favoris du spectateur.
    """
    liste_groupes_favoris = []
    liste_favoris_spectateur = FAVORI.get_par_id_spectateur(id_spectateur)
    for favori_spectateur in liste_favoris_spectateur:
        liste_groupes_favoris.append(GROUPE.get_par_id_groupe(favori_spectateur.get_id_groupe()))
    return liste_groupes_favoris

def rechercher_groupes_par_style_musical(nom_style_musical):
    """
        Retourne une liste de Groupe qui ont un style musical contenant la recherche d'un utilisateur.

        Args:
        Param: nom_style_musical : la recherche du style musical d'un utilisateur.

        Returns:
            (List[Groupe]): la liste de Groupe qui ont un style musical contenant la recherche d'un utilisateur.
    """
    liste_groupes_recherche = []
    liste_styles_musicals_recherche = STYLE_MUSICAL.get_recherche_par_nom_style_musical(nom_style_musical)
    for style_musical_recherche in liste_styles_musicals_recherche:
        liste_interpreter_avec_style_actuel = INTERPRETER.get_par_id_style_musical(style_musical_recherche.get_id())
        for interpreter_avec_style in liste_interpreter_avec_style_actuel:
            groupe_actuel = GROUPE.get_par_id_groupe(interpreter_avec_style.get_id_groupe())
            if groupe_actuel not in liste_groupes_recherche:
                liste_groupes_recherche.append(groupe_actuel)
    return STYLE_MUSICAL.get_recherche_par_nom_style_musical(nom_style_musical)

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

def au_moins_deux_artistes_dans_groupe(id_groupe):
    """
        Retourne True si le groupe contient au moins 2 artistes (si ce n'est pas un artiste seul), sinon False.

        Args:
        Param: id_groupe : l'id du groupe.

        Returns:
            (boolean): True si le groupe contient au moins 2 artistes, sinon False.
    """
    return len(FAIRE_PARTIE.get_par_id_groupe(id_groupe)) > 1

def supprimer_billet_panier(id_billet, id_spectateur):
    """
        Supprime un billet dans le panier du spectateur.

        Args:
        Param: id_billet : l'id du billet.
        Param: id_spectateur : l'id du spectateur.
    """
    PANIER.supprimer_billet(id_billet, id_spectateur)
