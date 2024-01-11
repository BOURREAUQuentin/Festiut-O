class Acheter:
    def __init__(self, id_billet, id_spectateur, quantite_billet):
        self.__id_billet_achete = id_billet
        self.__id_spectateur_achete = id_spectateur
        self.__quantite_billet_achete = quantite_billet
    
    def get_id_billet(self):
        return self.__id_billet_achete
    
    def get_id_spectateur(self):
        return self.__id_spectateur_achete
    
    def get_quantite_billet(self):
        return self.__quantite_billet_achete
    
    def set_quantite_billet(self, nouvelle_quantite_billet):
        self.__quantite_billet_achete = nouvelle_quantite_billet

    def __str__(self):
        return f"id du billet : {self.__id_billet_achete}, id du spectateur détenant le billet : {self.__id_spectateur_achete}, quantite du billet : {self.__quantite_billet_achete}"
