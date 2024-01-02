class Hebergement:
    def __init__(self, id, nom, adresse, nb_places_max):
        self.__id_h = id
        self.__nom_h = nom
        self.__adresse_h = adresse
        self.__nb_places_max_h = nb_places_max
    
    def get_id(self):
        return self.__id_h
    
    def get_nom(self):
        return self.__nom_h
    
    def get_adresse(self):
        return self.__adresse_h
    
    def get_nb_places_max(self):
        return self.__nb_places_max_h
    
    def set_nom(self, nouveau_nom):
        self.__nom_h = nouveau_nom
    
    def __str__(self):
        return f"id hébergement : {self.__id_h}, le nom : {self.__nom_h}, l'adresse : {self.__adresse_h}, le nombre de places maximum : {self.__nb_places_max_h}"
