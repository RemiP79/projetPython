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

CREATE TABLE bad_response (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bad_responses TEXT NOT NULL --Stokage under json possible
);

CREATE TABLE enigma_bad_response (
    enigma_id INTEGER,
    bad_response_id INTEGER,
    FOREIGN KEY (enigma_id) REFERENCES enigma(id),
    FOREIGN KEY (bad_response_id) REFERENCES bad_response(id),
    PRIMARY KEY (enigma_id, bad_response_id)
);

INSERT INTO user (email, username, password) VALUES ('monmail@ngft.com', 'Rem', 'monmotdepasse');
INSERT INTO enigma (title, image_url, good_response, link_good_response, Message_bad_response) VALUES ('Énigme 1', '/image1.jpg', 'Bonne réponse 1', 'lien1', 'Mauvaise réponse 1');
INSERT INTO bad_response (bad_responses) VALUES ('Mauvaise réponse 1');
INSERT INTO enigma_bad_response (enigma_id, bad_response_id) VALUES (1, 1);