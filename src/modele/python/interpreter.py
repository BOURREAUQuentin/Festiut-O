class Interpreter:
    def __init__(self, id_groupe, id_style_musical):
        self.__id_groupe_i = id_groupe
        self.__id_style_musical_i = id_style_musical
    
    def get_id_groupe(self):
        """Renvoie le nom du groupe

        Returns:
            int: l'id du groupe
        """
        return self.__id_groupe_i
    
    def get_id_style_musical(self):
        """Renvoie l'id du style musical

        Returns:
            int: l'id du style musical
        """
        return self.__id_style_musical_i

    def __str__(self):
        return f"id du groupe : {self.__id_groupe_i}, id du style musical du groupe : {self.__id_style_musical_i}"
