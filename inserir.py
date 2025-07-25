import sqlite3

def printar_informações():
    print(f"{"="*10} INSERIR {"="*10}")
    print("""1. Treinador
2. Professor
3. Líder
4. Ginásio
5. Enfrenta
6. Item
7. Recebe
8. Espécie
9. Pokémon
10. Movimento
11. Tem
12. Ensina""")
    print("=" * 29)


def safe_input(prompt, cast=str):
    valor = input(prompt)
    if valor == '':
        return None
    return cast(valor)
   

conn = sqlite3.connect('banco.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

printar_informações()

while True:
    try:
        resposta = int(input('Insira o número da tabela ou 0 para ver as tabelas novamente ou outro valor para finalizar: '))

        if resposta == 0:
            printar_informações()

        if resposta == 1:
            id_treinador = safe_input("ID do treinador: ")
            nome_treinador = safe_input("Nome do treinador: ")
            numero_pokemon = safe_input("Número do Pokémon do treinador: ", int)
            id_pokemon = safe_input("ID do Pokémon do treinador: ", int)

            cursor.execute("""
                SELECT * FROM pokemon WHERE numero = ? AND id_pokemon = ?
            """, (numero_pokemon, id_pokemon))
            pokemon_exists = bool(cursor.fetchall())

            if pokemon_exists:
                cursor.execute("""
                    INSERT INTO treinador (id, nome) VALUES (?, ?)
                """, (id_treinador, nome_treinador))

                cursor.execute("""
                    UPDATE pokemon SET id_treinador = ? 
                    WHERE numero = ? AND id_pokemon = ?
                """, (id_treinador, numero_pokemon, id_pokemon))
                print("Treinador inserido com sucesso.")
            else:
                print("Pokémon não encontrado. Treinador não inserido.")

        elif resposta == 2:
            id_treinador = safe_input("ID de treinador: ")
            area_pesquisa = safe_input("Área de pesquisa: ")
            cursor.execute("""
                INSERT INTO professor (id, area_de_pesquisa) VALUES (?, ?)
            """, (id_treinador, area_pesquisa))
            print("Professor inserido com sucesso.")

        elif resposta == 3:
            id_lider = safe_input("ID de treinador: ")
            cursor.execute("""
                INSERT INTO lider (id) VALUES (?)
            """, (id_lider,))
            print("Líder inserido com sucesso.")

        elif resposta == 4:
            cidade = safe_input("Cidade do ginásio: ")
            nome = safe_input("Nome do ginásio: ")
            tipo = safe_input("Tipo principal do ginásio: ")
            id_lider = safe_input("ID do líder: ")
            cursor.execute("""
                INSERT INTO ginasio (cidade, nome, tipo, id)
                VALUES (?, ?, ?, ?)
            """, (cidade, nome, tipo, id_lider))
            print("Ginásio inserido com sucesso.")

        elif resposta == 5:
            cidade = safe_input("Cidade do ginásio: ")
            id_treinador = safe_input("ID do treinador: ")
            data = safe_input("Data da batalha (formato AAAA-MM-DD): ")
            cursor.execute("""
                INSERT INTO enfrenta (cidade, id, data)
                VALUES (?, ?, ?)
            """, (cidade, id_treinador, data))
            print("Batalha registrada com sucesso.")

        elif resposta == 6:
            nome = safe_input("Nome do item: ")
            cursor.execute("""
                INSERT INTO item (nome) VALUES (?)
            """, (nome,))
            print("Item inserido com sucesso.")

        elif resposta == 7:
            cidade = safe_input("Cidade do ginásio: ")
            id_treinador = safe_input("ID do treinador: ")
            data = safe_input("Data (formato AAAA-MM-DD): ")
            nome_item = safe_input("Nome do item recebido: ")
            cursor.execute("""
                INSERT INTO recebe (cidade, id, data, nome)
                VALUES (?, ?, ?, ?)
            """, (cidade, id_treinador, data, nome_item))
            print("Item recebido registrado com sucesso.")

        elif resposta == 8:
            numero = safe_input("Número da espécie: ", int)
            nome = safe_input("Nome da espécie: ")
            pre_evolucao = safe_input("Número da pré-evolução (pode ser nulo): ", int)
            pre_req = safe_input("Pré-requisito para evoluir (pode ser nulo): ")
            tipo1 = safe_input("Tipo primário: ")
            tipo2 = safe_input("Tipo secundário (pode ser nulo): ")
            cursor.execute("""
                INSERT INTO especie (numero, nome, pre_evolucao, pre_requisito, tipo1, tipo2)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (numero, nome, pre_evolucao, pre_req, tipo1, tipo2))
            print("Espécie inserida com sucesso.")

        elif resposta == 9:
            numero = safe_input("Número da espécie: ", int)
            id_pokemon = safe_input("ID do Pokémon: ", int)
            rota = safe_input("Rota onde foi encontrado: ")
            regiao = safe_input("Região onde foi encontrado: ")
            cursor.execute("""
                INSERT INTO pokemon (numero, id_pokemon, rota, regiao)
                VALUES (?, ?, ?, ?)
            """, (numero, id_pokemon, rota, regiao))
            print("Pokémon inserido com sucesso.")

        elif resposta == 10:
            nome = safe_input("Nome do movimento: ")
            tipo = safe_input("Tipo do movimento: ")
            cursor.execute("""
                INSERT INTO movimento (nome, tipo) VALUES (?, ?)
            """, (nome, tipo))
            print("Movimento inserido com sucesso.")

        elif resposta == 11:
            nome_mov = safe_input("Nome do movimento: ")
            id_pokemon = safe_input("ID do Pokémon: ", int)
            numero = safe_input("Número da espécie do Pokémon: ", int)
            cursor.execute("""
                INSERT INTO tem (nome, indice, numero)
                VALUES (?, ?, ?)
            """, (nome_mov, id_pokemon, numero))
            print("Movimento associado ao Pokémon com sucesso.")

        elif resposta == 12:
            nome_mov = safe_input("Nome do movimento: ")
            id_pokemon = safe_input("ID do Pokémon: ", int)
            numero = safe_input("Número da espécie: ", int)
            id_treinador = safe_input("ID do treinador: ")
            cursor.execute("""
                INSERT INTO ensina (nome, id_pokemon, numero, id_treinador)
                VALUES (?, ?, ?, ?)
            """, (nome_mov, id_pokemon, numero, id_treinador))
            print("Movimento ensinado ao Pokémon com sucesso.")

        else:
            print("Encerrando...")
            break

        conn.commit()

    except:
        print("DADOS INVÁLIDOS, VALOR NÂO INSERIDO")

conn.close()
