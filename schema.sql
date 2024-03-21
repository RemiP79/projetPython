DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `enigma`;
DROP TABLE IF EXISTS `bad_response`;

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
    link_good_response TEXT NOT NULL,
    Message_bad_response TEXT NOT NULL DEFAULT 'Mauvaise réponse ! !' --For future use: Customization of the response 
);

--Create a table for storing multiple bad responses in the future. 
--will use Storage in JSON format
CREATE TABLE bad_response (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bad_responses TEXT NOT NULL, 
    enigma_id INTEGER,
    FOREIGN KEY (enigma_id) REFERENCES enigma(enigma_id)
);

INSERT INTO user (email, username, password) VALUES ('monmail@ngft.com', 'Rem', 'monmotdepasse');

INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Qui est le plus grand fan de python ?', '/image1.jpg', 'Guillaume', 'http://127.0.0.1:5000/Rem/enigme/2', 'Mauvaise réponse mon ami  !!!');
INSERT INTO bad_response (bad_responses, enigma_id) VALUES ('Professeur Tournesol', 1);

INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Quel est le meilleur langage de développement ?', '/image2.jpg', 'Le Python', 'http://127.0.0.1:5000/Rem/enigme/3', 'Mauvaise réponse !!!');
INSERT INTO bad_response (bad_responses, enigma_id) VALUES ('Le Chinois', 2);

INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Quelle est la particularité de Python ?', '/image3.jpg', 'Langage accessible même pour débutant', 'http://127.0.0.1:5000/Rem/enigme/4', 'Mauvaise réponse !!!');
INSERT INTO bad_response (bad_responses, enigma_id) VALUES ('Concatène la valeur 3,14 et un poisson', 3);

INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Quelle est la différence entre une liste et un tuple en Python ?', '/image4.jpg', 'Les listes sont mutables', 'http://127.0.0.1:5000/Rem/endpage', 'Mauvaise réponse !!!');
INSERT INTO bad_response (bad_responses, enigma_id) VALUES ('les listes sont définies par des parenthèses', 4);
