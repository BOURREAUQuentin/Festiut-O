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
        """Renvoie l'id du spectateur

        Returns:
            int: l'id du spectateur
        """
        return self.__id_s

    def get_nom(self):
        """Renvoie le nom du spectateur

        Returns:
            String: le nom du spectateur
        """
        return self.__nom_s

    def get_prenom(self):
        """Renvoie le prenom du spectateur

        Returns:
            String: le prenom du spectateur
        """
        return self.__prenom_s

    def get_mail(self):
        """Renvoie le mail du spectateur

        Returns:
            String: le mail du spectateur
        """
        return self.__mail_s

    def get_date_naissance(self):
        """Renvoie la date de naissance du spectateur

        Returns:
            String: la date de naissance du spectateur
        """
        return self.__date_naissance_s

    def get_telephone(self):
        """Renvoie le numéro de téléphone du spectateur

        Returns:
            String: le numéro de téléphone du spectateur
        """
        return self.__tel_s

    def get_nom_utilisateur(self):
        """Renvoie le nom_utilisateur du spectateur

        Returns:
            String: le nom-utilisateur du spectateur
        """
        return self.__nom_utilisateur_s

    def get_mdp(self):
        """Renvoie le mot de passe du spectateur

        Returns:
            String: le mot de passe du spectateur
        """
        return self.__mdp_s

    def get_admin(self):
        """Renvoie l'état admin du spectateur

        Returns:
            bool: si le spectateur est un spectateur
        """
        return self.__admin_s

    def set_nom(self, nouveau_nom):
        """Redéfini le nom du spectateur

        Args:
            nouveau_nom (String): le nouveau nom du spectateur
        """
        self.__nom_s = nouveau_nom

    def set_prenom(self, nouveau_prenom):
        """Redéfini le prenom du spectateur

        Args:
            nouveau_prenom (String): le nouveau prenom du spectateur
        """
        self.__prenom_s = nouveau_prenom

    def set_mail(self, nouveau_mail):
        """Redéfini le mail du spectateur

        Args:
            nouveau_mail (String): le nouveau mail du spectateur
        """
        self.__mail_s = nouveau_mail
    
    def set_telephone(self, nouveau_tel):
        """Redéfini le telephone du spectateur

        Args:
            nouveau_telephone (String): le nouveau telephone du spectateur
        """
        self.__tel_s = nouveau_tel
    
    def set_nom_utilisateur(self, nouveau_nom_utilisateur):
        """Redéfini le nom utilisateur du spectateur

        Args:
            nouveau_nom_utilisateur (String): le nouveau nom utilisateur du spectateur
        """
        self.__nom_utilisateur_s = nouveau_nom_utilisateur
    
    def set_mdp(self, nouveau_mdp):
        """Redéfini le mot de passe du spectateur

        Args:
            nouveau_nom (String): le nouveau mot de passe du spectateur
        """
        self.__mdp_s = nouveau_mdp

    def set_all(self, id, nom, prenom, mail, date_naissance, tel, nom_utilisateur, mdp, admin):
        """Redéfini tous les attributs de spectateur

        Args:
            id (int): l'id du spectateur
            nom (String): : le nom du spectateur
            prenom (String): : le prenom du spectateur
            mail (String): : le mail spectateur
            date_naissance (String): : la date de naissance du spectateur
            tel (String): : le telephone du spectateur
            nom_utilisateur (String): : le nom utilisateur du spectateur
            mdp (String): : le mot de passe du spectateur
            admin (bool): : l'etat admin du spectateur
        """
        self.__id_s = id
        self.__nom_s = nom
        self.__prenom_s = prenom
        self.__mail_s = mail
        self.__date_naissance_s = date_naissance
        self.__tel_s = tel
        self.__nom_utilisateur_s = nom_utilisateur
        self.__mdp_s = mdp
        self.__admin_s = admin
    
    def __str__(self):
        return f"id spectateur : {self.__id_s}, le nom : {self.__nom_s}, le prenom : {self.__prenom_s}, le nom utilisateur : {self.__nom_utilisateur_s}"
