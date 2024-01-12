class Panier:
    def __init__(self, id_billet, id_spectateur, quantite_billet):
        self.__id_billet_panier = id_billet
        self.__id_spectateur_panier = id_spectateur
        self.__quantite_billet_panier = quantite_billet
    
    def get_id_billet(self):
        return self.__id_billet_panier
    
    def get_id_spectateur(self):
        return self.__id_spectateur_panier

    def get_quantite_billet(self):
        return self.__quantite_billet_panier
    
    def set_quantite_billet(self, nouvelle_quantite_billet):
        self.__quantite_billet_panier = nouvelle_quantite_billet

    def __str__(self):
        return f"id du billet : {self.__id_billet_panier}, id du spectateur ayant le billet dans son panier : {self.__id_spectateur_panier}, quantite du billet : {self.__quantite_billet_panier}"
