class Acceder:
    def __init__(self, id_billet, id_journee):
        self.__id_billet_a = id_billet
        self.__id_journee_a = id_journee
    
    def get_id_billet(self):
        """Renvoie l'id du billet

        Returns:
            int: l'id du billet
        """
        return self.__id_billet_a
    
    def get_id_journee(self):
        """Renvoie l'id de la journée correspondant à l'accès

        Returns:
            int: l'id de la journée
        """
        return self.__id_journee_a
    
    def __str__(self):
        return f"id du billet : {self.__id_billet_a}, l'id de la journée possible avec le billet : {self.__id_journee_a}"
