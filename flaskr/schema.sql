DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `enigma`;
DROP TABLE IF EXISTS `bad_response`;
DROP TABLE IF EXISTS `enigma_bad_response`;

CREATE TABLE user (
    id INT PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
);

CREATE TABLE enigma(
    id INT PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE NOT NULL,
    image TEXT,    
    good_response TEXT NOT NULL,   
    link_good_response TEXT NOT NULL,
    Message_bad_response TEXT NOT NULL,
)

CREAT TABLE bad_response(
    id INT PRIMARY KEY AUTOINCREMENT,
    bad_responses TEXT NOT NULL, --Stokage under json possible    
)

CREATE TABLE enigma_bad_response (
    enigma_id INT,
    bad_response_id INT,
    FOREIGN KEY (enigma_id) REFERENCES enigma(id),
    FOREIGN KEY (bad_response_id) REFERENCES bad_response(id),
    PRIMARY KEY (enigma_id, bad_response_id)
);

