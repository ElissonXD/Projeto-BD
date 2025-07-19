import sqlite3 as sql


conn = sql.connect('banco.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# =================================================================
# ||                   POPULAÇÃO DO BANCO DE DADOS               ||
# =================================================================

print("Populando o banco de dados...")

# --- TREINADOR ---
cursor.execute("INSERT INTO treinador (id, nome) VALUES (1, 'Ash Ketchum');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (2, 'Misty');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (3, 'Brock');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (4, 'Giovanni');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (5, 'Gary Carvalho');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (6, 'May');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (7, 'Cynthia');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (10, 'Red');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (11, 'Lt. Surge');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (12, 'Erika');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (13, 'Sabrina');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (100, 'Professor Carvalho');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (101, 'Professor Elm');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (102, 'Professor Birch');")

# --- PROFESSOR (Subtipo de Treinador) ---
cursor.execute("INSERT INTO professor (id, area_de_pesquisa) VALUES (100, 'Biologia Pokémon');")
cursor.execute("INSERT INTO professor (id, area_de_pesquisa) VALUES (101, 'Criação e Ovos Pokémon');")
cursor.execute("INSERT INTO professor (id, area_de_pesquisa) VALUES (102, 'Habitats Pokémon');")

# --- LIDER (Subtipo de Treinador) ---
cursor.execute("INSERT INTO lider (id) VALUES (2);")
cursor.execute("INSERT INTO lider (id) VALUES (3);")
cursor.execute("INSERT INTO lider (id) VALUES (4);")
cursor.execute("INSERT INTO lider (id) VALUES (11);")
cursor.execute("INSERT INTO lider (id) VALUES (12);")
cursor.execute("INSERT INTO lider (id) VALUES (13);")

# --- ITEM ---
cursor.execute("INSERT INTO item (nome) VALUES ('Poção');")
cursor.execute("INSERT INTO item (nome) VALUES ('Super Poção');")
cursor.execute("INSERT INTO item (nome) VALUES ('Pedra do Trovão');")
cursor.execute("INSERT INTO item (nome) VALUES ('Pedra da Água');")
cursor.execute("INSERT INTO item (nome) VALUES ('Pedra da Folha');")
cursor.execute("INSERT INTO item (nome) VALUES ('Insígnia da Rocha');")
cursor.execute("INSERT INTO item (nome) VALUES ('Insígnia da Cascata');")
cursor.execute("INSERT INTO item (nome) VALUES ('Insígnia do Trovão');")
cursor.execute("INSERT INTO item (nome) VALUES ('TM34 - Onda Tóxica');")
cursor.execute("INSERT INTO item (nome) VALUES ('TM09 - Raio Solar');")

# --- MOVIMENTO ---
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Choque do Trovão', 'Elétrico');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Ataque Rápido', 'Normal');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Chicote de Vinha', 'Grama');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Lança-Chamas', 'Fogo');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Jato de Água', 'Água');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Tumba de Rochas', 'Pedra');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Raio Solar', 'Grama');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Psíquico', 'Psíquico');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Investida', 'Normal');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Cauda de Água', 'Água');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Ataque de Asa', 'Voador');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Teletransporte', 'Psíquico');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Mordida', 'Sombrio');")

