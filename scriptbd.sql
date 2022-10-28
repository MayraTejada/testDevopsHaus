CREATE DATABASE mydatabasehaus;

CREATE TABLE clients(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80),
    money INT
);

DROP TABLE clients