import sqlite3 as sql

# --- Conexão com o banco de dados ---
# Garanta que o arquivo 'banco.db' já foi criado com as tabelas do primeiro script.
conn = sql.connect('banco.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

print("Iniciando o povoamento massivo e detalhado do banco de dados...")

try:
    # =================================================================
    # ||                  DADOS BÁSICOS (LOOKUP)                     ||
    # =================================================================

    # --- TREINADOR (30 no total) ---
    print("Inserindo 30 treinadores...")
    # 10 Treinadores Nomeados
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (1, 'Ash Ketchum');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (2, 'Misty');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (3, 'Brock');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (4, 'Gary Oak');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (5, 'Red');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (6, 'Blue');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (7, 'Erika');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (8, 'Lt. Surge');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (9, 'Sabrina');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (10, 'Giovanni');")
    # 20 Treinadores Genéricos
    for i in range(11, 31):
        cursor.execute(f"INSERT INTO treinador (id, nome) VALUES ({i}, 'Treinador_{i}');")
    # Professores
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (100, 'Professor Oak');")
    cursor.execute("INSERT INTO treinador (id, nome) VALUES (101, 'Professor Elm');")

    # --- PROFESSOR (Subtipo de Treinador) ---
    cursor.execute("INSERT INTO professor (id, area_de_pesquisa) VALUES (100, 'Biologia Pokémon');")
    cursor.execute("INSERT INTO professor (id, area_de_pesquisa) VALUES (101, 'Criação e Ovos Pokémon');")

    # --- LIDER (Subtipo de Treinador) ---
    cursor.execute("INSERT INTO lider (id) VALUES (2);")  # Misty
    cursor.execute("INSERT INTO lider (id) VALUES (3);")  # Brock
    cursor.execute("INSERT INTO lider (id) VALUES (7);")  # Erika
    cursor.execute("INSERT INTO lider (id) VALUES (8);")  # Lt. Surge
    cursor.execute("INSERT INTO lider (id) VALUES (9);")  # Sabrina
    cursor.execute("INSERT INTO lider (id) VALUES (10);") # Giovanni

    # --- ITEM (30 no total) ---
    print("Inserindo 30 itens...")
    items = [
        'Potion', 'Super Potion', 'Hyper Potion', 'Max Potion', 'Full Heal', 'Revive', 'Max Revive',
        'Poké Ball', 'Great Ball', 'Ultra Ball', 'Master Ball',
        'Thunder Stone', 'Water Stone', 'Fire Stone', 'Leaf Stone', 'Moon Stone',
        'Nugget', 'Rare Candy', 'Escape Rope', 'Repel', 'Super Repel',
        'TM01 - Mega Punch', 'TM13 - Ice Beam', 'TM26 - Earthquake', 'TM38 - Fire Blast',
        'HM01 - Cut', 'HM03 - Surf',
        'Boulder Badge', 'Cascade Badge', 'Thunder Badge', 'Rainbow Badge', 'Soul Badge', 'Marsh Badge', 'Volcano Badge', 'Earth Badge'
    ]
    for item in items:
        cursor.execute("INSERT INTO item (nome) VALUES (?);", (item,))

    # --- MOVIMENTO (30 no total) ---
    print("Inserindo 30 movimentos...")
    moves = [
        ('Thunderbolt', 'Elétrico'), ('Quick Attack', 'Normal'), ('Vine Whip', 'Planta'),
        ('Flamethrower', 'Fogo'), ('Water Gun', 'Água'), ('Rock Tomb', 'Rocha'),
        ('Solar Beam', 'Planta'), ('Psychic', 'Psíquico'), ('Tackle', 'Normal'),
        ('Aqua Tail', 'Água'), ('Wing Attack', 'Voador'), ('Teleport', 'Psíquico'),
        ('Bite', 'Sombrio'), ('Body Slam', 'Normal'), ('Hyper Beam', 'Normal'),
        ('Earthquake', 'Terra'), ('Ice Beam', 'Gelo'), ('Thunder Wave', 'Elétrico'),
        ('Sleep Powder', 'Planta'), ('Toxic', 'Veneno'), ('Swords Dance', 'Normal'),
        ('Agility', 'Psíquico'), ('Recover', 'Normal'), ('Surf', 'Água'),
        ('Cut', 'Normal'), ('Strength', 'Normal'), ('Hydro Pump', 'Água'),
        ('Fire Blast', 'Fogo'), ('Double Kick', 'Lutador'), ('Mega Drain', 'Planta'),
        ('Rock Throw', 'Rocha'), ('Psybeam', 'Psíquico'), ('Iron Tail', 'Aço'),
        ('Seismic Toss', 'Lutador'), ('Skull Bash', 'Normal'), ('Mega Punch', 'Normal')
    ]
    for move in moves:
        cursor.execute("INSERT INTO movimento (nome, tipo) VALUES (?, ?);", move)
        
    # =================================================================
    # ||            POKÉDEX COMPLETA - 1ª GERAÇÃO (151)              ||
    # =================================================================
    print("Inserindo as 151 espécies da Geração 1...")
    especies_gen1 = [
        (1, 'Bulbasaur', None, None, 'Planta', 'Veneno'), (2, 'Ivysaur', 1, 'Level 16', 'Planta', 'Veneno'),
        (3, 'Venusaur', 2, 'Level 32', 'Planta', 'Veneno'), (4, 'Charmander', None, None, 'Fogo', None),
        (5, 'Charmeleon', 4, 'Level 16', 'Fogo', None), (6, 'Charizard', 5, 'Level 36', 'Fogo', 'Voador'),
        (7, 'Squirtle', None, None, 'Água', None), (8, 'Wartortle', 7, 'Level 16', 'Água', None),
        (9, 'Blastoise', 8, 'Level 36', 'Água', None), (10, 'Caterpie', None, None, 'Inseto', None),
        (11, 'Metapod', 10, 'Level 7', 'Inseto', None), (12, 'Butterfree', 11, 'Level 10', 'Inseto', 'Voador'),
        (13, 'Weedle', None, None, 'Inseto', 'Veneno'), (14, 'Kakuna', 13, 'Level 7', 'Inseto', 'Veneno'),
        (15, 'Beedrill', 14, 'Level 10', 'Inseto', 'Veneno'), (16, 'Pidgey', None, None, 'Normal', 'Voador'),
        (17, 'Pidgeotto', 16, 'Level 18', 'Normal', 'Voador'), (18, 'Pidgeot', 17, 'Level 36', 'Normal', 'Voador'),
        (19, 'Rattata', None, None, 'Normal', None), (20, 'Raticate', 19, 'Level 20', 'Normal', None),
        (21, 'Spearow', None, None, 'Normal', 'Voador'), (22, 'Fearow', 21, 'Level 20', 'Normal', 'Voador'),
        (23, 'Ekans', None, None, 'Veneno', None), (24, 'Arbok', 23, 'Level 22', 'Veneno', None),
        (25, 'Pikachu', None, None, 'Elétrico', None), (26, 'Raichu', 25, 'Thunder Stone', 'Elétrico', None),
        (27, 'Sandshrew', None, None, 'Terra', None), (28, 'Sandslash', 27, 'Level 22', 'Terra', None),
        (29, 'Nidoran♀', None, None, 'Veneno', None), (30, 'Nidorina', 29, 'Level 16', 'Veneno', None),
        (31, 'Nidoqueen', 30, 'Moon Stone', 'Veneno', 'Terra'), (32, 'Nidoran♂', None, None, 'Veneno', None),
        (33, 'Nidorino', 32, 'Level 16', 'Veneno', None), (34, 'Nidoking', 33, 'Moon Stone', 'Veneno', 'Terra'),
        (35, 'Clefairy', None, None, 'Fada', None), (36, 'Clefable', 35, 'Moon Stone', 'Fada', None),
        (37, 'Vulpix', None, None, 'Fogo', None), (38, 'Ninetales', 37, 'Fire Stone', 'Fogo', None),
        (39, 'Jigglypuff', None, None, 'Normal', 'Fada'), (40, 'Wigglytuff', 39, 'Moon Stone', 'Normal', 'Fada'),
        (41, 'Zubat', None, None, 'Veneno', 'Voador'), (42, 'Golbat', 41, 'Level 22', 'Veneno', 'Voador'),
        (43, 'Oddish', None, None, 'Planta', 'Veneno'), (44, 'Gloom', 43, 'Level 21', 'Planta', 'Veneno'),
        (45, 'Vileplume', 44, 'Leaf Stone', 'Planta', 'Veneno'), (46, 'Paras', None, None, 'Inseto', 'Planta'),
        (47, 'Parasect', 46, 'Level 24', 'Inseto', 'Planta'), (48, 'Venonat', None, None, 'Inseto', 'Veneno'),
        (49, 'Venomoth', 48, 'Level 31', 'Inseto', 'Veneno'), (50, 'Diglett', None, None, 'Terra', None),
        (51, 'Dugtrio', 50, 'Level 26', 'Terra', None), (52, 'Meowth', None, None, 'Normal', None),
        (53, 'Persian', 52, 'Level 28', 'Normal', None), (54, 'Psyduck', None, None, 'Água', None),
        (55, 'Golduck', 54, 'Level 33', 'Água', None), (56, 'Mankey', None, None, 'Lutador', None),
        (57, 'Primeape', 56, 'Level 28', 'Lutador', None), (58, 'Growlithe', None, None, 'Fogo', None),
        (59, 'Arcanine', 58, 'Fire Stone', 'Fogo', None), (60, 'Poliwag', None, None, 'Água', None),
        (61, 'Poliwhirl', 60, 'Level 25', 'Água', None), (62, 'Poliwrath', 61, 'Water Stone', 'Água', 'Lutador'),
        (63, 'Abra', None, None, 'Psíquico', None), (64, 'Kadabra', 63, 'Level 16', 'Psíquico', None),
        (65, 'Alakazam', 64, 'Trade', 'Psíquico', None), (66, 'Machop', None, None, 'Lutador', None),
        (67, 'Machoke', 66, 'Level 28', 'Lutador', None), (68, 'Machamp', 67, 'Trade', 'Lutador', None),
        (69, 'Bellsprout', None, None, 'Planta', 'Veneno'), (70, 'Weepinbell', 69, 'Level 21', 'Planta', 'Veneno'),
        (71, 'Victreebel', 70, 'Leaf Stone', 'Planta', 'Veneno'), (72, 'Tentacool', None, None, 'Água', 'Veneno'),
        (73, 'Tentacruel', 72, 'Level 30', 'Água', 'Veneno'), (74, 'Geodude', None, None, 'Rocha', 'Terra'),
        (75, 'Graveler', 74, 'Level 25', 'Rocha', 'Terra'), (76, 'Golem', 75, 'Trade', 'Rocha', 'Terra'),
        (77, 'Ponyta', None, None, 'Fogo', None), (78, 'Rapidash', 77, 'Level 40', 'Fogo', None),
        (79, 'Slowpoke', None, None, 'Água', 'Psíquico'), (80, 'Slowbro', 79, 'Level 37', 'Água', 'Psíquico'),
        (81, 'Magnemite', None, None, 'Elétrico', 'Aço'), (82, 'Magneton', 81, 'Level 30', 'Elétrico', 'Aço'),
        (83, "Farfetch'd", None, None, 'Normal', 'Voador'), (84, 'Doduo', None, None, 'Normal', 'Voador'),
        (85, 'Dodrio', 84, 'Level 31', 'Normal', 'Voador'), (86, 'Seel', None, None, 'Água', None),
        (87, 'Dewgong', 86, 'Level 34', 'Água', 'Gelo'), (88, 'Grimer', None, None, 'Veneno', None),
        (89, 'Muk', 88, 'Level 38', 'Veneno', None), (90, 'Shellder', None, None, 'Água', None),
        (91, 'Cloyster', 90, 'Water Stone', 'Água', 'Gelo'), (92, 'Gastly', None, None, 'Fantasma', 'Veneno'),
        (93, 'Haunter', 92, 'Level 25', 'Fantasma', 'Veneno'), (94, 'Gengar', 93, 'Trade', 'Fantasma', 'Veneno'),
        (95, 'Onix', None, None, 'Rocha', 'Terra'), (96, 'Drowzee', None, None, 'Psíquico', None),
        (97, 'Hypno', 96, 'Level 26', 'Psíquico', None), (98, 'Krabby', None, None, 'Água', None),
        (99, 'Kingler', 98, 'Level 28', 'Água', None), (100, 'Voltorb', None, None, 'Elétrico', None),
        (101, 'Electrode', 100, 'Level 30', 'Elétrico', None), (102, 'Exeggcute', None, None, 'Planta', 'Psíquico'),
        (103, 'Exeggutor', 102, 'Leaf Stone', 'Planta', 'Psíquico'), (104, 'Cubone', None, None, 'Terra', None),
        (105, 'Marowak', 104, 'Level 28', 'Terra', None), (106, 'Hitmonlee', None, None, 'Lutador', None),
        (107, 'Hitmonchan', None, None, 'Lutador', None), (108, 'Lickitung', None, None, 'Normal', None),
        (109, 'Koffing', None, None, 'Veneno', None), (110, 'Weezing', 109, 'Level 35', 'Veneno', None),
        (111, 'Rhyhorn', None, None, 'Rocha', 'Terra'), (112, 'Rhydon', 111, 'Level 42', 'Rocha', 'Terra'),
        (113, 'Chansey', None, None, 'Normal', None), (114, 'Tangela', None, None, 'Planta', None),
        (115, 'Kangaskhan', None, None, 'Normal', None), (116, 'Horsea', None, None, 'Água', None),
        (117, 'Seadra', 116, 'Level 32', 'Água', None), (118, 'Goldeen', None, None, 'Água', None),
        (119, 'Seaking', 118, 'Level 33', 'Água', None), (120, 'Staryu', None, None, 'Água', None),
        (121, 'Starmie', 120, 'Water Stone', 'Água', 'Psíquico'), (122, 'Mr. Mime', None, None, 'Psíquico', 'Fada'),
        (123, 'Scyther', None, None, 'Inseto', 'Voador'), (124, 'Jynx', None, None, 'Gelo', 'Psíquico'),
        (125, 'Electabuzz', None, None, 'Elétrico', None), (126, 'Magmar', None, None, 'Fogo', None),
        (127, 'Pinsir', None, None, 'Inseto', None), (128, 'Tauros', None, None, 'Normal', None),
        (129, 'Magikarp', None, None, 'Água', None), (130, 'Gyarados', 129, 'Level 20', 'Água', 'Voador'),
        (131, 'Lapras', None, None, 'Água', 'Gelo'), (132, 'Ditto', None, None, 'Normal', None),
        (133, 'Eevee', None, None, 'Normal', None), (134, 'Vaporeon', 133, 'Water Stone', 'Água', None),
        (135, 'Jolteon', 133, 'Thunder Stone', 'Elétrico', None), (136, 'Flareon', 133, 'Fire Stone', 'Fogo', None),
        (137, 'Porygon', None, None, 'Normal', None), (138, 'Omanyte', None, None, 'Rocha', 'Água'),
        (139, 'Omastar', 138, 'Level 40', 'Rocha', 'Água'), (140, 'Kabuto', None, None, 'Rocha', 'Água'),
        (141, 'Kabutops', 140, 'Level 40', 'Rocha', 'Água'), (142, 'Aerodactyl', None, None, 'Rocha', 'Voador'),
        (143, 'Snorlax', None, None, 'Normal', None), (144, 'Articuno', None, None, 'Gelo', 'Voador'),
        (145, 'Zapdos', None, None, 'Elétrico', 'Voador'), (146, 'Moltres', None, None, 'Fogo', 'Voador'),
        (147, 'Dratini', None, None, 'Dragão', None), (148, 'Dragonair', 147, 'Level 30', 'Dragão', None),
        (149, 'Dragonite', 148, 'Level 55', 'Dragão', 'Voador'), (150, 'Mewtwo', None, None, 'Psíquico', None),
        (151, 'Mew', None, None, 'Psíquico', None)
    ]
    cursor.executemany("INSERT INTO especie (numero, nome, pre_evolucao, pre_requisito, tipo1, tipo2) VALUES (?, ?, ?, ?, ?, ?);", especies_gen1)

    # =================================================================
    # ||             DADOS RELACIONAIS E DE INSTÂNCIAS               ||
    # =================================================================

    # --- GINASIO ---
    print("Inserindo ginásios...")
    cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Pewter', 'Pewter Gym', 'Rocha', 3);")
    cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Cerulean', 'Cerulean Gym', 'Água', 2);")
    cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Vermilion', 'Vermilion Gym', 'Elétrico', 8);")
    cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Celadon', 'Celadon Gym', 'Planta', 7);")
    cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Saffron', 'Saffron Gym', 'Psíquico', 9);")
    cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Viridian', 'Viridian Gym', 'Terra', 10);")
    
    # --- POKEMON (Instâncias individuais) ---
    print("Criando instâncias de Pokémon para treinadores e como selvagens...")
    # --- Equipe de Ash Ketchum (id: 1) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (25, 1, 1);")  # Pikachu #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (6, 1, 1);")   # Charizard #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (9, 1, 1);")   # Blastoise #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (3, 1, 1);")   # Venusaur #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (18, 1, 1);")  # Pidgeot #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (131, 1, 1);") # Lapras #1
    
    # --- Equipe de Misty (id: 2) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (121, 1, 2);") # Starmie #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (54, 1, 2);")  # Psyduck #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (118, 1, 2);") # Goldeen #1
    
    # --- Equipe de Brock (id: 3) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (95, 1, 3);")  # Onix #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (74, 1, 3);")  # Geodude #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (37, 1, 3);")  # Vulpix #1
    
    # --- Equipe de Gary Oak (id: 4) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (9, 2, 4);")   # Blastoise #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (59, 1, 4);")  # Arcanine #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (65, 1, 4);")  # Alakazam #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (18, 2, 4);")  # Pidgeot #2
    
    # --- Equipe de Red (id: 5) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (3, 2, 5);")   # Venusaur #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (25, 2, 5);")  # Pikachu #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (143, 1, 5);") # Snorlax #1
    
    # --- Equipe de Blue (id: 6) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (6, 2, 6);")   # Charizard #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (112, 1, 6);") # Rhydon #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (103, 1, 6);") # Exeggutor #1
    
    # --- Equipe de Erika (id: 7) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (45, 1, 7);")  # Vileplume #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (114, 1, 7);") # Tangela #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (71, 1, 7);")  # Victreebel #1
    
    # --- Equipe de Lt. Surge (id: 8) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (26, 1, 8);")  # Raichu #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (101, 1, 8);") # Electrode #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (82, 1, 8);")  # Magneton #1
    
    # --- Equipe de Sabrina (id: 9) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (65, 2, 9);")  # Alakazam #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (49, 1, 9);")  # Venomoth #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (122, 1, 9);") # Mr. Mime #1
    
    # --- Equipe de Giovanni (id: 10) ---
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (53, 1, 10);") # Persian #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (34, 1, 10);") # Nidoking #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (112, 2, 10);")# Rhydon #2
    
   # --- Equipes Variadas e Completas para Treinadores Genéricos (11-30) ---
    print("Criando times variados para os 20 treinadores genéricos...")
    # Treinador 11
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (27, 1, 11);") # Sandshrew #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (23, 1, 11);") # Ekans #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (56, 1, 11);") # Mankey #1
    # Treinador 12
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (58, 1, 12);") # Growlithe #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (66, 1, 12);") # Machop #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (69, 1, 12);") # Bellsprout #1
    # Treinador 13
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (72, 1, 13);") # Tentacool #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (77, 1, 13);") # Ponyta #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (79, 1, 13);") # Slowpoke #1
    # Treinador 14
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (84, 1, 14);") # Doduo #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (86, 1, 14);") # Seel #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (88, 1, 14);") # Grimer #1
    # Treinador 15
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (90, 1, 15);") # Shellder #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (96, 1, 15);") # Drowzee #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (98, 1, 15);") # Krabby #1
    # Treinador 16
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (100, 1, 16);")# Voltorb #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (104, 1, 16);")# Cubone #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (109, 1, 16);")# Koffing #1
    # Treinador 17
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (111, 1, 17);")# Rhyhorn #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (116, 1, 17);")# Horsea #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (118, 2, 17);")# Goldeen #2
    # Treinador 18
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (21, 1, 18);") # Spearow #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (43, 1, 18);") # Oddish #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (46, 1, 18);") # Paras #1
    # Treinador 19
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (20, 1, 19);") # Raticate #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (22, 1, 19);") # Fearow #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (41, 1, 19);") # Zubat #1
    # Treinador 20
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (48, 1, 20);") # Venonat #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (50, 1, 20);") # Diglett #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (52, 1, 20);") # Meowth #1
    # Treinador 21
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (60, 1, 21);") # Poliwag #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (63, 1, 21);") # Abra #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (129, 1, 21);")# Magikarp #1
    # Treinador 22
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (39, 1, 22);") # Jigglypuff #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (133, 1, 22);")# Eevee #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (137, 1, 22);")# Porygon #1
    # Treinador 23
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (127, 1, 23);")# Pinsir #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (123, 1, 23);")# Scyther #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (128, 1, 23);")# Tauros #1
    # Treinador 24
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (108, 1, 24);")# Lickitung #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (113, 1, 24);")# Chansey #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (115, 1, 24);")# Kangaskhan #1
    # Treinador 25
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (106, 1, 25);")# Hitmonlee #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (107, 1, 25);")# Hitmonchan #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (57, 1, 25);") # Primeape #1
    # Treinador 26
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (138, 1, 26);")# Omanyte #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (140, 1, 26);")# Kabuto #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (142, 1, 26);")# Aerodactyl #1
    # Treinador 27
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (124, 1, 27);")# Jynx #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (125, 1, 27);")# Electabuzz #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (126, 1, 27);")# Magmar #1
    # Treinador 28
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (31, 1, 28);") # Nidoqueen #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (34, 2, 28);") # Nidoking #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (112, 3, 28);")# Rhydon #3
    # Treinador 29
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (134, 1, 29);")# Vaporeon #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (135, 1, 29);")# Jolteon #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (136, 1, 29);")# Flareon #1
    # Treinador 30
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (147, 1, 30);")# Dratini #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (148, 1, 30);")# Dragonair #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (149, 1, 30);")# Dragonite #1

    # --- 40 Pokémon Selvagens (Lista Completa) ---
    print("Criando as 40 instâncias de Pokémon selvagens...")
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (16, 1, 'Route 1', 'Kanto');")        # Pidgey #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (16, 2, 'Route 1', 'Kanto');")        # Pidgey #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (19, 1, 'Route 1', 'Kanto');")        # Rattata #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (19, 2, 'Route 1', 'Kanto');")        # Rattata #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (10, 1, 'Viridian Forest', 'Kanto');")# Caterpie #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (13, 1, 'Viridian Forest', 'Kanto');")# Weedle #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (11, 1, 'Viridian Forest', 'Kanto');")# Metapod #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (25, 3, 'Viridian Forest', 'Kanto');")# Pikachu #3 (raro)
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (74, 2, 'Mt. Moon', 'Kanto');")       # Geodude #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (74, 3, 'Mt. Moon', 'Kanto');")       # Geodude #3
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (41, 2, 'Mt. Moon', 'Kanto');")       # Zubat #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (41, 3, 'Mt. Moon', 'Kanto');")       # Zubat #3
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (46, 2, 'Mt. Moon', 'Kanto');")       # Paras #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (35, 1, 'Mt. Moon', 'Kanto');")       # Clefairy #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (27, 2, 'Route 4', 'Kanto');")       # Sandshrew #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (23, 2, 'Route 4', 'Kanto');")       # Ekans #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (72, 2, 'Route 19', 'Kanto');")       # Tentacool #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (72, 3, 'Route 19', 'Kanto');")       # Tentacool #3
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (116, 2, 'Route 19', 'Kanto');")      # Horsea #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (100, 2, 'Power Plant', 'Kanto');")   # Voltorb #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (100, 3, 'Power Plant', 'Kanto');")   # Voltorb #3
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (81, 1, 'Power Plant', 'Kanto');")    # Magnemite #1
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (88, 2, 'Power Plant', 'Kanto');")    # Grimer #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (125, 2, 'Power Plant', 'Kanto');")   # Electabuzz #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (145, 1, 'Power Plant', 'Kanto');")   # Zapdos #1 (Lendário)
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (96, 2, 'Route 11', 'Kanto');")       # Drowzee #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (21, 2, 'Route 11', 'Kanto');")       # Spearow #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (128, 2, 'Safari Zone', 'Kanto');")   # Tauros #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (115, 2, 'Safari Zone', 'Kanto');")   # Kangaskhan #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (123, 2, 'Safari Zone', 'Kanto');")   # Scyther #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (147, 2, 'Safari Zone', 'Kanto');")   # Dratini #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (86, 2, 'Seafoam Islands', 'Kanto');")# Seel #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (79, 2, 'Seafoam Islands', 'Kanto');")# Slowpoke #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (41, 4, 'Seafoam Islands', 'Kanto');")# Zubat #4
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (144, 1, 'Seafoam Islands', 'Kanto');") # Articuno #1 (Lendário)
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (77, 2, 'Cinnabar Island', 'Kanto');") # Ponyta #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (109, 2, 'Cinnabar Island', 'Kanto');") # Koffing #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (146, 1, 'Victory Road', 'Kanto');")   # Moltres #1 (Lendário)
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (66, 2, 'Victory Road', 'Kanto');")    # Machop #2
    cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (150, 1, 'Cerulean Cave', 'Kanto');") # Mewtwo #1 (Lendário)

    # =================================================================
    # ||                    MOVIMENTOS E RELAÇÕES                    ||
    # =================================================================

    # --- TEM (Movimentos Inatos/Aprendidos por Nível) ---
    print("Atribuindo movimentos inatos e canônicos...")
    # Ash Ketchum
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Thunderbolt', 1, 25);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Quick Attack', 1, 25);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Flamethrower', 1, 6);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Wing Attack', 1, 6);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Hydro Pump', 1, 9);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Vine Whip', 1, 3);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Wing Attack', 1, 18);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 131);")
    # Misty
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 121);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 121);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 54);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Psychic', 1, 54);") # Psyduck usa Psychic em momentos de estresse
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 118);")
    # Brock
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Rock Throw', 1, 95);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 74);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Flamethrower', 1, 37);")
    # Gary Oak
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Hydro Pump', 2, 9);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Bite', 2, 9);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Fire Blast', 1, 59);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Psychic', 1, 65);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Psybeam', 1, 65);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Recover', 1, 65);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Teleport', 1, 65);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Hyper Beam', 1, 65);") # Mais de 4 ataques
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Wing Attack', 2, 18);")
    # Red
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Sleep Powder', 2, 3);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Thunderbolt', 2, 25);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Body Slam', 1, 143);")
    # Blue
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Fire Blast', 2, 6);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Earthquake', 1, 112);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Psychic', 1, 103);")
    # Líderes de Ginásio
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Mega Drain', 1, 45);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Sleep Powder', 1, 114);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Thunderbolt', 1, 26);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Thunder Wave', 1, 26);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Psychic', 2, 65);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Earthquake', 2, 112);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Rock Tomb', 1, 34);")

    # --- ENSINA (Movimentos Ensinados por Treinadores) ---
    print("Atribuindo movimentos ensinados...")
    # Ash ensina
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Iron Tail', 1, 25, 1);")
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Seismic Toss', 1, 6, 1);")
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Skull Bash', 1, 9, 1);")
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Solar Beam', 1, 3, 1);")
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Surf', 1, 131, 1);")
    # Misty ensina para o Lapras de Ash
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Ice Beam', 1, 131, 2);")
    # Brock ensina para o Snorlax de Red
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Earthquake', 1, 143, 3);")
    # Gary ensina
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Ice Beam', 2, 9, 4);")
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Quick Attack', 2, 18, 4);")
    # Red ensina
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Mega Drain', 2, 3, 5);")
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Surf', 2, 25, 5);") # Pikachu surfista!
    # Blue ensina
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Swords Dance', 2, 6, 6);")
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Rock Tomb', 1, 112, 6);")

    # --- Povoamento de Movimentos para Treinadores Genéricos (ID 11-30) ---
    print("Atribuindo movimentos para os Pokémon dos 20 treinadores genéricos...")

    # --- Tabela TEM (Movimentos Inatos/Básicos para TODOS) ---
    # Cada Pokémon receberá pelo menos um movimento básico.

    # Treinador 11 (Sandshrew, Ekans, Mankey)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 27);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Bite', 1, 23);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Double Kick', 1, 56);")
    # Treinador 12 (Growlithe, Machop, Bellsprout)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Bite', 1, 58);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Double Kick', 1, 66);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Vine Whip', 1, 69);")
    # Treinador 13 (Tentacool, Ponyta, Slowpoke)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Toxic', 1, 72);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 77);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 79);")
    # Treinador 14 (Doduo, Seel, Grimer)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Quick Attack', 1, 84);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 86);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Toxic', 1, 88);")
    # Treinador 15 (Shellder, Drowzee, Krabby)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 90);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Psychic', 1, 96);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 98);")
    # Treinador 16 (Voltorb, Cubone, Koffing)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 100);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 104);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Toxic', 1, 109);")
    # Treinador 17 (Rhyhorn, Horsea, Goldeen)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Rock Tomb', 1, 111);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 116);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Aqua Tail', 2, 118);")
    # Treinador 18 (Spearow, Oddish, Paras)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Wing Attack', 1, 21);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Vine Whip', 1, 43);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Sleep Powder', 1, 46);")
    # Treinador 19 (Raticate, Fearow, Zubat)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Quick Attack', 1, 20);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Wing Attack', 1, 22);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Bite', 1, 41);")
    # Treinador 20 (Venonat, Diglett, Meowth)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Psychic', 1, 48);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 50);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Bite', 1, 52);")
    # Treinador 21 (Poliwag, Abra, Magikarp)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 60);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Teleport', 1, 63);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 129);")
    # Treinador 22 (Jigglypuff, Eevee, Porygon)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Body Slam', 1, 39);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Quick Attack', 1, 133);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 137);")
    # Treinador 23 (Pinsir, Scyther, Tauros)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 127);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Wing Attack', 1, 123);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Body Slam', 1, 128);")
    # Treinador 24 (Lickitung, Chansey, Kangaskhan)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Body Slam', 1, 108);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Double Kick', 1, 113);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Mega Punch', 1, 115);")
    # Treinador 25 (Hitmonlee, Hitmonchan, Primeape)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Double Kick', 1, 106);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Mega Punch', 1, 107);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Double Kick', 1, 57);")
    # Treinador 26 (Omanyte, Kabuto, Aerodactyl)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 138);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tackle', 1, 140);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Wing Attack', 1, 142);")
    # Treinador 27 (Jynx, Electabuzz, Magmar)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Ice Beam', 1, 124);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Thunderbolt', 1, 125);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Flamethrower', 1, 126);")
    # Treinador 28 (Nidoqueen, Nidoking, Rhydon)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Body Slam', 1, 31);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Double Kick', 2, 34);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Rock Tomb', 3, 112);")
    # Treinador 29 (Vaporeon, Jolteon, Flareon)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Water Gun', 1, 134);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Thunderbolt', 1, 135);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Flamethrower', 1, 136);")
    # Treinador 30 (Dratini, Dragonair, Dragonite)
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Bite', 1, 147);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Agility', 1, 148);")
    cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Wing Attack', 1, 149);")

    # --- Tabela ENSINA (10 Casos de Treinadores Nomeados Ensinando para Genéricos) ---
    print("Registrando interações de ensino entre treinadores nomeados e genéricos...")

    # Ash (id: 1) ensina 'Mega Punch' para o Mankey do Treinador_11
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Mega Punch', 1, 56, 1);")

    # Misty (id: 2) ensina 'Hydro Pump' para o Tentacool do Treinador_13
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Hydro Pump', 1, 72, 2);")

   # Brock (id: 3), como especialista em rochas, ensina 'Rock Tomb' para o Aerodactyl do Treinador_26
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Rock Tomb', 1, 142, 3);")

    # Gary (id: 4) ensina 'Hyper Beam' para o Krabby do Treinador_15
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Hyper Beam', 1, 98, 4);")

    # Red (id: 5) ensina 'Strength' para o Rhyhorn do Treinador_17
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Strength', 1, 111, 5);")

    # Blue (id: 6) ensina 'Swords Dance' para o Paras do Treinador_18
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Swords Dance', 1, 46, 6);")

    # Erika (id: 7) ensina 'Mega Drain' para o Oddish do mesmo Treinador_18, que a visitou
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Mega Drain', 1, 43, 7);")

    # Lt. Surge (id: 8) ensina 'Thunder Wave' para o Voltorb do Treinador_16
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Thunder Wave', 1, 100, 8);")

    # Sabrina (id: 9) ensina 'Agility' para o Meowth do Treinador_20
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Agility', 1, 52, 9);")

    # Giovanni (id: 10) ensina 'Earthquake' para o Cubone do mesmo Treinador_16
    cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Earthquake', 1, 104, 10);")

    # --- ENFRENTA (Batalhas de Ginásio) ---
    print("Registrando batalhas de ginásio expandidas...")
    # Jornada do Ash
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Pewter', 1, '2025-07-15');")    # Ash vs Brock (Derrota)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Cerulean', 1, '2025-07-22');")  # Ash vs Misty (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Vermilion', 1, '2025-07-29');") # Ash vs Lt. Surge (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Celadon', 1, '2025-08-05');")   # Ash vs Erika (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Saffron', 1, '2025-08-12');")   # Ash vs Sabrina (Derrota)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Pewter', 1, '2025-08-15');")    # Revanche Ash vs Brock (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Viridian', 1, '2025-08-20');")  # Ash vs Giovanni (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Saffron', 1, '2025-08-25');")   # Revanche Ash vs Sabrina (Vitória)
    
    # Jornada do Gary - com 4 tentativas em Viridian
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Pewter', 4, '2025-07-16');")    # Gary vs Brock (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Cerulean', 4, '2025-07-24');")  # Gary vs Misty (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Viridian', 4, '2025-08-01');")  # Gary vs Giovanni (Derrota)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Viridian', 4, '2025-08-15');")  # Gary vs Giovanni (Derrota)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Viridian', 4, '2025-08-28');")  # Gary vs Giovanni (Derrota)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Viridian', 4, '2025-09-05');")  # Gary vs Giovanni (Vitória!)

    # Jornada do Red
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Vermilion', 5, '2025-07-25');") # Red vs Lt. Surge (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Celadon', 5, '2025-08-10');")   # Red vs Erika (Derrota)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Celadon', 5, '2025-08-11');")   # Red vs Erika (Vitória)

    # Jornada da Blue - com 3 tentativas em Saffron
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Celadon', 6, '2025-07-28');")   # Blue vs Erika (Vitória)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Saffron', 6, '2025-08-14');")   # Blue vs Sabrina (Derrota)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Saffron', 6, '2025-08-21');")   # Blue vs Sabrina (Derrota)
    cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Saffron', 6, '2025-08-29');")   # Blue vs Sabrina (Vitória!)

    # --- RECEBE (Itens de Batalha) ---
    print("Registrando itens recebidos em batalhas...")
    # Recompensas do Ash
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Pewter', 1, '2025-08-15', 'Boulder Badge');") #vende na segunda vez
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Pewter', 1, '2025-08-15', 'TM01 - Mega Punch');") #vence na segunda vez
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Cerulean', 1, '2025-07-22', 'Cascade Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Vermilion', 1, '2025-07-29', 'Thunder Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Celadon', 1, '2025-08-05', 'Rainbow Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Saffron', 1, '2025-08-25', 'Marsh Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Viridian', 1, '2025-08-20', 'Earth Badge');")
    
    # Recompensas do Gary (recebe a insígnia apenas na última data)
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Pewter', 4, '2025-07-16', 'Boulder Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Cerulean', 4, '2025-07-24', 'Cascade Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Cerulean', 4, '2025-07-24', 'Water Stone');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Viridian', 4, '2025-09-05', 'Earth Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Viridian', 4, '2025-09-05', 'Max Revive');") # Uma recompensa extra pela persistência

    # Recompensas do Red
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Vermilion', 5, '2025-07-25', 'Thunder Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Vermilion', 5, '2025-07-25', 'Thunder Stone');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Celadon', 5, '2025-08-11', 'Rainbow Badge');")

    # Recompensas da Blue (recebe a insígnia apenas na última data)
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Celadon', 6, '2025-07-28', 'Rainbow Badge');")
    cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Saffron', 6, '2025-08-29', 'Marsh Badge');")

    # --- Finalizar Transação e Fechar Conexão ---
    conn.commit()
    print("\nPovoamento massivo e detalhado concluído com sucesso!")

except sql.Error as e:
    print(f"\nOcorreu um erro ao popular o banco de dados: {e}")
    print("As alterações serão revertidas (rollback).")
    conn.rollback()

finally:
    if conn:
        conn.close()
        print("Conexão com o banco de dados fechada.")
