DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `enigma`;
DROP TABLE IF EXISTS `bad_response`;
DROP TABLE IF EXISTS `enigma_bad_response`;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE enigma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE NOT NULL,
    image_url TEXT ,
    good_response TEXT NOT NULL,
    link_good_response TEXT NOT NULL DEFAULT 'http://127.0.0.1:5000/{{username}}/enigme/{{id_enigme+1}}',
    Message_bad_response TEXT NOT NULL DEFAULT 'Mauvaise réponse ! !'
);


--Create a table for storing multiple bad responses in the future. 
--will use Storage in JSON format
CREATE TABLE bad_response (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bad_responses TEXT NOT NULL, 
    enigma_id INTEGER,
    FOREIGN KEY (enigma_id) REFERENCES enigma(id)    
);


INSERT INTO user (email, username, password) VALUES ('monmail@ngft.com', 'Rem', 'monmotdepasse');

INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Qui est le meilleur prof du monde ?', '/image1.jpg', 'Guillaume', 'http://127.0.0.1:5000/Rem/enigme/2', 'Mauvaise réponse !!!');
INSERT INTO bad_response (bad_responses) VALUES ('Professeur Tournesol');

INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Quel est le meilleur langage du monde ?', '/image2.jpg', 'Python', 'http://127.0.0.1:5000/Rem/enigme/3', 'Mauvaise réponse !!!');
INSERT INTO bad_response (bad_responses) VALUES ('Le Chinois');

INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Quelle est la particularité de Python ?', '/image3.jpg', 'Langage accessible même pour débutant', 'http://127.0.0.1:5000/Rem/enigme/4', 'Mauvaise réponse !!!');
INSERT INTO bad_response (bad_responses) VALUES ('Concatène la valeur 3,14 et un poisson');

INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Quelle est la différence entre une liste et un tuple en Python ?', '/image4.jpg', 'Les listes sont mutables', 'http://127.0.0.1:5000/Rem/endpage', 'Mauvaise réponse !!!');
INSERT INTO bad_response (bad_responses) VALUES ('les listes sont définies par des parenthèses');
