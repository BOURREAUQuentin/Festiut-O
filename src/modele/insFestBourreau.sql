-- Insertions pour la table STYLE_MUSICAL
INSERT INTO STYLE_MUSICAL (idSt, nomSt, caracteristiquesSt) VALUES 
(1, 'Jazz', 'Improvisation musicale'),
(2, 'Rock', 'Rythmes puissants et guitares électriques'),
(3, 'Rap', 'Égrener des couplets rimés séparés par des refrains, accompagnés de rythmes'),
(4, 'Classique', 'Musique orchestrale traditionnelle');

-- Insertions pour la table SPECTATEUR
INSERT INTO SPECTATEUR (idS, nomS, prenomS, mailS, dateNaissS, telS, nomUtilisateurS, mdpS, adminS) VALUES 
(1, 'Doe', 'John', 'john.doe@example.com', '1990-01-15', '1234567890', 'adm', 'adm', 'O'),
(2, 'Smith', 'Alice', 'alice.smith@example.com', '1985-05-22', '9876543210', 'alicesmith', 'password', 'N'),
(3, 'Johnson', 'Michael', 'michael.johnson@example.com', '1982-11-10', '1122334455', 'michaeljohnson', 'password', 'N'),
(4, 'Bourreau', 'Quentin', 'quentin.bourreau@example.com', '2004-12-14', '0684525642', 'quentin', 'quentin', 'N');

-- Insertions pour la table ARTISTE
INSERT INTO ARTISTE (idA, nomA, descriptionA, lienImageA) VALUES 
(1, 'John Lennon', 'Guitariste et chanteur légendaire', 'johnlennon.jpg'),
(2, 'George Harrison', "L'un des meilleurs guitaristes de tous les temps", 'georgeharrison.jpg'),
(3, 'Paul McCartney', 'Compositeur classique autrichien', 'paulmccartney.jpg'),
(4, 'Favé', 'Difficile de passer à côté du phénomène Favé !', 'fave.jpg'),
(5, 'Gazo', 'Gazo la mala est gangx boy', 'gazo.jpg'),
(6, 'Kerchak', 'Le rappeur jeune cagoulé', 'kerchak.jpg'),
(7, 'Ninho', 'Ninho le crack de fou malade', 'ninho.jpg');

-- Insertions pour la table LIEU
INSERT INTO LIEU (idL, nomL, adresseL, nbMaxSpecL) VALUES 
(1, 'Salle de concert A', '456 Center St', 1),
(2, 'Théâtre B', '789 Broadway', 300),
(3, 'Opéra C', '101 Opera Lane', 700);

