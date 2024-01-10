class Groupe:
    def __init__(self, id, nom, description, lien_image):
        self.__id_g = id
        self.__nom_g = nom
        self.__description_g = description
        self.__lien_image_g = lien_image

    def get_id(self):
        return self.__id_g

    def get_nom(self):
        return self.__nom_g

    def get_description(self):
        return self.__description_g
    
    def get_lien_image(self):
        return self.__lien_image_g

    def set_nom(self, nouveau_nom):
        self.__nom_g = nouveau_nom
    
    def set_description(self, nouvelle_description):
        self.__description_g = nouvelle_description

    def __str__(self):
        return f"id groupe : {self.__id_g}, le nom : {self.__nom_g}, la description : {self.__description_g}, le lien de l'image : {self.__lien_image_g}"
