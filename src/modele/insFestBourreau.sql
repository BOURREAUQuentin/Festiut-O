-- Insertions pour la table STYLE_MUSICAL
INSERT INTO STYLE_MUSICAL (idSt, nomSt, caracteristiquesSt) VALUES 
(1, 'Jazz', 'Improvisation musicale'),
(2, 'Rock', 'Rythmes puissants et guitares électriques'),
(3, 'Classique', 'Musique orchestrale traditionnelle');

-- Insertions pour la table SPECTATEUR
INSERT INTO SPECTATEUR (idS, nomS, prenomS, mailS, dateNaissS, telS, nomUtilisateurS, mdpS, adminS) VALUES 
(1, 'Doe', 'John', 'john.doe@example.com', '1990-01-15', '1234567890', 'johndoe', 'password', 'N'),
(2, 'Smith', 'Alice', 'alice.smith@example.com', '1985-05-22', '9876543210', 'alicesmith', 'password', 'N'),
(3, 'Johnson', 'Michael', 'michael.johnson@example.com', '1982-11-10', '1122334455', 'michaeljohnson', 'password', 'N');

-- Insertions pour la table ARTISTE
INSERT INTO ARTISTE (idA, nomA, descriptionA) VALUES 
(1, 'John Lennon', 'Guitariste et chanteur légendaire'),
(2, 'Jimi Hendrix', "L'un des meilleurs guitaristes de tous les temps"),
(3, 'Wolfgang Amadeus Mozart', 'Compositeur classique autrichien');

-- Insertions pour la table LIEU
INSERT INTO LIEU (idL, nomL, adresseL, nbMaxSpecL) VALUES 
(1, 'Salle de concert A', '456 Center St', 1),
(2, 'Théâtre B', '789 Broadway', 300),
(3, 'Opéra C', '101 Opera Lane', 700);

-- Insertions pour la table GROUPE
INSERT INTO GROUPE (idG, nomG, descriptionG) VALUES 
(1, 'The Beatles', 'Légendaire groupe de rock britannique'),
(2, 'The Rolling Stones', 'Groupe de rock emblématique'),
(3, 'Orchestre Philharmonique de New York', 'Fameux orchestre symphonique américain');

-- Insertions pour la table INSTRUMENT
INSERT INTO INSTRUMENT (idI, nomI) VALUES 
(1, 'Guitare'),
(2, 'Batterie'),
(3, 'Violon');

-- Insertions pour la table JOURNEE
INSERT INTO JOURNEE (idJ, dateJ) VALUES 
(1, '2024-07-18'),
(2, '2024-07-19'),
(3, '2024-07-20');

-- Insertions pour la table EVENEMENT
INSERT INTO EVENEMENT (idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE, idL, idJ, idG) VALUES 
(1, 'Concert des Beatles', 'Concert exceptionnel du célèbre groupe', '20:00:00', '02:00:00', '03:00:00', '01:00:00', 1, 1, 1),
(2, 'Concert des Rolling Stones', 'Performance live des légendaires Rolling Stones', '19:30:00', '02:30:00', '02:30:00', '00:45:00', 2, 2, 2),
(3, "Concert de l'Orchestre Philharmonique", "Soirée musicale avec l'orchestre symphonique", '19:00:00', '03:00:00', '03:30:00', '01:15:00', 3, 3, 3);

-- Insertions pour la table FAIRE_PARTIE
INSERT INTO FAIRE_PARTIE (idG, idA) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insertions pour la table FAVORI
INSERT INTO FAVORI (idS, idG) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insertions pour la table HEBERGEMENT
INSERT INTO HEBERGEMENT (idH, nomH, adresseH, nbPlacesMaxH) VALUES 
(1, 'Hôtel ABC', '789 Elm St', 100),
(2, 'Auberge XYZ', '123 Pine St', 50),
(3, 'Hôtel 123', '456 Oak St', 80);

-- Insertions pour la table HEBERGER
INSERT INTO HEBERGER (idH, idG) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insertions pour la table INTERPRETER
INSERT INTO INTERPRETER (idG, idSt) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insertions pour la table JOUER
INSERT INTO JOUER (idA, idI) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insertions pour la table RESEAU_SOCIAL
INSERT INTO RESEAU_SOCIAL (idRS, nomRS, lienRS, idG) VALUES 
(1, 'Facebook', 'https://www.facebook.com/thebeatles', 1),
(2, 'Twitter', 'https://twitter.com/therollingstones', 2),
(3, 'Instagram', 'https://www.instagram.com/orchestraphilharmonic/', 3);

-- Insertions pour la table RESEAU_VIDEO
INSERT INTO RESEAU_VIDEO (idRV, nomRV, lienRV, idG) VALUES 
(1, 'YouTube', 'https://youtube.com', 1),
(2, 'Vimeo', 'https://youtube.com', 2),
(3, 'Dailymotion', 'https://youtube.com', 3);

-- Insertions pour la table BILLET
INSERT INTO BILLET (idB, prixB, idS) VALUES 
(1, 50, 1),
(2, 55, 2),
(3, 40, 3);

-- Insertions pour la table ACCEDER
INSERT INTO ACCEDER (idB, idJ) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insertions pour la table A_SOUS_STYLE
INSERT INTO A_SOUS_STYLE (idSt1, idSt2) VALUES
(1, 2), -- Le style musical 1 (Jazz) est lié au style musical 2 (Rock)
(1, 3), -- Le style musical 1 (Jazz) est lié au style musical 3 (Classique)
(2, 3); -- Le style musical 2 (Rock) est lié au style musical 3 (Classique)


-- Tentatives d'insertion d'un nouvel événement chevauchant la plage horaire (cette insertion devrait échouer en raison du trigger triggerSuperpositionEvenement)
-- INSERT INTO EVENEMENT (idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE, idL, idJ, idG)
-- VALUES (4, 'Nouvel Événement', 'Description du nouvel événement', '16:00:00', '08:00:00', '00:00:00', '00:00:00', 1, 1, 2);
-- INSERT INTO EVENEMENT (idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE, idL, idJ, idG)
-- VALUES (5, 'Nouvel Événement', 'Description du nouvel événement', '23:00:00', '01:00:00', '00:00:00', '00:00:00', 1, 1, 2);