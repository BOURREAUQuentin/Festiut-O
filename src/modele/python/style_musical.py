class StyleMusical:
    def __init__(self, id, nom, caracteristiques):
        self.__id_st = id
        self.__nom_st = nom
        self.__caracteristiques_st = caracteristiques
    
    def get_id(self):
        """Renvoie l'id du style musical

        Returns:
            id: l'id du style musical
        """
        return self.__id_st
    
    def get_nom_st(self):
        """Renvoie le nom du style musical

        Returns:
            String: le nom du style musical
        """
        return self.__nom_st

    def get_caracteristiques(self):
        """Renvoie les caractéristiques du style musical

        Returns:
            String: les caractéristiques du style muscical
        """
        return self.__caracteristiques_st
    
    def set_nom_st(self, nouveau_nom):
        """Redéfini le nom dy style musical

        Args:
            nouveau_nom (String): le nouveau nom du style musical
        """
        self.__nom_st = nouveau_nom
    
    def set_caracteristiques(self, nouvelles_caracteristiques):
        """Redéfini les caractéristiques du style musical

        Args:
            nouvelles_caracteristiques (String): les nouvelles caractéristiques du style musical
        """
        self.__caracteristiques_st = nouvelles_caracteristiques
    
    def __str__(self):
        return f"id style musical : {self.__id_st}, le nom : {self.__nom_st}, les caracteristiques : {self.__caracteristiques_st}"
