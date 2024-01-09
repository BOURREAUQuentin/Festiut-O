CREATE TABLE STYLE_MUSICAL (
  idSt INT(40) NOT NULL,
  nomSt VARCHAR(42) NOT NULL,
  caracteristiquesSt VARCHAR(42) NOT NULL,
  PRIMARY KEY (idSt)
);

CREATE TABLE SPECTATEUR (
  idS INT(40) NOT NULL,
  nomS VARCHAR(42) NOT NULL,
  prenomS VARCHAR(42) NOT NULL,
  mailS VARCHAR(100) UNIQUE NOT NULL,
  dateNaissS DATE NOT NULL,
  telS CHAR(10) NOT NULL,
  nomUtilisateurS VARCHAR(42),
  mdpS VARCHAR(42) NOT NULL,
  adminS VARCHAR(1) DEFAULT 'N',
  PRIMARY KEY (idS),
  CONSTRAINT majorite CHECK (TIMESTAMPDIFF(YEAR,dateNaissS,'2024-07-18') >= 18)
);

CREATE TABLE ARTISTE (
  idA INT(40) UNIQUE NOT NULL,
  nomA VARCHAR(42) NOT NULL,
  descriptionA VARCHAR(100),
  PRIMARY KEY (idA)
);

CREATE TABLE LIEU (
  idL INT(40) NOT NULL,
  nomL VARCHAR(42) NOT NULL,
  adresseL VARCHAR(100) NOT NULL,
  nbMaxSpecL INT(5) CHECK (nbMaxSpecL > 0),
  PRIMARY KEY (idL)
);

CREATE TABLE GROUPE (
  idG INT(40) NOT NULL,
  nomG VARCHAR(42) NOT NULL,
  descriptionG VARCHAR(100) NOT NULL,
  lienImageG VARCHAR(100),
  PRIMARY KEY (idG)
);

CREATE TABLE INSTRUMENT (
  idI INT(40) NOT NULL,
  nomI VARCHAR(42) NOT NULL,
  PRIMARY KEY (idI)
);

CREATE TABLE JOURNEE (
  idJ INT(40) NOT NULL,
  dateJ DATE UNIQUE CHECK (dateJ BETWEEN '2024-07-18' AND '2024-07-20'),
  PRIMARY KEY (idJ)
);

CREATE TABLE EVENEMENT (
  idE INT(40) NOT NULL,
  nomE VARCHAR(42) NOT NULL,
  descriptionE VARCHAR(100) NOT NULL,
  heureDebutE TIME NOT NULL,
  dureeE TIME NOT NULL,
  tpsMontageE TIME NOT NULL,
  tpsDemontageE TIME NOT NULL,
  idL INT(40) NOT NULL,
  idJ INT(40) NOT NULL,
  idG INT(40) NOT NULL,
  PRIMARY KEY (idE),
  FOREIGN KEY (idJ) REFERENCES JOURNEE (idJ),
  FOREIGN KEY (idL) REFERENCES LIEU (idL),
  FOREIGN KEY (idG) REFERENCES GROUPE (idG)
);

CREATE TABLE FAIRE_PARTIE (
  idG INT(40) NOT NULL,
  idA INT(40) UNIQUE NOT NULL,
  PRIMARY KEY (idG, idA),
  FOREIGN KEY (idG) REFERENCES GROUPE (idG),
  FOREIGN KEY (idA) REFERENCES ARTISTE (idA)
);

CREATE TABLE FAVORI (
  idS INT(40) NOT NULL,
  idG INT(40) NOT NULL,
  PRIMARY KEY (idS, idG),
  FOREIGN KEY (idG) REFERENCES GROUPE (idG),
  FOREIGN KEY (idS) REFERENCES SPECTATEUR (idS)
);

CREATE TABLE HEBERGEMENT (
  idH INT(40) NOT NULL,
  nomH VARCHAR(42) NOT NULL,
  adresseH VARCHAR(100) NOT NULL,
  nbPlacesMaxH INT(3) CHECK (nbPlacesMaxH > 0),
  PRIMARY KEY (idH)
);

