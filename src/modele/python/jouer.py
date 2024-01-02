class Jouer:
    def __init__(self, id_artiste, id_instrument):
        self.__id_artiste_j = id_artiste
        self.__id_instrument_j = id_instrument

    def get_id_artiste(self):
        return self.__id_artiste_j
    
    def get_id_instrument(self):
        return self.__id_instrument_j

    def __str__(self):
        return f"id de l'artiste : {self.__id_artiste_j}, id de l'instrument joué par l'artiste : {self.__id_instrument_j}"
