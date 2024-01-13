class Artiste:
    def __init__(self, id, nom, description, lien_image):
        self.__id_a = id
        self.__nom_a = nom
        self.__description_a = description
        self.__lien_image_a = lien_image

    def get_id(self):
        """Renvoie l'id de l'artiste

        Returns:
            int: l'id de l'artiste
        """
        return self.__id_a

    def get_nom(self):
        """Renvoie le nom de l'artiste

        Returns:
            String: Le nom de l'artiste
        """
        return self.__nom_a

    def get_description(self):
        """Renvoie la description de l'artiste

        Returns:
            String: La description de l'artiste
        """
        return self.__description_a
    
    def get_lien_image(self):
        """Renvoie le lien de l'image de l'artiste

        Returns:
            String : le lien de l'image de l'artiste
        """
        return self.__lien_image_a
    
    def set_nom(self, nouveau_nom):
        """Permet de redéfinir le nom de l'artiste

        Args:
            nouveau_nom (String): le nouveau nom de l'artiste
        """
        self.__id_a = nouveau_nom

    def set_description(self, nouvelle_description):
        """Permet de redéfinir la description de l'artiste

        Args:
            nouvelle_description (String): la nouvelle description de l'artiste
        """
        self.__description_a = nouvelle_description
    
    def set_lien_image(self, nouveau_lien_image):
        """Permet de redéfinir le lien de l'image de l'artiste

        Args:
            nouveau_lien_image(String): le nouveau lien de l'image de l'artiste
        """
        self.__lien_image_a = nouveau_lien_image

    def __str__(self):
        return f"id artiste : {self.__id_a}, le nom : {self.__nom_a}, la description : {self.__description_a}, le lien de l'image : {self.__lien_image_a}"
