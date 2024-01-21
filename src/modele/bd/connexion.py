import sqlalchemy

def ouvrir_connexion(user, passwd, host, database):
    """Ouvre la connexion à la bd
    """
    try:
        # Créer un moteur pour intéragir avec le serveur de base de données
        engine = sqlalchemy.create_engine(
            f"mysql+mysqlconnector://{user}:{passwd}@{host}/{database}")

        # Créer la connexion
        connexion = engine.connect()
        print("Connexion réussie !")
        return connexion
    except Exception as err:
        print("le serveur n'est pas connecté !")
        return err

connexion = ouvrir_connexion("bourreau", "bourreau", "servinfo-maria",
                       "DBbourreau")

def fermer_connexion():
    connexion.close()