CREATE TABLE HEBERGER (
  idH INT(40) NOT NULL,
  idG INT(40) NOT NULL,
  PRIMARY KEY (idH, idG),
  FOREIGN KEY (idG) REFERENCES GROUPE (idG)
);

CREATE TABLE INTERPRETER (
  idG INT(40) NOT NULL,
  idSt INT(40) NOT NULL,
  PRIMARY KEY (idG, idSt),
  FOREIGN KEY (idG) REFERENCES GROUPE (idG),
  FOREIGN KEY (idSt) REFERENCES STYLE_MUSICAL (idSt)
);

CREATE TABLE JOUER (
  idA INT(40) NOT NULL,
  idI INT(40) NOT NULL,
  PRIMARY KEY (idA, idI),
  FOREIGN KEY (idA) REFERENCES ARTISTE (idA),
  FOREIGN KEY (idI) REFERENCES INSTRUMENT (idI)
);

CREATE TABLE RESEAU_SOCIAL (
  idRS INT(40) NOT NULL,
  nomRS VARCHAR(42) NOT NULL,
  lienRS VARCHAR(100) NOT NULL,
  idG INT(40) NOT NULL,
  PRIMARY KEY (idRS),
  FOREIGN KEY (idG) REFERENCES GROUPE (idG)
);

CREATE TABLE RESEAU_VIDEO (
  idRV INT(40) NOT NULL,
  nomRV VARCHAR(42) NOT NULL,
  lienRV VARCHAR(100) NOT NULL,
  idG INT(40) NOT NULL,
  PRIMARY KEY (idRV),
  FOREIGN KEY (idG) REFERENCES GROUPE (idG)
);

CREATE TABLE BILLET (
  idB INT(40) NOT NULL,
  prixB INT(3) NOT NULL,
  idS INT(40) NOT NULL,
  PRIMARY KEY (idB),
  FOREIGN KEY (idS) REFERENCES SPECTATEUR (idS)
);

CREATE TABLE ACCEDER (
  idB INT(40) NOT NULL,
  idJ INT(40) NOT NULL,
  PRIMARY KEY (idB, idJ),
  FOREIGN KEY (idB) REFERENCES BILLET (idB),
  FOREIGN KEY (idJ) REFERENCES JOURNEE (idJ)
);

CREATE TABLE A_SOUS_STYLE (
  idSt1 INT(40) NOT NULL,
  idSt2 INT(40) NOT NULL,
  PRIMARY KEY (idSt1, idSt2),
  FOREIGN KEY (idSt1) REFERENCES STYLE_MUSICAL (idSt),
  FOREIGN KEY (idSt2) REFERENCES STYLE_MUSICAL (idSt)
);

--  le trigger
DELIMITER |

