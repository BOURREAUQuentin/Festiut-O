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
from heberger_bd import HebergerBD

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
HEBERGER = HebergerBD(connexion)
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
    return SPECTATEUR.inserer_spectateur(SPECTATEUR.get_prochain_id_spectateur(), nom, prenom,
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
    return liste_evenements_du_groupe

def lister_groupes_meme_style(id_groupe):
    """
        Liste les id de groupe des groupes qui ont le même style que celui entré en paramètre (recommandation selon le style d groupe actuel).
        
        Args:
            id_groupe: l'id du groupe actuel et duquel la recommandation selon le style sera appliquée.

        Args:
            (List[GROUPES]): Les groupes avec le même style que le groupe passé en paramètre.
    """
    liste_groupes_meme_style = []
    liste_groupes = GROUPE.get_all_groupes()
    index_groupe = 1
    for _,groupeActuel in liste_groupes:
        if (groupeActuel.get_id() != int(id_groupe)) and (GROUPE.get_style(groupeActuel.get_id()) == GROUPE.get_style(id_groupe)):
            if len(liste_groupes_meme_style) < 3: # faire une limite de 3
                liste_groupes_meme_style.append((index_groupe, groupeActuel))
                index_groupe += 1
            else:
                break
    return liste_groupes_meme_style

def lister_evenements_par_journee(dateJournee):
    """
        Liste les événements (avec le groupe associé et le lieu) qui ont lieu durant la date donnée (triés par heureDebutE croissant).
        
        Args:
            dateJournee: La date de la journée à vérifier.

        Args:
            (List[tuple(Evenement, Groupe, Lieu)]): Les événements (avec le groupe associé et le lieu) qui ont lieu durant dateJournee et triés par heureDebutE croissant.
    """
    liste_evenements_journee= []
    liste_evenements = EVENEMENT.get_all_evenements_pour_planning(dateJournee)
    for evenementActuel in liste_evenements:
        if evenementActuel[0].get_id_journee() == JOURNEE.get_par_date_journee(dateJournee).get_id():
            liste_evenements_journee.append(evenementActuel)
    return liste_evenements_journee

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

def ajouter_billet_panier(id_billet, id_spectateur, initialise=False):
    """
        Ajoute au panier le billet qui est associé au spectateur connecté.

        Args:
        Param: id_billet : l'id du billet.
        Param: id_spectateur : l'id du spectateur.
        Param: initialise : true si c'est lors de l'inscription d'un nouvel utilisateur, sinon false.
    """
    if PANIER.get_billet_deja_dans_panier(id_billet, id_spectateur):
        print("deja billet dans panier")
        # si le billet est déjà dans le panier ca modifie la quantité de ce billet (donc ajoute 1)
        PANIER.update_quantite_billet_panier(id_billet, id_spectateur, 1)
    else:
        if not initialise:
            # le billet n'est pas déjà dans le panier du spectateur donc ca l'ajoute au panier (quantiteB = 1 par défaut)
            PANIER.ajouter_panier(id_billet, id_spectateur, 1)
        else:
            # on ajoute juste le billet de quantite zéro pour pouvoir le modifier dans le panier plus tard
            PANIER.ajouter_panier(id_billet, id_spectateur, 0)

def modifier_quantite_billet_panier(id_billet, id_spectateur, nouvelle_quantite_billet):
    """
        Modifie la quantité du billet sélectionné dans le panier (utilisable que dans la page panier).

        Args:
        Param: id_billet : l'id du billet.
        Param: id_spectateur : l'id du spectateur.
        Param: nouvelle_quantite_billet : la nouvelle quantite du billet.
    """
    PANIER.modifier_quantite_billet(id_billet, id_spectateur, nouvelle_quantite_billet)

def payer_panier(id_spectateur):
    """
        Paye le panier du spectateur connecté.

        Args:
        Param: id_spectateur : l'id du spectateur.
    """
    liste_panier_spectateur = PANIER.get_par_id_spectateur(id_spectateur)
    for billet_panier_spectateur in liste_panier_spectateur:
        if ACHETER.get_billet_deja_achete(billet_panier_spectateur.get_id_billet(), billet_panier_spectateur.get_id_spectateur()):
            # si le spectateur a déjà le billet dans le panier, ca actualise juste la quantité de ce billet
            ACHETER.update_quantite_billet_achete(billet_panier_spectateur.get_id_billet(), billet_panier_spectateur.get_id_spectateur(), billet_panier_spectateur.get_quantite_billet())
        else:
            if (int(billet_panier_spectateur.get_quantite_billet()) > 0):
                ACHETER.payer_billet(billet_panier_spectateur.get_id_billet(), billet_panier_spectateur.get_id_spectateur(), billet_panier_spectateur.get_quantite_billet())
        
def supprimer_un_spectateur(id_spect):
    """Supprime un spectateur dans la base de donnée en prenant en compte toutes ses associations

    Args:
        id_spect (int): l'id du spectateur à supprimer
    """
    ACHETER.supprimer_avec_id_spectateur(id_spect)
    PANIER.supprimer_avec_id_spectateur(id_spect)
    FAVORI.supprimer_avec_id_spectateur(id_spect)
    SPECTATEUR.supprimer_spectateur(id_spect)
            
def supprimer_un_groupe(id_groupe):
    """Supprime un groupe dans la base de donnée en prenant en compte toutes ses associations

    Args:
        id_spect (int): l'id du groupe à supprimer
    """
    RESEAU_VIDEO.supprimer_avec_id_groupe(id_groupe)
    RESEAU_SOCIAL.supprimer_avec_id_groupe(id_groupe)
    INTERPRETER.supprimer_avec_id_groupe(id_groupe)
    HEBERGER.supprimer_avec_id_groupe(id_groupe)
    FAVORI.supprimer_avec_id_groupe(id_groupe)
    FAIRE_PARTIE.supprimer_avec_id_groupe(id_groupe)
    EVENEMENT.supprimer_avec_id_groupe(id_groupe)
    GROUPE.supprimer_groupe(id_groupe)
    
def supprimer_un_artiste(id_artiste):
    """Supprime un groupe dans la base de donnée en prenant en compte toutes ses associations

    Args:
        id_spect (int): l'id du groupe à supprimer
    """
    JOUER.supprimer_avec_id_artiste(id_artiste)
    FAIRE_PARTIE.supprimer_avec_id_artiste(id_artiste)
    ARTISTE.supprimer_artiste(id_artiste)
    
def supprimer_un_evenement(id_evenement):
    """Supprime un evenement dans la base de donnée en prenant en compte toutes ses associations

    Args:
        id_spect (int): l'id de l'événement à supprimer
    """
    EVENEMENT.supprimer_evenement(id_evenement)

def ajouter_evenement(nom, description, heure_debut, duree, temps_montage, temps_demontage, id_lieu, id_journee, id_groupe):
    """
        Cette fonction permet d'appeler la fonction pour insérer un nouvel évènement.
    """
    prochain_id = EVENEMENT.get_prochain_id_evenement()
    insertion_passee_evenement = EVENEMENT.ajouter_evenement(prochain_id, nom, description, heure_debut, duree, temps_montage, temps_demontage, id_lieu, id_journee, id_groupe)
    return insertion_passee_evenement

def ajouter_groupe(nom, courte_description, longue_description, lien_image):
    """
        Cette fonction permet d'appeler la fonction pour insérer un nouveau groupe.
    """
    prochain_id = GROUPE.get_prochain_id_groupe()
    insertion_passee_groupe = GROUPE.ajouter_groupe(prochain_id, nom, courte_description, longue_description, lien_image)
    return insertion_passee_groupe

def ajouter_artiste(nom, courte_description, longue_description, lien_image):
    """
        Cette fonction permet d'appeler la fonction pour insérer un nouvel artiste.
    """
    prochain_id = ARTISTE.get_prochain_id_artiste()
    insertion_passee_artiste = ARTISTE.ajouter_artiste(prochain_id, nom, courte_description, longue_description, lien_image)
    return insertion_passee_artiste

def spectateur_est_connecte(spectateur_connecte):
    """
    Retourne si le spectateur est connecté sur le site


    Args:
        spectateur_connecte (Spectateur): le spectateur connecté (s'il n'est pas connecté l'id = -1)


    Returns:
        (bool): true si le spectateur est connecté, sinon false
    """
    return spectateur_connecte.get_id() != -1

def est_admin(spectateur_connecte):
    """
    Retourne si le spectateur est connecté sur le site


    Args:
        spectateur_connecte (Spectateur): le spectateur connecté (s'il n'est pas connecté l'id = -1)


    Returns:
        (bool): true si le spectateur est connecté, sinon false
    """
    return spectateur_connecte.get_admin() == "O"

def modifier_infos_spectateur(id_spectateur, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp):
    """
    Modifie les informations du spectateur


    Args:
        id_spectateur (int): l'id du spectateur
        nom (String): le nom du spectateur
        prenom (String): le prenom du spectateur
        mail (String): le mail du spectateur
        date_naissance (String): le date de naissance du spectateur
        tel (String): le telephone du spectateur
        nom_utilisateur (String): le nom utilisateur du spectateur
        mdp (String): le mot de passe du spectateur
    """
    SPECTATEUR.modifier_spectateur(id_spectateur, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp)
