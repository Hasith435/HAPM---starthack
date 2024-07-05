INSERT INTO Chemicals (name, formula, state) VALUES ('Water', 'H2O', 'liquid');
INSERT INTO Chemicals (name, formula, state) VALUES ('Hydrogen', 'H2', 'gas');
INSERT INTO Chemicals (name, formula, state) VALUES ('Oxygen', 'O2', 'gas');

-- Insert reactions
INSERT INTO Reactions (description, temperature, pressure) VALUES ('Hydrogen and oxygen react to form water.', 25, 1);

-- Insert reaction details (reactants and products)
INSERT INTO ReactionDetails (reaction_id, chemical_id, role) VALUES (1, 2, 'reactant');  -- Hydrogen
INSERT INTO ReactionDetails (reaction_id, chemical_id, role) VALUES (1, 3, 'reactant');  -- Oxygen
INSERT INTO ReactionDetails (reaction_id, chemical_id, role) VALUES (1, 1, 'product');   -- Water