# --- ESPÉCIE ---
cursor.execute("INSERT INTO especie (numero, nome, tipo1, tipo2) VALUES (1, 'Bulbasaur', 'Grama', 'Veneno');")
cursor.execute("INSERT INTO especie (numero, nome, pre_evolucao, tipo1, tipo2) VALUES (2, 'Ivysaur', 1, 'Grama', 'Veneno');")
cursor.execute("INSERT INTO especie (numero, nome, tipo1) VALUES (4, 'Charmander', 'Fogo');")
cursor.execute("INSERT INTO especie (numero, nome, tipo1) VALUES (7, 'Squirtle', 'Água');")
cursor.execute("INSERT INTO especie (numero, nome, tipo1) VALUES (10, 'Caterpie', 'Inseto');")
cursor.execute("INSERT INTO especie (numero, nome, pre_evolucao, tipo1) VALUES (11, 'Metapod', 10, 'Inseto');")
cursor.execute("INSERT INTO especie (numero, nome, tipo1, tipo2) VALUES (16, 'Pidgey', 'Normal', 'Voador');")
cursor.execute("INSERT INTO especie (numero, nome, pre_evolucao, tipo1, tipo2) VALUES (17, 'Pidgeotto', 16, 'Normal', 'Voador');")
cursor.execute("INSERT INTO especie (numero, nome, tipo1) VALUES (25, 'Pikachu', 'Elétrico');")
cursor.execute("INSERT INTO especie (numero, nome, pre_evolucao, pre_requisito, tipo1) VALUES (26, 'Raichu', 25, 'Pedra do Trovão', 'Elétrico');")
cursor.execute("INSERT INTO especie (numero, nome, tipo1) VALUES (63, 'Abra', 'Psíquico');")
cursor.execute("INSERT INTO especie (numero, nome, pre_evolucao, tipo1) VALUES (64, 'Kadabra', 63, 'Psíquico');")
cursor.execute("INSERT INTO especie (numero, nome, tipo1, tipo2) VALUES (95, 'Onix', 'Pedra', 'Terrestre');")
cursor.execute("INSERT INTO especie (numero, nome, tipo1) VALUES (133, 'Eevee', 'Normal');")
cursor.execute("INSERT INTO especie (numero, nome, pre_evolucao, pre_requisito, tipo1) VALUES (134, 'Vaporeon', 133, 'Pedra da Água', 'Água');")
cursor.execute("INSERT INTO especie (numero, nome, pre_evolucao, pre_requisito, tipo1) VALUES (136, 'Jolteon', 133, 'Pedra do Trovão', 'Elétrico');")

# --- GINASIO ---
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Pewter', 'Ginásio de Pewter', 'Pedra', 3);")
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Cerulean', 'Ginásio de Cerulean', 'Água', 2);")
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Viridian', 'Ginásio de Viridian', 'Terrestre', 4);")
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Vermilion', 'Ginásio de Vermilion', 'Elétrico', 11);")
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Celadon', 'Ginásio de Celadon', 'Grama', 12);")
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Saffron', 'Ginásio de Saffron', 'Psíquico', 13);")

# --- POKEMON ---
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (25, 1, 1);")    # Pikachu do Ash
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (4, 1, 1);")     # Charmander do Ash
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (7, 1, 2);")     # Squirtle da Misty
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (95, 1, 3);")    # Onix do Brock
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (133, 5, 5);")   # Eevee do Gary
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (16, 5, 5);")    # Pidgey do Gary
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (7, 6, 6);")     # Squirtle da May
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (1, 10, 10);")   # Bulbasaur do Red
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (63, 13, 13);")   # Abra da Sabrina
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (1, 101, 'Rota 1', 'Kanto');")
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (10, 102, 'Floresta de Viridian', 'Kanto');")
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (16, 103, 'Rota 2', 'Kanto');")
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (63, 104, 'Rota 24', 'Kanto');")

# --- TEM (Movimentos Inatos) ---
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Choque do Trovão', 1, 25);")
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Ataque Rápido', 1, 25);")
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tumba de Rochas', 1, 95);")
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Investida', 5, 133);")
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Ataque de Asa', 5, 16);")
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Jato de Água', 6, 7);")
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Teletransporte', 13, 63);")
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Chicote de Vinha', 101, 1);")
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Mordida', 102, 10);")

# --- ENSINA (Movimentos Ensinados) ---
cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Lança-Chamas', 1, 4, 1);")
cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Cauda de Água', 6, 7, 6);")
cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Psíquico', 13, 63, 13);")

# --- ENFRENTA (Batalhas de Ginásio) ---
cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Pewter', 1, '2025-07-15');")
cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Cerulean', 10, '2025-07-16');")
cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Pewter', 5, '2025-07-20');")
cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Cerulean', 1, '2025-07-22');")
cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Vermilion', 10, '2025-07-25');")
cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Celadon', 6, '2025-07-28');")

# --- RECEBE (Itens de Batalha) ---
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Pewter', 1, '2025-07-15', 'Insígnia da Rocha');")
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Pewter', 1, '2025-07-15', 'Poção');")
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Pewter', 5, '2025-07-20', 'Insígnia da Rocha');")
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Cerulean', 1, '2025-07-22', 'Insígnia da Cascata');")
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Vermilion', 10, '2025-07-25', 'Insígnia do Trovão');")
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Celadon', 6, '2025-07-28', 'Super Poção');")
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Celadon', 6, '2025-07-28', 'TM09 - Raio Solar');")


# --- Finalizar Transação e Fechar Conexão ---
conn.commit()
print("Banco de dados populado com sucesso!")
conn.close()
