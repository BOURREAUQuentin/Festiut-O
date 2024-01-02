class Spectateur:
    def __init__(self, id, nom, prenom, mail, dateNaiss, tel, nomUtilisateur, mdp, admin):
        self.__idS = id
        self.__nomS = nom
        self.__prenomS = prenom
        self.__mailS = mail
        self.__dateNaissS = dateNaiss
        self.__telS = tel
        self.__nomUtilisateurS = nomUtilisateur
        self.__mdpS = mdp
        self.__adminS = admin

    def get_id(self):
        return self.__idS

    def get_nom(self):
        return self.__nomS



    def __str__(self):
        return f"id artiste : {self.__idA}, le nom : {self.__nomA}, la description : {self.__descriptionA}"
