class ReseauVideo:
    def __init__(self, id, nom, lien, id_groupe):
        self.__id_rv = id
        self.__nom_rv = nom
        self.__lien_rv = lien
        self.__id_groupe_rv = id_groupe
    
    def get_id(self):
        """Renvoie l'id du réseau vidéo

        Returns:
            int: _l'id du réseau vidéo
        """
        return self.__id_rv
    
    def get_nom(self):
        """Renvoie le nom du réseau vidéo

        Returns:
            String: le nom du réseau vidéo
        """
        return self.__nom_rv
    
    def get_lien(self):
        """Renvoie le lien du réseau vidéo

        Returns:
            String: le lien du réseau vidéo
        """
        return self.__lien_rv
    
    def get_id_groupe(self):
        """Renvoie l'id du groupe associé

        Returns:
            int: l'id du groupe
        """
        return self.__id_groupe_rv
    
    def set_nom(self, nouveau_nom):
        """Redéfini le nom du réseau vidéo

        Args:
            nouveau_nom (String): le nouveau nom du réseau vidéo
        """
        self.__nom_rv = nouveau_nom
    
    def set_lien(self, nouveau_lien):
        """Redéfini le lien du réseau vidéo

        Args:
            nouveau_lien (String): le nouveau lien du réseau vidéo
        """
        self.__lien_rv = nouveau_lien

    def __str__(self):
        return f"id du réseau vidéo : {self.__id_rv}, le nom du réseau vidéo : {self.__nom_rv}, le lien du réseau vidéo : {self.__lien_rv}, l'id du groupe associé au lien : {self.__id_groupe_rv}"