-- Insertions pour la table GROUPE
INSERT INTO GROUPE (idG, nomG, courteDescriptionG, longueDescriptionG, lienImageG) VALUES 
(1, 'Favé', 'Difficile de passer à côté du phénomène Favé ! Ce jeune rappeur affole déjà tous les compteurs...', 'Difficile de passer à côté du phénomène Favé ! Ce jeune rappeur venu tout droit du 95 affole déjà tous les compteurs… Après le carton de son titre Urus certifié single de platine avec plus 45 millions de streams, il sort son premier EP appelé F4 et met tout le monde d’accord. Plus récemment on pouvait le retrouver sur le titre No Lèche en featuring avec Gazo, Kerchak & Leto et sur son dernier freestyle J’aime pas perdre. Sa signature : des sons dynamiques et des refrains qui restent dans la tête toute la journée. On l’écoute pour se donner de l’énergie et profiter de sa vibe et ça fonctionne.', 'fave.jpg'),
(2, 'Gazo', 'Caractérisé par une voix rauque et un flow unique, Gazo explore la drill.', 'Gazo est aujourd’hui l’une des figures les plus importantes de la drill dans l’univers du rap français. Il a su s’imposer et fait désormais partie du gratin du mouvement hip-hop dans l’hexagone. Ibrahima Diakité de son nom à l’état civil est né le 5 août 1994 à Châteauroux en France. D’origine guinéenne, Gazo est issu d’une fratrie de 5 enfants dont il est le benjamin. Caractérisé par une voix rauque et un flow unique, Gazo explore en dehors de la drill des genres musicaux comme la trap, le rap hardcore ou encore le gangsta rap. Il a grandi dans des petits logements de la Roquette dans le 11e arrondissement de Paris. À l’âge de 11 ans, il connut la réalité du foyer éducatif sur décision de justice. Il arrêtera l’école très tôt, déjà en sixième.', 'gazo.jpg'),
(3, 'Kerchak', 'Après une saison 1 à 200km/h marquée par la certification de son projet « Confiance »', 'Après une saison 1 à 200km/h marquée par la certification de son projet « Confiance » et une Cigale complète en quelques jours, Kerchak revient pour la saison 2 passer un second step avec un nouveau projet et une date événement à l’Olympia le 10 mai 2024 !', 'kerchak.jpg'),
(4, 'Ninho', 'Ninho est un rappeur freestyler et chanteur français d’origine congolaise.', 'Ninho est un rappeur freestyler et chanteur français d’origine congolaise. En imitant les grands rappeurs qu’il côtoie à Yerres où il vit, il développe très tôt son propre style en s’inspirant du flow des rappeurs américains, et se fait rapidement connaître sur la scène du rap français. Découvrez dans cet article la carrière d’un rappeur confirmé à l’avenir prometteur. Le rappeur Ninho est l’artiste le plus streamé de l’année, et ceci pour la deuxième année consécutive. D’ailleurs, sa récente mixtape a uniquement été écoulée sur les plateformes. En effet, pour se faire connaître, Ninho commence à se filmer pendant ses différents remixes et freestyles. Après avoir mis des vidéos sur la plateforme YouTube, il se fait un nom dans le monde du rap français et cumule plusieurs centaines de milliers de vues en quelques mois. Aujourd’hui, il tease régulièrement ses singles et les met en exploitation sur les plateformes de téléchargement.', 'ninho.jpg'),
(5, 'The Beatles', 'The Beatles est un groupe de rock britannique originaire de Liverpool', 'The Beatles est un groupe de rock britannique originaire de Liverpool, en Angleterre. Le noyau du groupe se forme avec les Quarrymen fondés par John Lennon en 1957, il adopte son nouveau nom en 1960 et, à partir de 1962, prend sa configuration définitive, composé de John Lennon, Paul McCartney, George Harrison et, le dernier à se joindre, Ringo Starr. Il est considéré comme le groupe le plus populaire et influent de l’histoire du rock. En dix ans d’existence et seulement sept ans d’enregistrement (de 1962 à 1969)a, les Beatles ont enregistré douze albums originaux et composé près de 200 chansons majoritairement écrites par le tandem Lennon/McCartney, dont le succès dans l’histoire de l’industrie discographique reste inégalé.', 'thebeatles.jpg');

-- Insertions pour la table INSTRUMENT
INSERT INTO INSTRUMENT (idI, nomI) VALUES 
(1, 'Guitare'),
(2, 'Batterie'),
(3, 'Violon');

-- Insertions pour la table JOURNEE
INSERT INTO JOURNEE (idJ, dateJ) VALUES 
(1, '2024-07-18'),
(2, '2024-07-19');

-- Insertions pour la table EVENEMENT
INSERT INTO EVENEMENT (idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE, idL, idJ, idG) VALUES 
(1, 'Concert des Beatles', 'Concert exceptionnel du célèbre groupe', '20:00:00', '02:00:00', '03:00:00', '01:00:00', 1, 1, 5),
(2, 'Concert de Favé', 'Performance live du légendaire Favé', '19:30:00', '02:30:00', '02:30:00', '00:45:00', 2, 2, 1),
(3, "Concert de Gazo", "Soirée mouvementé par ses musiques connues à l'international", '19:00:00', '03:00:00', '03:30:00', '01:15:00', 3, 2, 2);

-- Insertions pour la table FAIRE_PARTIE
INSERT INTO FAIRE_PARTIE (idG, idA) VALUES
(1, 4),
(2, 5),
(3, 6),
(4, 7),
(5, 1),
(5, 2),
(5, 3);

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
(1, 'Instagram', 'https://www.instagram.com/fave.db/?hl=fr', 1),
(2, 'Instagram', 'https://www.instagram.com/gazo_officiel/?hl=fr', 2),
(3, 'Instagram', 'https://www.instagram.com/kerchak9b/?hl=fr', 3),
(4, 'Instagram', 'https://www.instagram.com/ninhosdt/?hl=fr', 4),
(5, 'Instagram', 'https://www.instagram.com/thebeatles/', 5);

-- Insertions pour la table RESEAU_VIDEO
INSERT INTO RESEAU_VIDEO (idRV, nomRV, lienRV, idG) VALUES 
(1, 'Youtube', 'https://www.youtube.com/channel/UC6yKbnMj2JpyaigY16AYQ9Q', 1),
(2, 'Youtube', 'https://www.youtube.com/chann