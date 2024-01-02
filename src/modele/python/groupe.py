class Groupe:
    def __init__(self, id, nom, description):
        self.__id_g = id
        self.__nom_g = nom
        self.__description_g = description

    def get_id(self):
        return self.__id_g

    def get_nom(self):
        return self.__nom_g

    def get_description(self):
        return self.__description_g

    def set_nom(self, nouveau_nom):
        self.__nom_g = nouveau_nom
    
    def set_description(self, nouvelle_description):
        self.__description_g = nouvelle_description

    def __str__(self):
        return f"id groupe : {self.__id_g}, le nom : {self.__nom_g}, la description : {self.__description_g}"
