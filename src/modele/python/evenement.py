class Evenement:
    def __init__(self, id_evenement, nom, description, heure_debut, heure_fin, duree, tps_montage, tps_demontage, id_lieu, id_journee, id_groupe):
        self.__id_e = id_evenement
        self.__nom_e = nom
        self.__description_e = description
        self.__heure_debut_e = heure_debut
        self.__heure_fin_e = heure_fin
        self.__duree_e = duree
        self.__tps_montage_e = tps_montage
        self.__tps_demontage_e = tps_demontage
        self.__id_lieu_e = id_lieu
        self.__id_journee_e = id_journee
        self.__id_groupe_e = id_groupe
    
    def get_id(self):
        return self.__id_e
    
    def get_nom(self):
        return self.__nom_e
    
    def get_description(self):
        return self.__description_e
    
    def get_heure_debut(self):
        return self.__heure_debut_e
    
    def get_heure_fin(self):
        return self.__heure_fin_e
    
    def get_duree(self):
        return self.__duree_e
    
    def get_tps_montage(self):
        return self.__tps_montage_e
    
    def get_tps_demontage(self):
        return self.__tps_demontage_e
    
    def get_id_lieu(self):
        return self.__id_lieu_e
    
    def get_id_journee(self):
        return self.__id_journee_e
    
    def get_id_groupe(self):
        return self.__id_groupe_e
    
    def set_nom(self, nouveau_nom):
        self.__nom_e = nouveau_nom
    
    def set_description(self, nouvelle_description):
        self.__description_e = nouvelle_description
    
    def set_heure_debut(self, nouvelle_heure_debut):
        self.__heure_debut_e = nouvelle_heure_debut
    
    def set_heure_fin(self, nouvelle_heure_fin):
        self.__heure_fin_e = nouvelle_heure_fin
    
    def set_tps_montage(self, nouveau_tps_montage):
        self.__tps_montage_e = nouveau_tps_montage
    
    def set_tps_demontage(self, nouveau_tps_demontage):
        self.__tps_demontage_e = nouveau_tps_demontage

    def __str__(self):
        return f"id evenement : {self.__id_e}, le nom : {self.__nom_e}, la description : {self.__description_e}, l'heure de début : {self.__heure_debut_e}, l'heure de fin : {self.__heure_fin_e}, la durée : {self.__duree_e}"
