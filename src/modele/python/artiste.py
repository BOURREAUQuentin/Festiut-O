class Artiste:
    def __init__(self, id, nom, courte_description, longue_description, lien_image):
        self.__id_a = id
        self.__nom_a = nom
        self.__courte_description_a = courte_description
        self.__longue_description_a = longue_description
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

    def get_courte_description(self):
        """Renvoie la courte description de l'artiste

        Returns:
            String: La courte description de l'artiste
        """
        return self.__courte_description_a
    
    def get_longue_description(self):
        """Renvoie la longue description de l'artiste

        Returns:
            String: La longue description de l'artiste
        """
        return self.__longue_description_a
    
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

    def set_courte_description(self, nouvelle_courte_description):
        """Permet de redéfinir la courte description de l'artiste

        Args:
            nouvelle_description (String): la nouvelle courte description de l'artiste
        """
        self.__courte_description_a = nouvelle_courte_description
    
    def set_longue_description(self, nouvelle_longue_description):
        """Permet de redéfinir la longue description de l'artiste

        Args:
            nouvelle_description (String): la nouvelle longue description de l'artiste
        """
        self.__longue_description_a = nouvelle_longue_description
    
    def set_lien_image(self, nouveau_lien_image):
        """Permet de redéfinir le lien de l'image de l'artiste

        Args:
            nouveau_lien_image(String): le nouveau lien de l'image de l'artiste
        """
        self.__lien_image_a = nouveau_lien_image

    def __str__(self):
        return f"id artiste : {self.__id_a}, le nom : {self.__nom_a}, la courte description : {self.__courte_description_a}, le lien de l'image : {self.__lien_image_a}"
