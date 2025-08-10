import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]
movimentos = banco["movimento"]
pokemon_moves = banco["pokemon_move"]

lista_movimentos = [
    {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico"},
    {"_id": 102, "nome": "Quick Attack","tipo": "Normal"},
    {"_id": 103, "nome": "Iron Tail",   "tipo": "Aço"},
    {"_id": 201, "nome": "Flamethrower","tipo": "Fogo"},
    {"_id": 202, "nome": "Wing Attack", "tipo": "Voador"},
    {"_id": 301, "nome": "Surf",        "tipo": "Água"},
    {"_id": 302, "nome": "Hydro Pump",  "tipo": "Água"},
    {"_id": 401, "nome": "Ice Beam",    "tipo": "Gelo"},
]

lista_pokemon_move = [
    {"_id": 1001, "pokemon_id": 1, "movimento_id": 101},
    {"_id": 1002, "pokemon_id": 1, "movimento_id": 102},
    {"_id": 1003, "pokemon_id": 1, "movimento_id": 103},
    {"_id": 1101, "pokemon_id": 2, "movimento_id": 201},
    {"_id": 1102, "pokemon_id": 2, "movimento_id": 202},
    {"_id": 1201, "pokemon_id": 3, "movimento_id": 301},
    {"_id": 1202, "pokemon_id": 3, "movimento_id": 302},
    {"_id": 1301, "pokemon_id": 4, "movimento_id": 102},
    {"_id": 1401, "pokemon_id": 5, "movimento_id": 301},
    {"_id": 1402, "pokemon_id": 5, "movimento_id": 401},
    {"_id": 1501, "pokemon_id": 6, "movimento_id": 301},
    {"_id": 1502, "pokemon_id": 6, "movimento_id": 302},
    {"_id": 1601, "pokemon_id": 7, "movimento_id": 302},
    {"_id": 1602, "pokemon_id": 7, "movimento_id": 401},
    {"_id": 1701, "pokemon_id": 8, "movimento_id": 202},
]

lista_pokemons = [
    {"_id": 1, "nome": "Pikachu",   "movimentos_refs": [1001, 1002, 1003]},
    {"_id": 2, "nome": "Charizard", "movimentos_refs": [1101, 1102]},
    {"_id": 3, "nome": "Starmie",   "movimentos_refs": [1201, 1202]},
    {"_id": 4, "nome": "Eevee",     "movimentos_refs": [1301]},
    {"_id": 5, "nome": "Lapras",    "movimentos_refs": [1401, 1402]},
    {"_id": 6, "nome": "Gyarados",  "movimentos_refs": [1501, 1502]},
    {"_id": 7, "nome": "Blastoise", "movimentos_refs": [1601, 1602]},
    {"_id": 8, "nome": "Pidgeot",   "movimentos_refs": [1701]},
]

cliente.drop_database("banco_de_dados")
movimentos.insert_many(lista_movimentos)
pokemon_moves.insert_many(lista_pokemon_move)
pokemons.insert_many(lista_pokemons)

nome_pokemon = input("Digite o nome do Pokémon: ").strip()

poke = pokemons.find_one({"nome": nome_pokemon}, projection={"_id": 1, "movimentos_refs": 1})
if not poke:
    print("Pokémon não encontrado.")
else:
    if not poke.get("movimentos_refs"):
        print("Esse Pokémon não possui movimentos cadastrados.")
    else:
        pares = list(pokemon_moves.find(
            {"_id": {"$in": poke["movimentos_refs"]}},
            projection={"_id": 0, "movimento_id": 1}
        ))
        if not pares:
            print("Pares pokemon_move não encontrados.")
        else:
            mov_ids = [p["movimento_id"] for p in pares]
            cursor = movimentos.find({"_id": {"$in": mov_ids}}, projection={"_id": 0, "nome": 1})
            nomes = [m["nome"] for m in cursor]
            print(*nomes, sep="\n") if nomes else print("Movimentos não encontrados.")
