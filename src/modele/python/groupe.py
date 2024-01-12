class Groupe:
    def __init__(self, id, nom, courte_description, longue_description, lien_image):
        self.__id_g = id
        self.__nom_g = nom
        self.__courte_description_g = courte_description
        self.__longue_description_g = longue_description
        self.__lien_image_g = lien_image

    def get_id(self):
        return self.__id_g

    def get_nom(self):
        return self.__nom_g

    def get_courte_description(self):
        return self.__courte_description_g
    
    def get_longue_description(self):
        return self.__longue_description_g
    
    def get_lien_image(self):
        return self.__lien_image_g

    def set_nom(self, nouveau_nom):
        self.__nom_g = nouveau_nom
    
    def set_courte_description(self, nouvelle_courte_description):
        self.__courte_description_g = nouvelle_courte_description

    def set_longue_description(self, nouvelle_longue_description):
        self.__longue_description_g = nouvelle_longue_description

    def __str__(self):
        return f"id groupe : {self.__id_g}, le nom : {self.__nom_g}, la description courte : {self.__courte_description_g}, le lien de l'image : {self.__lien_image_g}"
