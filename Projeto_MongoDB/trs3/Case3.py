import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]
pokemon_moves = banco["pokemon_move"]

lista_pokemon_move = [
    {"_id": 1001, "movimento": {"nome": "Thunderbolt", "tipo": "Elétrico"}},
    {"_id": 1002, "movimento": {"nome": "Quick Attack","tipo": "Normal"}},
    {"_id": 1003, "movimento": {"nome": "Iron Tail",   "tipo": "Aço"}},
    {"_id": 1101, "movimento": {"nome": "Flamethrower","tipo": "Fogo"}},
    {"_id": 1102, "movimento": {"nome": "Wing Attack", "tipo": "Voador"}},
    {"_id": 1201, "movimento": {"nome": "Surf",        "tipo": "Água"}},
    {"_id": 1202, "movimento": {"nome": "Hydro Pump",  "tipo": "Água"}},
    {"_id": 1301, "movimento": {"nome": "Quick Attack","tipo": "Normal"}},
    {"_id": 1401, "movimento": {"nome": "Surf",        "tipo": "Água"}},
    {"_id": 1402, "movimento": {"nome": "Ice Beam",    "tipo": "Gelo"}},
    {"_id": 1501, "movimento": {"nome": "Surf",        "tipo": "Água"}},
    {"_id": 1502, "movimento": {"nome": "Hydro Pump",  "tipo": "Água"}},
    {"_id": 1601, "movimento": {"nome": "Hydro Pump",  "tipo": "Água"}},
    {"_id": 1602, "movimento": {"nome": "Ice Beam",    "tipo": "Gelo"}},
    {"_id": 1701, "movimento": {"nome": "Wing Attack", "tipo": "Voador"}},
]

lista_pokemons = [
    {"_id": 1, "nome": "Pikachu", "movimentos_refs": [1001, 1002, 1003]},
    {"_id": 2, "nome": "Charizard", "movimentos_refs": [1101, 1102]},
    {"_id": 3, "nome": "Starmie", "movimentos_refs": [1201, 1202]},
    {"_id": 4, "nome": "Eevee", "movimentos_refs": [1301]},
    {"_id": 5, "nome": "Lapras", "movimentos_refs": [1401, 1402]},
    {"_id": 6, "nome": "Gyarados", "movimentos_refs": [1501, 1502]},
    {"_id": 7, "nome": "Blastoise", "movimentos_refs": [1601, 1602]},
    {"_id": 8, "nome": "Pidgeot", "movimentos_refs": [1701]},
]

cliente.drop_database("banco_de_dados")
pokemon_moves.insert_many(lista_pokemon_move)
pokemons.insert_many(lista_pokemons)

id_pokemon = int(input("Digite o id do Pokémon: "))

movs = pokemons.find_one({"_id": id_pokemon})
if movs:
    for moves in movs['movimentos_refs']:
        pokmov = pokemon_moves.find_one({"_id": moves})
        if pokmov:
            print(f'{pokmov['movimento']['nome']}, {pokmov['movimento']['tipo']}')
