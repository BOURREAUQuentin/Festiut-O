-- Insertions pour la table STYLE_MUSICAL
INSERT INTO STYLE_MUSICAL (idSt, nomSt, caracteristiquesSt) VALUES 
(1, 'Jazz', 'Improvisation musicale'),
(2, 'Rock', 'Rythmes puissants et guitares électriques'),
(3, 'Rap', 'Couplets rimés séparés par des refrains'),
(4, 'Classique', 'Musique orchestrale traditionnelle');

-- Insertions pour la table SPECTATEUR
INSERT INTO SPECTATEUR (idS, nomS, prenomS, mailS, dateNaissS, telS, nomUtilisateurS, mdpS, adminS) VALUES 
(1, 'Doe', 'John', 'john.doe@example.com', '1990-01-15', '1234567890', 'adm', 'Test@123', 'O'),
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
(6, 'Chris Martin', 'Chanteur de Coldplay', 'chrismartin.jpg'),
(7, 'Thom Yorke', 'Chanteur de Radiohead', 'thomyorke.jpg'),
(8, 'Freddie Mercury', 'Chanteur de Queen', 'freddiemercury.jpg'),
(9, 'Bono', 'Chanteur de U2', 'bono.jpg'),
(10, 'James Hetfield', 'Chanteur et guitariste de Metallica', 'jameshetfield.jpg'),
(11, 'Mick Jagger', 'Chanteur des Rolling Stones', 'mickjagger.jpg'),
(12, 'Chester Bennington', 'Chanteur de Linkin Park', 'chesterbennington.jpg'),
(13, 'Win Butler', "Chanteur d'Arcade Fire", 'winbutler.jpg'),
(14, 'Anthony Kiedis', 'Chanteur des Red Hot Chili Peppers', 'anthonykiedis.jpg'),
(15, 'Dave Grohl', 'Chanteur des Foo Fighters', 'davegrohl.jpg'),
(16, 'Alex Turner', 'Chanteur des Arctic Monkeys', 'alexturner.jpg'),
(17, 'Matthew Bellamy', 'Chanteur de Muse', 'matthewbellamy.jpg'),
(18, 'Brandon Flowers', 'Chanteur des Killers', 'brandonflowers.jpg'),
(19, 'Billie Joe Armstrong', 'Chanteur de Green Day', 'billiejoearmstrong.jpg'),
(20, 'Damon Albarn', 'Chanteur de Blur', 'damonalbarn.jpg'),
(21, 'Jonny Buckland', 'Guitariste de Coldplay', 'jonnybuckland.jpg'),
(22, 'Thom Yorke', 'Chanteur de Radiohead', 'thomyorke.jpg'),
(23, 'Brian May', 'Guitariste de Queen', 'brianmay.jpg'),
(24, 'The Edge', 'Guitariste de U2', 'theedge.jpg'),
(25, 'Lars Ulrich', 'Batteur de Metallica', 'larsulrich.jpg'),
(26, 'Keith Richards', 'Guitariste des Rolling Stones', 'keithrichards.jpg'),
(27, 'Chester Bennington', 'Chanteur de Linkin Park', 'chesterbennington.jpg'),
(28, 'Win Butler', "Chanteur d'Arcade Fire", 'winbutler.jpg'),
(29, 'Flea', 'Bassiste des Red Hot Chili Peppers', 'flea.jpg'),
(30, 'Dave Grohl', 'Chanteur des Foo Fighters', 'davegrohl.jpg'),
(31, 'Jamie Cook', 'Guitariste des Arctic Monkeys', 'jamiecook.jpg'),
(32, 'Chris Wolstenholme', 'Bassiste de Muse', 'chriswolstenholme.jpg'),
(33, 'Dave Keuning', 'Guitariste des Killers', 'davekeuning.jpg'),
(34, 'Mike Dirnt', 'Bassiste de Green Day', 'mikedirnt.jpg'),
(35, 'Graham Coxon', 'Guitariste de Blur', 'grahamcoxon.jpg'),
(36, 'Kerchak', 'Le rappeur jeune cagoulé', 'kerchak.jpg'),
(37, 'Ninho', 'Ninho le crack de fou malade', 'ninho.jpg');

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
(5, 'The Beatles', 'The Beatles est un groupe de rock britannique originaire de Liverpool', 'The Beatles est un groupe de rock britannique originaire de Liverpool, en Angleterre. Le noyau du groupe se forme avec les Quarrymen fondés par John Lennon en 1957, il adopte son nouveau nom en 1960 et, à partir de 1962, prend sa configuration définitive, composé de John Lennon, Paul McCartney, George Harrison et, le dernier à se joindre, Ringo Starr. Il est considéré comme le groupe le plus populaire et influent de l’histoire du rock. En dix ans d’existence et seulement sept ans d’enregistrement (de 1962 à 1969)a, les Beatles ont enregistré douze albums originaux et composé près de 200 chansons majoritairement écrites par le tandem Lennon/McCartney, dont le succès dans l’histoire de l’industrie discographique reste inégalé.', 'thebeatles.jpg'),
(6, 'Coldplay', 'Groupe de pop-rock britannique', 'Coldplay est un groupe de pop-rock britannique formé en 1996 à Londres. Composé de Chris Martin, Jonny Buckland, Guy Berryman et Will Champion, le groupe a connu un immense succès mondial avec des albums tels que "Parachutes", "A Rush of Blood to the Head" et "Viva la Vida". Leur musique est caractérisée par des mélodies accrocheuses, des paroles émotionnelles et des arrangements créatifs.', 'coldplay.jpg'),
(7, 'Radiohead', 'Pionniers du rock alternatif', "Radiohead est un groupe de rock alternatif britannique formé en 1985. Leurs albums emblématiques incluent 'OK Computer', 'Kid A' et 'In Rainbows'. Radiohead est connu pour son innovation musicale, ses paroles profondes et son engagement envers l'expérimentation sonore.", "radiohead.jpg"),
(8, 'Queen', 'Légendes du rock', "Queen est un groupe de rock britannique formé en 1970, comprenant Freddie Mercury, Brian May, Roger Taylor et John Deacon. Ils ont produit certains des plus grands succès de l'histoire du rock, tels que 'Bohemian Rhapsody', 'We Will Rock You' et 'Another One Bites the Dust'.", 'queen.jpg'),
(9, 'U2', 'Rock alternatif et engagement social', 'U2 est un groupe de rock irlandais formé en 1976. Avec Bono, The Edge, Adam Clayton et Larry Mullen Jr., U2 est connu pour ses performances énergiques et ses paroles engagées. Leurs albums incluent "The Joshua Tree" et "Achtung Baby".', 'u2.jpg'),
(10, 'Metallica', 'Pionniers du heavy metal', 'Metallica est un groupe de heavy metal américain formé en 1981. Composé de James Hetfield, Lars Ulrich, Kirk Hammett et Robert Trujillo, le groupe a eu un impact majeur sur le genre avec des albums comme "Master of Puppets" et "Metallica" (communément appelé "The Black Album").', 'metallica.jpg'),
(11, 'The Rolling Stones', 'Légendes du rock', "The Rolling Stones est un groupe de rock britannique formé en 1962. Composé de Mick Jagger, Keith Richards, Charlie Watts et Ronnie Wood, ils sont l'un des groupes les plus durables et influents de l'histoire du rock. Leurs hits incluent 'Satisfaction' et 'Paint It, Black'.", 'rollingstones.jpg'),
(12, 'Linkin Park', 'Fusion rock et nu metal', 'Linkin Park est un groupe américain formé en 1996. Connus pour leur fusion de rock alternatif et de nu metal, ils ont atteint un grand succès avec des albums tels que "Hybrid Theory" et "Meteora". Le chanteur Chester Bennington était au cœur de leur identité sonore.', 'linkinpark.jpg'),
(13, 'Arcade Fire', 'Indie rock et orchestration épique', "Arcade Fire est un groupe de rock indépendant canadien formé en 2001. Leurs performances énergiques et leurs arrangements orchestraux ont valu des éloges critiques. Leur album 'The Suburbs' a remporté le Grammy Award de l'album de l'année en 2011.", 'arcadefire.jpg'),
(14, 'Red Hot Chili Peppers', 'Funk rock et énergie explosive', "Red Hot Chili Peppers est un groupe de rock américain formé en 1983. Connus pour leur fusion de funk, de rock et de punk, ils ont produit des tubes tels que 'Under the Bridge' et 'Californication'.", 'redhotchilipeppers.jpg'),
(15, 'Foo Fighters', 'Rock alternatif et énergie contagieuse', "Foo Fighters est un groupe de rock américain formé en 1994 par Dave Grohl, ancien batteur de Nirvana. Leur musique est caractérisée par des mélodies accrocheuses et une énergie positive. Des albums comme 'The Colour and the Shape' ont solidifié leur statut dans l'industrie.", 'foofighters.jpg'),
(16, 'Arctic Monkeys', 'Rock indépendant et post-punk revival', 'Arctic Monkeys est un groupe de rock indépendant britannique formé en 2002. Ils sont connus pour leur style énergique, leurs paroles intelligentes et leur influence post-punk revival. Des albums comme "Whatever People Say I Am, That''s What I''m Not" ont été salués par la critique.', 'arcticmonkeys.jpg'),
(17, 'Muse', 'Rock alternatif et expérimentation musicale', 'Muse est un groupe de rock britannique formé en 1994. Composé de Matthew Bellamy, Chris Wolstenholme et Dominic Howard, ils sont célèbres pour leur style musical éclectique et leurs performances scéniques spectaculaires. Des albums comme "Absolution" et "The Resistance" ont marqué leur carrière.', 'muse.jpg'),
(18, 'The Killers', 'Indie rock et new wave', "The Killers est un groupe de rock américain formé en 2001. Leurs mélodies accrocheuses et leur mélange d'indie rock et de new wave ont captivé les auditeurs du monde entier. Des hits comme 'Mr. Brightside' ont contribué à leur renommée.", 'thekillers.jpg'),
(19, 'Green Day', 'Punk rock et influence pop-punk', "Green Day est un groupe de punk rock américain formé en 1986. Ils sont connus pour leur influence majeure sur le genre punk et pop-punk. Des albums tels que 'Dookie' et 'American Idiot' ont été des succès commerciaux et critiques.", 'greenday.jpg'),
(20, 'Blur', 'Britpop et expérimentation sonore', "Blur est un groupe de britpop britannique formé en 1988. Ils sont reconnus pour leur contribution majeure au mouvement britpop avec des albums comme 'Parklife' et 'The Great Escape'. Leur exploration musicale a également incorporé des éléments d'expérimentation sonore.", 'blur.jpg');

