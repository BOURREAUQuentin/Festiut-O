class Instrument:
    def __init__(self, id, nom):
        self.__id_i = id
        self.__nom_i = nom
    
    def get_id(self):
        """Renvoie l'id de l'instrument

        Returns:
            int: l'id de l'instrument
        """
        return self.__id_i

    def get_nom(self):
        """Renvoie nom de l'instrument

        Returns:
            String: le nom de l'instrument
        """
        return self.__nom_i

    def set_nom(self, nouveau_nom):
        """Permet de redéfinir le nom de l'instrument

        Args:
            nouveau_nom (String): le nouveau nom de l'instrument
        """
        self.__nom_i = nouveau_nom
    
    def __str__(self):
        return f"id instrument : {self.__id_i}, le nom : {self.__nom_i}"
