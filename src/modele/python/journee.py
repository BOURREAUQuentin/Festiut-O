class Journee:
    def __init__(self, id, date):
        self.__id_j = id
        self.__date_j = date
    
    def get_id(self):
        return self.__id_j
    
    def get_date(self):
        return self.__date_j
    
    def set_date(self, nouvelle_date):
        self.__date_j = nouvelle_date
    
    def __str__(self):
        return f"id journee : {self.__id_j}, la date : {self.__date_j}"
