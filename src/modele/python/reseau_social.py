class ReseauSocial:
    def __init__(self, id, nom, lien, id_groupe):
        self.__id_rs = id
        self.__nom_rs = nom
        self.__lien_rs = lien
        self.__id_groupe_rs = id_groupe
    
    def get_id(self):
        """Renvoie l'id du réseau social

        Returns:
            int: l'id du réseau social
        """
        return self.__id_rs
    
    def get_nom(self):
        """Renvoie le nom du réseau social

        Returns:
            String: le nom du réseau social
        """
        return self.__nom_rs
    
    def get_lien(self):
        """Renvoie le lien du réseau social

        Returns:
            String: renvoie le lien du réseau social
        """
        return self.__lien_rs
    
    def get_id_groupe(self):
        """Renvoie l'id du groupe qui a le réseau social

        Returns:
            int: l'id du groupe qui a le réseau social
        """
        return self.__id_groupe_rs
    
    def set_nom(self, nouveau_nom):
        """Redéfini le nom du réseau social

        Args:
            nouveau_nom (String): le nouveau nom du réseau social
        """
        self.__nom_rs = nouveau_nom
    
    def set_lien(self, nouveau_lien):
        """Redéfini le lien du réseau social

        Args:
            nouveau_lien (String): le nouveau lien du réseau social
        """
        self.__lien_rs = nouveau_lien

    def __str__(self):
        return f"id du réseau social : {self.__id_rs}, le nom du réseau social : {self.__nom_rs}, le lien du réseau social : {self.__lien_rs}, l'id du groupe associé au lien : {self.__id_groupe_rs}"
