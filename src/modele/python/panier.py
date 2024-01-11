class Panier:
    def __init__(self, id_billet, id_spectateur):
        self.__id_billet_panier = id_billet
        self.__id_spectateur_panier = id_spectateur
    
    def get_id_billet(self):
        return self.__id_billet_panier
    
    def get_id_spectateur(self):
        return self.__id_spectateur_panier

    def __str__(self):
        return f"id du billet : {self.__id_billet_panier}, id du spectateur ayant le billet dans son panier : {self.__id_spectateur_panier}"
