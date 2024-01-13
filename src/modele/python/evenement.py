class Evenement:
    def __init__(self, id_evenement, nom, description, heure_debut, duree, tps_montage, tps_demontage, id_lieu, id_journee, id_groupe):
        self.__id_e = id_evenement
        self.__nom_e = nom
        self.__description_e = description
        self.__heure_debut_e = heure_debut
        self.__duree_e = duree
        self.__tps_montage_e = tps_montage
        self.__tps_demontage_e = tps_demontage
        self.__id_lieu_e = id_lieu
        self.__id_journee_e = id_journee
        self.__id_groupe_e = id_groupe
    
    def get_id(self):
        """Renvoie l'id de l'évenement

        Returns:
            int: l'id de l'évenement
        """
        return self.__id_e
    
    def get_nom(self):
        """Renvoie le nom de l'évenement

        Returns:
            String: le nom de l'évenement
        """
        return self.__nom_e
    
    def get_description(self):
        """Renvoie la description de l'évenement

        Returns:
            String: La description de l'évenement
        """
        return self.__description_e
    
    def get_heure_debut(self):
        """Renvoie l'heure de début de l'événement

        Returns:
            DateTime: L'heure de début de l'événement
        """
        return self.__heure_debut_e
    
    def get_duree(self):
        """Renvoie la durée de l'événemment

        Returns:
            DateTime: La durée de l'événement
        """
        return self.__duree_e
    
    def get_tps_montage(self):
        """Renvoie le temps de montage de lévénement

        Returns:
            DateTime: la duree de montage de l'événement
        """
        return self.__tps_montage_e
    
    def get_tps_demontage(self):
        """Renvoie le temps de démontage de l'événement

        Returns:
            DateTime: la duree de démontage de l'événement
        """
        return self.__tps_demontage_e
    
    def get_id_lieu(self):
        """Renvoie l'id du lieu de l'événement

        Returns:
            int: l'id de l'événement où a lieu l'événement
        """
        return self.__id_lieu_e
    
    def get_id_journee(self):
        """Renvoie l'id de la journée de l'événement

        Returns:
            int: l'id de la journée pendant laquelle a lieu l'événement
        """
        return self.__id_journee_e
    
    def get_id_groupe(self):
        """Renvoie de l'id du groupe qui performe durant l'événement

        Returns:
            int: l'id du groupe
        """
        return self.__id_groupe_e
    
    def set_nom(self, nouveau_nom):
        """Permet de redéfinir le nom de l'événement

        Args:
            nouveau_nom (String): le nouveau nom
        """
        self.__nom_e = nouveau_nom
    
    def set_description(self, nouvelle_description):
        """Permet de redéfinir la déscription de l'événement

        Args:
            nouveau_description (String): la nouvelle description
        """
        self.__description_e = nouvelle_description
    
    def set_heure_debut(self, nouvelle_heure_debut):
        """Permet de redéfinir l'heure de début de l'événement

        Args:
            nouvelle_heure_debut (DateTime): la nouvelle heure de début
        """
        self.__heure_debut_e = nouvelle_heure_debut
    
    def set_duree(self, nouvelle_duree):
        """Permet de définir la nouvelle durée de l'événement

        Args:
            nouvelle_duree (DateTime): La nouvelle durée de l'événement
        """
        self.__duree_e = nouvelle_duree
    
    def set_tps_montage(self, nouveau_tps_montage):
        """Permet de redéfinir le temps de montage de l'événement

        Args:
            nouveau_tps_montage (DateTime): le nouveau temps de montage de l'événement
        """
        self.__tps_montage_e = nouveau_tps_montage
    
    def set_tps_demontage(self, nouveau_tps_demontage):
        """Permet de redéfinir le temps de démontage de l'événeùment

        Args:
            nouveau_tps_demontage (DateTime): Le nouveau temps de demontage de l'événement
        """
        self.__tps_demontage_e = nouveau_tps_demontage

    def __str__(self):
        return f"id evenement : {self.__id_e}, le nom : {self.__nom_e}, la description : {self.__description_e}, l'heure de début : {self.__heure_debut_e}, la durée : {self.__duree_e}"
