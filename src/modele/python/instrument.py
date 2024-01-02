class Instrument:
    def __init__(self, id, nom):
        self.__id_i = id
        self.__nom_i = nom
    
    def get_id(self):
        return self.__id_i

    def get_nom(self):
        return self.__nom_i

    def set_nom(self, nouveau_nom):
        self.__nom_i = nouveau_nom
    
    def __str__(self):
        return f"id instrument : {self.__id_i}, le nom : {self.__nom_i}"
