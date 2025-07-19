import sqlite3 as sql

conn = sql.connect('banco.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# Espécies
cursor.executemany("""
    INSERT INTO especie (numero, pre_evolucao, pre_requisito, tipo1, tipo2)
    VALUES (?, ?, ?, ?, ?)
""", [
    (1, None, None, 'Grama', 'Veneno'),
    (4, None, None, 'Fogo', None),
    (7, None, None, 'Água', None)
])

# Pokémon
cursor.executemany("""
    INSERT INTO pokemon (numero, id_pokemon, id_treinador, rota, regiao)
    VALUES (?, ?, ?, ?, ?)
""", [
    (1, 1, None, 'Rota 1', 'Kanto'),
    (4, 2, None, 'Rota 2', 'Kanto'),
    (7, 3, None, 'Rota 3', 'Kanto')
])

# Treinadores
cursor.executemany("""
    INSERT INTO treinador (id, nome)
    VALUES (?, ?)
""", [
    (1, 'Ash'),
    (2, 'Misty'),
    (3, 'Brock')
])

# Professores
cursor.executemany("""
    INSERT INTO professor (id, area_de_pesquisa)
    VALUES (?, ?)
""", [
    (1, 'Evolução Pokémon'),
    (2, 'Comportamento aquático')
])

# Líderes
cursor.executemany("""
    INSERT INTO lider (id)
    VALUES (?)
""", [
    (2,),
    (3,)
])

# Ginásios
cursor.executemany("""
    INSERT INTO ginasio (cidade, nome, tipo, id)
    VALUES (?, ?, ?, ?)
""", [
    ('Cerulean', 'Ginásio da Água', 'Água', 2),
    ('Pewter', 'Ginásio da Pedra', 'Pedra', 3)
])

# Enfrenta
cursor.executemany("""
    INSERT INTO enfrenta (cidade, id, data)
    VALUES (?, ?, ?)
""", [
    ('Cerulean', 1, '2024-01-01'),
    ('Pewter', 1, '2024-01-02')
])

# Itens
cursor.executemany("""
    INSERT INTO item (nome)
    VALUES (?)
""", [
    ('Potion',),
    ('Rare Candy',)
])

# Recebe
cursor.executemany("""
    INSERT INTO recebe (cidade, id, data, nome)
    VALUES (?, ?, ?, ?)
""", [
    ('Cerulean', 1, '2024-01-01', 'Potion'),
    ('Pewter', 1, '2024-01-02', 'Rare Candy')
])

# Movimentos
cursor.executemany("""
    INSERT INTO movimento (nome, tipo)
    VALUES (?, ?)
""", [
    ('Tackle', 'Normal'),
    ('Water Gun', 'Água'),
    ('Ember', 'Fogo')
])

# Tem movimento
cursor.executemany("""
    INSERT INTO tem (nome, indice, numero)
    VALUES (?, ?, ?)
""", [
    ('Tackle', 1, 1),
    ('Water Gun', 3, 7),
    ('Ember', 2, 4)
])

# Ensina
cursor.executemany("""
    INSERT INTO ensina (nome, id_pokemon, numero, id_treinador)
    VALUES (?, ?, ?, ?)
""", [
    ('Tackle', 1, 1, 1),
    ('Water Gun', 3, 7, 1)
])

conn.commit()
print("Banco povoado com sucesso.")
