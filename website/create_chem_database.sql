
CREATE DATABASE chemistry;

USE chemistry;

CREATE TABLE Chemicals (
    chemical_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    formula VARCHAR(255) NOT NULL,
    state VARCHAR(50)
);

CREATE TABLE Reactions (
    reaction_id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    temperature DECIMAL(5,2),
    pressure DECIMAL(5,2)
);

CREATE TABLE ReactionDetails (
    reaction_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    reaction_id INT,
    chemical_id INT,
    role ENUM('reactant', 'product'),
    FOREIGN KEY (reaction_id) REFERENCES Reactions(reaction_id),
    FOREIGN KEY (chemical_id) REFERENCES Chemicals(chemical_id)
);