-- Insertions pour la table INSTRUMENT
INSERT INTO INSTRUMENT (idI, nomI) VALUES 
(1, 'Guitare'),
(2, 'Batterie'),
(3, 'Basse'),
(4, 'Voix');

-- Insertions pour la table JOURNEE
INSERT INTO JOURNEE (idJ, dateJ) VALUES 
(1, '2024-07-18'),
(2, '2024-07-19');

-- Insertions pour la table EVENEMENT
INSERT INTO EVENEMENT (idE, nomE, descriptionE, heureDebutE, dureeE, tpsMontageE, tpsDemontageE, idL, idJ, idG) VALUES
-- Samedi
(1, "Concert de Metallica", "Dernier concert de leur groupe pour Metallica", '19:45:00', '03:00:00', '01:30:00', '01:30:00', 3, 1, 10),
(2, 'Concert des Beatles', 'Concert exceptionnel du célèbre groupe', '20:00:00', '02:00:00', '02:00:00', '01:00:00', 1, 1, 5),
(3, 'Concert des The Killers', 'Indie rock et new wave en live', '18:30:00', '01:00:00', '00:15:00', '00:15:00', 2, 1, 18),
(4, 'Showcase de Green Day', 'Une soirée punk rock avec Green Day', '21:15:00', '01:45:00', '01:15:00', '01:30:00', 2, 1, 19),
(5, 'Concert de Favé', "Une soirée très énergique pour son album 'Il le fallait'", '22:00:00', '02:15:00', '01:15:00', '00:45:00', 1, 1, 1),
-- Dimanche
(6, 'Concert de Favé', 'Performance live du légendaire Favé', '19:30:00', '02:30:00', '00:30:00', '00:45:00', 2, 2, 1),
(7, "Concert de Gazo", "Soirée mouvementé par ses musiques connues à l'international", '19:00:00', '03:00:00', '01:30:00', '01:15:00', 3, 2, 2),
(8, 'Showcase de Ninho', 'Showcase organisé sur son dernier album NI', '23:15:00', '01:30:00', '00:30:00', '00:15:00', 2, 2, 4),
(9, "Concert d'Arctic Monkeys", 'Performance live du groupe de rock indépendant', '00:30:00', '02:15:00', '01:45:00', '01:00:00', 1, 2, 16),
(10, 'Concert de Muse', 'Expérience musicale avec le groupe de rock alternatif', '16:00:00', '01:45:00', '01:00:00', '00:45:00', 2, 2, 17),
(11, 'Concert de Blur', 'Britpop et expérimentation sonore en direct', '16:30:00', '02:30:00', '02:00:00', '02:30:00', 1, 2, 20);

