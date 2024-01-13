class ASousStyle:
    def __init__(self, id_style_principal, id_sous_style):
        self.__id_style_principal_a = id_style_principal
        self.__id_sous_style_a = id_sous_style
    
    def get_id_style_principal(self):
        """Renvoie l'id du style principal

        Returns:
            int: l'id du style
        """
        return self.__id_style_principal_a

    def get_id_sous_style(self):
        """Renvoie l'id du sous style

        Returns:
            int: l'id du sous style
        """
        return self.__id_sous_style_a

    def __str__(self):
        return f"id du style musical principal : {self.__id_style_principal_a}, l'id du sous style musical associé : {self.__id_sous_style_a}"
