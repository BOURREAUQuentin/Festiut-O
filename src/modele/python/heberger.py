class Heberger:
    def __init__(self, id_hebergement, id_groupe):
        self.__id_hebergement_h = id_hebergement
        self.__id_groupe_h = id_groupe
    
    def get_id_hebergement(self):
        return self.__id_hebergement_h
    
    def get_id_groupe(self):
        return self.__id_groupe_h
    
    def __str__(self):
        return f"id de l'hébergement : {self.__id_hebergement_h}, id du groupe dans l'hébergement : {self.__id_groupe_h}"