CREATE TRIGGER triggerSuperpositionEvenement BEFORE INSERT ON EVENEMENT FOR EACH ROW
BEGIN
    DECLARE evenements_existants INT;
    DECLARE nouvel_evenement_debut TIME;
    DECLARE nouvel_evenement_fin TIME;
    
    -- calculer l'heure de début réelle de l'événement avec le temps de montage
    SET nouvel_evenement_debut = SUBTIME(NEW.heureDebutE, NEW.tpsMontageE);
    -- calculer l'heure de fin réelle de l'événement avec la durée, le temps de montage et le temps de démontage
    SET nouvel_evenement_fin = ADDTIME(ADDTIME(NEW.heureDebutE, NEW.dureeE), NEW.tpsDemontageE);

    -- vérifier s'il y a des événements existants pour le même lieu et la même plage horaire (y compris le temps de montage et de démontage)
    SET evenements_existants = (
        SELECT COUNT(*)
        FROM EVENEMENT
        WHERE idL = NEW.idL 
        AND (
            -- vérifier si le début de l'événement chevauche un autre événement
            (nouvel_evenement_debut BETWEEN SUBTIME(heureDebutE, tpsMontageE) AND ADDTIME(ADDTIME(heureDebutE, dureeE), tpsDemontageE))
            -- vérifier si la fin de l'événement chevauche un autre événement
            OR (nouvel_evenement_fin BETWEEN SUBTIME(heureDebutE, tpsMontageE) AND ADDTIME(ADDTIME(heureDebutE, dureeE), tpsDemontageE))
            -- vérifier si l'événement existant chevauche le début de l'événement en cours
            OR (nouvel_evenement_debut < SUBTIME(heureDebutE, tpsMontageE) AND ADDTIME(nouvel_evenement_fin, NEW.tpsDemontageE) > ADDTIME(ADDTIME(heureDebutE, dureeE), tpsDemontageE))
        )
    );
    
    -- si des événements existants sont trouvés, annuler l'insertion
    IF evenements_existants > 0 THEN
        SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = "Impossible d'ajouter l'événement. La plage horaire est déjà réservée pour un autre événement sur ce lieu.";
    END IF;
END |

DELIMITER ;

-- les procédures
DELIMITER |

CREATE OR REPLACE PROCEDURE AfficherEvenementsParJour (idJour INT)
BEGIN
    SELECT idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE
    FROM EVENEMENT
    WHERE idJ = idJour;
END |

DELIMITER ;

DELIMITER |
CREATE OR REPLACE PROCEDURE UpdateGroupe(newIdG INT, newNomG VARCHAR(42), newDescriptionG VARCHAR(100))
BEGIN
    UPDATE GROUPE
    SET nomG = newNomG, descriptionG = newDescriptionG
    WHERE idG = newIdG;
END |
DELIMITER ;

DELIMITER |
CREATE OR REPLACE PROCEDURE ReserveBillets(idS INT, idE INT, nbBillets INT)
BEGIN
    DECLARE placesDisponibles INT;
    DECLARE placesReserves INT;

    -- Vérifiez le nombre de places disponibles pour l'événement
    SELECT nbMaxSpecL INTO placesDisponibles
    FROM LIEU
    WHERE idL = (SELECT idL FROM EVENEMENT WHERE idE = idE);

    -- Comptez le nombre de billets déjà réservés pour l'événement
    SELECT COUNT(*) INTO placesReserves
    FROM ACCEDER
    WHERE idE = idE;

    -- Vérifiez si le nombre total de billets réservés dépasse la capacité maximale
    IF (placesReserves + nbBillets) <= placesDisponibles THEN
        -- Réservez les billets
        INSERT INTO ACCEDER (idB, idJ) VALUES (idS, (SELECT idJ FROM EVENEMENT WHERE idE = idE));
    ELSE
        SIGNAL SQLSTATE "45000"
        SET MESSAGE_TEXT = "Capacité maximale du lieu dépassée. Impossible de réserver ces billets.";
    END IF;
END |
DELIMITER;

-- les fonctions
DELIMITER |
CREATE OR REPLACE FUNCTION GetGroupesParStyleMusical(nomStyle VARCHAR(255)) RETURNS VARCHAR(255)
BEGIN
    DECLARE groupes_liste VARCHAR(255);

    SELECT GROUP_CONCAT(nomG SEPARATOR ', ')
    INTO groupes_liste
    FROM GROUPE NATURAL JOIN INTERPRETER NATURAL JOIN STYLE_MUSICAL
    WHERE nomSt = nomStyle;

    RETURN groupes_liste;
END |

DELIMITER ;

DELIMITER |
CREATE OR REPLACE FUNCTION GetNombreBilletsReserves(idEvenement INT) RETURNS INT
BEGIN
    DECLARE nbBillets INT;

    SELECT IFNULL(COUNT(*),0) INTO nbBillets
    FROM ACCEDER
    WHERE idE = idEvenement;

    RETURN nbBillets;
END |
DELIMITER ;