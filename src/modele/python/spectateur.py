class Spectateur:
    def __init__(self, id, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp, admin):
        self.__id_s = id
        self.__nom_s = nom
        self.__prenom_s = prenom
        self.__mail_s = mail
        self.__date_naissance_s = date_naissance
        self.__tel_s = tel
        self.__nom_utilisateur_s = nom_utilisateur
        self.__mdp_s = mdp
        self.__admin_s = admin

    def get_id(self):
        return self.__id_s

    def get_nom(self):
        return self.__nom_s

    def get_prenom(self):
        return self.__prenom_s

    def get_mail(self):
        return self.__mail_s

    def get_date_naissance(self):
        return self.__date_naissance_s

    def get_telephone(self):
        return self.__tel_s

    def get_nom_utilisateur(self):
        return self.__nom_utilisateur_s

    def get_mdp(self):
        return self.__mdp_s

    def get_admin(self):
        return self.__admin_s

    def set_nom(self, nouveau_nom):
        self.__nom_s = nouveau_nom

    def set_prenom(self, nouveau_prenom):
        self.__prenom_s = nouveau_prenom

    def set_mail(self, nouveau_mail):
        self.__mail_s = nouveau_mail
    
    def set_telephone(self, nouveau_tel):
        self.__tel_s = nouveau_tel
    
    def set_nom_utilisateur(self, nouveau_nom_utilisateur):
        self.__nom_utilisateur_s = nouveau_nom_utilisateur
    
    def set_mdp(self, nouveau_mdp):
        self.__mdp_s = nouveau_mdp
    
    def __str__(self):
        return f"id spectateur : {self.__id_s}, le nom : {self.__nom_s}, le prenom : {self.__prenom_s}, le nom utilisateur : {self.__nom_utilisateur_s}"
