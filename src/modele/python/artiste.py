class Artiste:
    def __init__(self, id, nom, description, lien_image):
        self.__id_a = id
        self.__nom_a = nom
        self.__description_a = description
        self.__lien_image_a = lien_image

    def get_id(self):
        return self.__id_a

    def get_nom(self):
        return self.__nom_a

    def get_description(self):
        return self.__description_a
    
    def get_lien_image(self):
        return self.__lien_image_a
    
    def set_nom(self, nouveau_nom):
        self.__id_a = nouveau_nom

    def set_description(self, nouvelle_description):
        self.__description_a = nouvelle_description
    
    def set_lien_image(self, nouveau_lien_image):
        self.__lien_image_a = nouveau_lien_image

    def __str__(self):
        return f"id artiste : {self.__id_a}, le nom : {self.__nom_a}, la description : {self.__description_a}, le lien de l'image : {self.__lien_image_a}"
