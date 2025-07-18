import sqlite3

conn = sqlite3.connect('banco.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

resposta = input('qual tabela: ')

if resposta == "treinador":
    id_treinador = input("insira o id: ")
    nome_treinador = input("insira o nome: ")
    indice_pokemon = int(input("Insira o indice de um dos Pokémon do treinador: "))
    especie_pokemon = input("Insira a espécie do Pokémon do treinador: ")

    
    #TODO: Consulta se o pokémon existe
    cursor.execute("""
    SELECT * FROM pokemon p
                   WHERE p.indice = ? AND p.especie = ?
""", indice_pokemon, especie_pokemon)
    pokemon_exists = bool(cursor.fetchall())

    if pokemon_exists:
        cursor.execute("""
        INSERT INTO treinador (id, nome)
        VALUES (?, ?)
        """, (id_treinador, nome_treinador))

        #TODO: Adicionar o ID do treinador como estrangeira no pokémon escolhido
        ...
elif resposta == "professor":
    id_treinador = input("insira o id: ")
    area_pesquisa = input("insira a area de pesquisa: ")
    cursor.execute("""
    INSERT INTO professor (id, area_de_pesquisa)
    VALUES (?, ?)
    """, (id_treinador, area_pesquisa))

conn.commit()
