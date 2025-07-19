import sqlite3

conn = sqlite3.connect('banco.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

resposta = input('qual tabela: ')

if resposta == "treinador":
    id_treinador = input("insira o id: ")
    nome_treinador = input("insira o nome: ")
    numero_pokemon = int(input("Insira o numero de um dos Pokémon do treinador: "))
    id_pokemon = int(input("Insira a id do Pokémon do treinador: "))

    cursor.execute("""
    SELECT * FROM pokemon p
                   WHERE p.numero = ? AND p.id_pokemon = ?
""", (numero_pokemon, id_pokemon))
    pokemon_exists = bool(cursor.fetchall())

    if pokemon_exists:
        cursor.execute("""
        INSERT INTO treinador (id, nome)
        VALUES (?, ?)
        """, (id_treinador, nome_treinador))

        cursor.execute("""
        UPDATE pokemon
        SET id_treinador = ?
        WHERE numero = ? AND id_pokemon = ?
        """, (id_treinador, numero_pokemon, id_pokemon))
    else:
        print("valor não inserido :)")

elif resposta == "pokemon":
    numero_pokemon = int(input("insira o numero do pokemon: "))
    id_pokemon = int(input("insira o id do pokemon: "))
    rota_pokemon = input("insira a rota onde foi encontrado: ")
    região_pokemon = input("insir a região onde o pokemon foi encontrado: ")

    cursor.execute("""
    INSERT INTO pokemon (numero, id_pokemon, rota, regiao)
    VALUES (?, ?, ?, ?)
    """, (numero_pokemon, id_pokemon,rota_pokemon, região_pokemon))

elif resposta == "professor":
    id_treinador = input("insira o id: ")
    area_pesquisa = input("insira a area de pesquisa: ")
    cursor.execute("""
    INSERT INTO professor (id, area_de_pesquisa)
    VALUES (?, ?)
    """, (id_treinador, area_pesquisa))

conn.commit()
