class Acheter:
    def __init__(self, id_billet, id_spectateur):
        self.__id_billet_achete = id_billet
        self.__id_spectateur_achete = id_spectateur
    
    def get_id_billet(self):
        return self.__id_billet_achete
    
    def get_id_spectateur(self):
        return self.__id_spectateur_achete

    def __str__(self):
        return f"id du billet : {self.__id_billet_achete}, id du spectateur détenant le billet : {self.__id_spectateur_achete}"
