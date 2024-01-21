class Billet:
    def __init__(self, id, prix):
        self.__id_b = id
        self.__prix_b = prix
    
    def get_id(self):
        """Récupère l'id du billet

        Returns:
            int: l'id du billet
        """
        return self.__id_b

    def get_prix(self):
        """Récupère le prix du billet

        Returns:
            int: le prix du billet
        """
        return self.__prix_b
    
    def __str__(self):
        return f"id du billet : {self.__id_b}, le prix : {self.__prix_b}"