-- Insertions pour la table FAIRE_PARTIE
INSERT INTO FAIRE_PARTIE (idG, idA) VALUES
(1, 4),
(2, 5),
(3, 36),
(4, 37),
(5, 1),
(5, 2),
(5, 3),
(6, 6), -- Chris Martin dans Coldplay
(7, 7), -- Thom Yorke dans Radiohead
(8, 8), -- Freddie Mercury dans Queen
(9, 9), -- Bono dans U2
(10, 10), -- James Hetfield dans Metallica
(11, 11), -- Mick Jagger dans The Rolling Stones
(12, 12), -- Chester Bennington dans Linkin Park
(13, 13), -- Win Butler dans Arcade Fire
(14, 14), -- Anthony Kiedis dans Red Hot Chili Peppers
(15, 15), -- Dave Grohl dans Foo Fighters
(16, 16), -- Alex Turner dans Arctic Monkeys
(17, 17), -- Matthew Bellamy dans Muse
(18, 18), -- Brandon Flowers dans The Killers
(19, 19), -- Billie Joe Armstrong dans Green Day
(20, 20), -- Damon Albarn dans Blur
(6, 21),  -- Jonny Buckland dans Coldplay
(7, 22),  -- Thom Yorke dans Radiohead
(8, 23),  -- Brian May dans Queen
(9, 24),  -- The Edge dans U2
(10, 25), -- Lars Ulrich dans Metallica
(11, 26), -- Keith Richards dans The Rolling Stones
(12, 27), -- Chester Bennington dans Linkin Park
(13, 28), -- Win Butler dans Arcade Fire
(14, 29), -- Flea dans Red Hot Chili Peppers
(15, 30), -- Dave Grohl dans Foo Fighters
(16, 31), -- Jamie Cook dans Arctic Monkeys
(17, 32), -- Chris Wolstenholme dans Muse
(18, 33), -- Dave Keuning dans The Killers
(19, 34), -- Mike Dirnt dans Green Day
(20, 35); -- Graham Coxon dans Blur

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
(1, 4),
(2, 4),
(3, 4),
(32, 3),
(4, 4),
(5, 4),
(25, 2),
(10, 1);

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
(2, 'Youtube', 'https://www.youtube.com/channel/UCn2DAE87nJp01zbFmUI8V5A', 2),
(3, 'Youtube', 'https://www.youtube.com/channel/UCnE23B4C-iUTp_et-xl_EEQ', 3),
(4, 'Youtube', 'https://www.youtube.com/channel/UCXdHJabqwLJ3NvPfx6XmS5Q', 4),
(5, 'Youtube', 'https://www.youtube.com/channel/UCc4K7bAqpdBP8jh1j9XZAww', 5);

