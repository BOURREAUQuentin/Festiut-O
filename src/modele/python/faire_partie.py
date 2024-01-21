class FairePartie:
    def __init__(self, id_groupe, id_artiste):
        self.__id_groupe_fp = id_groupe
        self.__id_artiste_fp = id_artiste
    
    def get_id_groupe(self):
        """Renvoie l'id du groupe

        Returns:
            int: l'id du groupe
        """
        return self.__id_groupe_fp
    
    def get_id_artiste(self):
        """Renvoie l'id de l'artiste qui fait parti du groupe

        Returns:
            int: l'id de l'artiste
        """
        return self.__id_artiste_fp

    def __str__(self):
        return f"id du groupe : {self.__id_groupe_fp}, id de l'artiste dans le groupe : {self.__id_artiste_fp}"
