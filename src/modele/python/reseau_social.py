class ReseauSocial:
    def __init__(self, id, nom, lien, id_groupe):
        self.__id_rs = id
        self.__nom_rs = nom
        self.__lien_rs = lien
        self.__id_groupe_rs = id_groupe
    
    def get_id(self):
        return self.__id_rs
    
    def get_nom(self):
        return self.__nom_rs
    
    def get_lien(self):
        return self.__lien_rs
    
    def get_id_groupe(self):
        return self.__id_groupe_rs
    
    def set_nom(self, nouveau_nom):
        self.__nom_rs = nouveau_nom
    
    def set_lien(self, nouveau_lien):
        self.__lien_rs = nouveau_lien

    def __str__(self):
        return f"id du réseau social : {self.__id_rs}, le nom du réseau social : {self.__nom_rs}, le lien du réseau social : {self.__lien_rs}, l'id du groupe associé au lien : {self.__id_groupe_rs}"