-- Insertions pour la table BILLET
INSERT INTO BILLET (idB, prixB) VALUES
-- billet id 1 donne accès -> journée 1 (samedi)
-- billet id 2 donne accès -> journée 1 et 2 (week-end)
-- billet id 3 donne accès -> journée 2 (dimanche)
(1, 50),
(2, 80),
(3, 50);

-- Insertions pour la table PANIER
INSERT INTO PANIER (idB, idS, quantiteB) VALUES
-- spectateur id 1 dans son panier -> journée 1
-- spectateur id 2 dans son panier -> journée 1 et journée 2 (avec pass 2 jours)
-- spectateur id 3 dans son panier -> journée 1 et journée 2 (sans pass 2 jours)
(1, 1, 1),
(2, 2, 2),
(2, 3, 3),
(3, 3, 1);

-- Insertions pour la table ACHETER
INSERT INTO ACHETER (idB, idS, quantiteB) VALUES
-- spectateur id 4 a acheté 2 billets -> journée 1
(2, 4, 2);

-- Insertions pour la table ACCEDER
INSERT INTO ACCEDER (idB, idJ) VALUES
-- billet id 1 donne accès -> journée 1 (samedi)
-- billet id 2 donne accès -> journée 1 et 2 (week-end)
-- billet id 3 donne accès -> journée 2 (dimanche)
(1, 1),
(2, 1),
(2, 2),
(3, 2);

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