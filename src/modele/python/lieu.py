class Lieu:
    def __init__(self, id, nom, adresse, nb_max_spect):
        self.__id_l = id
        self.__nom_l = nom
        self.__adresse_l = adresse
        self.__nb_max_spect_l = nb_max_spect
    
    def get_id(self):
        """Renvoie l'id du lieu

        Returns:
            int: l'id du lieu
        """
        return self.__id_l
    
    def get_nom(self):
        """Renvoie le nom du lieu

        Returns:
            String: le nom du lieu
        """
        return self.__nom_l

    def get_adresse(self):
        """Renvoie l'adresse du lieu

        Returns:
            DateTime: l'adresse du lieu
        """
        return self.__adresse_l

    def get_nb_max_spect(self):
        """Renvoie le nb max de spectateurs du lieu

        Returns:
            int: le nb de spectateurs max du lieu
        """
        return self.__nb_max_spect_l
    
    def set_nom(self, nouveau_nom):
        """Redéfini le nom du lieu

        Args:
            nouveau_nom (String): le nouveau nom du lieu
        """
        self.__nom_l = nouveau_nom
    
    def set_adresse(self, nouvelle_adresse):
        """Redéfini l'adresse du lieu

        Args:
            nouvelle_adresse (String): la nouvelle adresse du lieu
        """
        self.__adresse_l = nouvelle_adresse
    
    def set_nb_max_spect(self, nouveau_nb_max_spect):
        """Redéfini le nombre max du lieu

        Args:
            nouveau_nb_max_spect (int): le nouveau nombre de spect max
        """
        self.__nb_max_spect_l = nouveau_nb_max_spect
    
    def __str__(self):
        return f"id lieu : {self.__id_l}, le nom : {self.__nom_l}, l'adresse : {self.__adresse_l}, le nombre maximum de spectateurs : {self.__nb_max_spect_l}"
