class ReseauVideo:
    def __init__(self, id, nom, lien, id_groupe):
        self.__id_rv = id
        self.__nom_rv = nom
        self.__lien_rv = lien
        self.__id_groupe_rv = id_groupe
    
    def get_id(self):
        return self.__id_rv
    
    def get_nom(self):
        return self.__nom_rv
    
    def get_lien(self):
        return self.__lien_rv
    
    def get_id_groupe(self):
        return self.__id_groupe_rv
    
    def set_nom(self, nouveau_nom):
        self.__nom_rv = nouveau_nom
    
    def set_lien(self, nouveau_lien):
        self.__lien_rv = nouveau_lien

    def __str__(self):
        return f"id du réseau vidéo : {self.__id_rv}, le nom du réseau vidéo : {self.__nom_rv}, le lien du réseau vidéo : {self.__lien_rv}, l'id du groupe associé au lien : {self.__id_groupe_rv}"
