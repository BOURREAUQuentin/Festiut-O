class StyleMusical:
    def __init__(self, id, nom, caracteristiques):
        self.__id_st = id
        self.__nom_st = nom
        self.__caracteristiques_st = caracteristiques
    
    def get_id(self):
        return self.__id_st
    
    def get_nom_st(self):
        return self.__nom_st

    def get_caracteristiques(self):
        return self.__caracteristiques_st
    
    def set_nom_st(self, nouveau_nom):
        self.__nom_st = nouveau_nom
    
    def set_caracteristiques(self, nouvelles_caracteristiques):
        self.__caracteristiques_st = nouvelles_caracteristiques
    
    def __str__(self):
        return f"id style musical : {self.__id_st}, le nom : {self.__nom_st}, les caracteristiques : {self.__caracteristiques_st}"
