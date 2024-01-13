class Journee:
    def __init__(self, id, date):
        self.__id_j = id
        self.__date_j = date
    
    def get_id(self):
        """Renvoie l'id de la journée

        Returns:
            int: _l'id de la journee
        """
        return self.__id_j
    
    def get_date(self):
        """Renvoie la date de la journée

        Returns:
            DateTime: la date de la journée
        """
        return self.__date_j
    
    def set_date(self, nouvelle_date):
        """redéfini la date de la journée

        Returns:
            DateTime: la nouvelle date de la journée
        """
        self.__date_j = nouvelle_date
    
    def __str__(self):
        return f"id journee : {self.__id_j}, la date : {self.__date_j}"
