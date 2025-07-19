import sqlite3 as sql


conn = sql.connect('banco.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()
# INSERINDO DADOS

# --- Entidades Principais ---

# TREINADOR
cursor.execute("INSERT INTO treinador (id, nome) VALUES (1, 'Ash Ketchum');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (2, 'Misty');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (3, 'Brock');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (4, 'Giovanni');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (10, 'Red');")
cursor.execute("INSERT INTO treinador (id, nome) VALUES (100, 'Professor Carvalho');")

# PROFESSOR (Subtipo de Treinador)
cursor.execute("INSERT INTO professor (id, area_de_pesquisa) VALUES (100, 'Biologia Pokémon');")

# LIDER (Subtipo de Treinador)
cursor.execute("INSERT INTO lider (id) VALUES (2);")
cursor.execute("INSERT INTO lider (id) VALUES (3);")
cursor.execute("INSERT INTO lider (id) VALUES (4);")

# ITEM
cursor.execute("INSERT INTO item (nome) VALUES ('Poção');")
cursor.execute("INSERT INTO item (nome) VALUES ('Pedra do Trovão');")
cursor.execute("INSERT INTO item (nome) VALUES ('Insígnia da Rocha');")
cursor.execute("INSERT INTO item (nome) VALUES ('TM34 - Onda Tóxica');")

# MOVIMENTO
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Choque do Trovão', 'Elétrico');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Ataque Rápido', 'Normal');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Chicote de Vinha', 'Grama');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Lança-Chamas', 'Fogo');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Jato de Água', 'Água');")
cursor.execute("INSERT INTO movimento (nome, tipo) VALUES ('Tumba de Rochas', 'Pedra');")

# ESPÉCIE
cursor.execute("INSERT INTO especie (numero, tipo1, tipo2) VALUES (1, 'Grama', 'Veneno');") # Bulbasaur
cursor.execute("INSERT INTO especie (numero, pre_evolucao, tipo1, tipo2) VALUES (2, 1, 'Grama', 'Veneno');") # Ivysaur
cursor.execute("INSERT INTO especie (numero, tipo1) VALUES (4, 'Fogo');") # Charmander
cursor.execute("INSERT INTO especie (numero, tipo1) VALUES (7, 'Água');") # Squirtle
cursor.execute("INSERT INTO especie (numero, tipo1) VALUES (25, 'Elétrico');") # Pikachu
cursor.execute("INSERT INTO especie (numero, pre_evolucao, pre_requisito, tipo1) VALUES (26, 25, 'Pedra do Trovão', 'Elétrico');") # Raichu
cursor.execute("INSERT INTO especie (numero, tipo1, tipo2) VALUES (95, 'Pedra', 'Terrestre');") # Onix

# --- Entidades com Relacionamentos ---

# GINASIO (Liderado por um Líder)
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Pewter', 'Ginásio de Pewter', 'Pedra', 3);")
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Cerulean', 'Ginásio de Cerulean', 'Água', 2);")
cursor.execute("INSERT INTO ginasio (cidade, nome, tipo, id) VALUES ('Viridian', 'Ginásio de Viridian', 'Terrestre', 4);")

# POKEMON (Com e sem treinador)
# Pokémons do Ash
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (25, 1, 1);") # Pikachu do Ash
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (4, 1, 1);")  # Charmander do Ash
# Pokémon da Misty
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (7, 1, 2);")  # Squirtle da Misty
# Pokémon do Brock
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, id_treinador) VALUES (95, 1, 3);") # Onix do Brock
# Pokémon Selvagem (sem treinador, com rota/regiao)
cursor.execute("INSERT INTO pokemon (numero, id_pokemon, rota, regiao) VALUES (1, 101, 'Rota 1', 'Kanto');") # Bulbasaur selvagem

# --- Tabelas de Relacionamento N:M ---

# POKEMON TEM MOVIMENTO (Movimentos inatos)
# id_pokemon é 'indice' na tabela 'tem'
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Choque do Trovão', 1, 25);") # Pikachu do Ash
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Ataque Rápido', 1, 25);")   # Pikachu do Ash
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Chicote de Vinha', 101, 1);") # Bulbasaur selvagem
cursor.execute("INSERT INTO tem (nome, indice, numero) VALUES ('Tumba de Rochas', 1, 95);")  # Onix do Brock

# TREINADOR ENSINA MOVIMENTO A POKEMON
cursor.execute("INSERT INTO ensina (nome, id_pokemon, numero, id_treinador) VALUES ('Lança-Chamas', 1, 4, 1);") # Ash ensina Lança-Chamas ao seu Charmander

# TREINADOR ENFRENTA GINASIO
cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Pewter', 1, '2025-07-15');") # Ash enfrenta o ginásio de Pewter
cursor.execute("INSERT INTO enfrenta (cidade, id, data) VALUES ('Cerulean', 10, '2025-07-16');") # Red enfrenta o ginásio de Cerulean

# TREINADOR RECEBE ITEM (Ligado a um confronto em 'enfrenta')
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Pewter', 1, '2025-07-15', 'Insígnia da Rocha');") # Ash recebe a insígnia após vencer
cursor.execute("INSERT INTO recebe (cidade, id, data, nome) VALUES ('Pewter', 1, '2025-07-15', 'Poção');") # Ash também recebe uma poção

# --- Finalizar Transação ---
conn.commit()
print("Banco de dados populado com sucesso!")

# --- Fechar Conexão ---
conn.close()
