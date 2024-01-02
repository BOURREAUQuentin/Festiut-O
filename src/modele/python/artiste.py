class Artiste:
    def __init__(self, id, nom, age, description):
        self.__idA = id
        self.__nomA = nom
        self.__descriptionA = description

    def get_id(self):
        return self.__idA

    def get_nom(self):
        return self.__nomA

    def get_description(self):
        return self.__descriptionA
    
    def set_nom(self, nouveau_nom):
        self.__idA = nouveau_nom

    def set_description(self, nouvelle_description):
        self.__descriptionA = nouvelle_description

    def __str__(self):
        return f"id artiste : {self.__idA}, le nom : {self.__nomA}, la description : {self.__descriptionA}"
