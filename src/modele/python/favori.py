class Favori:
    def __init__(self, id_spectateur, id_groupe):
        self.__id_spectateur_f = id_spectateur
        self.__id_groupe_f = id_groupe
    
    def get_id_spectateur(self):
        """Renvoie d'id du spectateur

        Returns:
            int: id du spectateur
        """
        return self.__id_spectateur_f
    
    def get_id_groupe(self):
        """Renvoie l'id du groupe

        Returns:
            int l'id du groupe
        """
        return self.__id_groupe_f
    
    def __str__(self):
        return f"id du spectateur : {self.__id_spectateur_f}, id du groupe en favori : {self.__id_groupe_f}"
