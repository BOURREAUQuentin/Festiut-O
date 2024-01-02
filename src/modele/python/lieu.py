class Lieu:
    def __init__(self, id, nom, adresse, nb_max_spect):
        self.__id_l = id
        self.__nom_l = nom
        self.__adresse_l = adresse
        self.__nb_max_spect_l = nb_max_spect
    
    def get_id(self):
        return self.__id_l
    
    def get_nom(self):
        return self.__nom_l

    def get_adresse(self):
        return self.__adresse_l

    def get_nb_max_spect(self):
        return self.__nb_max_spect_l
    
    def set_nom(self, nouveau_nom):
        self.__nom_l = nouveau_nom
    
    def set_adresse(self, nouvelle_adresse):
        self.__adresse_l = nouvelle_adresse
    
    def set_nb_max_spect(self, nouveau_nb_max_spect):
        self.__nb_max_spect_l = nouveau_nb_max_spect
    
    def __str__(self):
        return f"id lieu : {self.__id_l}, le nom : {self.__nom_l}, l'adresse : {self.__adresse_l}, le nombre maximum de spectateurs : {self.__nb_max_spect_l}"
