class Acheter:
    def __init__(self, id_billet, id_spectateur, quantite_billet):
        self.__id_billet_achete = id_billet
        self.__id_spectateur_achete = id_spectateur
        self.__quantite_billet_achete = quantite_billet
    
    def get_id_billet(self):
        """Renvoie l'id du billet correspondant à l'achat

        Returns:
            int: l'id du billet
        """
        return self.__id_billet_achete
    
    def get_id_spectateur(self):
        """Renvoie l'id du spectateur correspondant à l'achat

        Returns:
            int: l'id du spectateur
        """
        return self.__id_spectateur_achete
    
    def get_quantite_billet(self):
        """Renvoie la quantité de billets correspondant à l'achat

        Returns:
            int: la quantité de billets
        """
        return self.__quantite_billet_achete

    def __str__(self):
        return f"id du billet : {self.__id_billet_achete}, id du spectateur détenant le billet : {self.__id_spectateur_achete}, quantite du billet : {self.__quantite_billet_achete}"
