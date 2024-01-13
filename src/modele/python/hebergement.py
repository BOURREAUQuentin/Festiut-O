class Hebergement:
    def __init__(self, id, nom, adresse, nb_places_max):
        self.__id_h = id
        self.__nom_h = nom
        self.__adresse_h = adresse
        self.__nb_places_max_h = nb_places_max
    
    def get_id(self):
        """Renvoie l'id de l'hebergement

        Returns:
            int: l'id de l'hébergement
        """
        return self.__id_h
    
    def get_nom(self):
        """Renvoie le nom de l'hébergement

        Returns:
            String: le nom de l'hébergement
        """
        return self.__nom_h
    
    def get_adresse(self):
        """Renvoie l'adresse de l'hébergement

        Returns:
            String: l'adresse de l'hébergement
        """
        return self.__adresse_h
    
    def get_nb_places_max(self):
        """Renvoie le nb de places max de l'hébergement

        Returns:
            int: le nb de places max de l'hébergement
        """
        return self.__nb_places_max_h
    
    def set_nom(self, nouveau_nom):
        """Permet de redéfinir le nom de l'hébergement

        Args:
            nouveau_nom (String): le nouveau nom de l'hébergement
        """
        self.__nom_h = nouveau_nom
    
    def __str__(self):
        return f"id hébergement : {self.__id_h}, le nom : {self.__nom_h}, l'adresse : {self.__adresse_h}, le nombre de places maximum : {self.__nb_places_max_h}"
