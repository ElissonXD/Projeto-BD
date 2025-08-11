import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]
movimentos = banco["movimento"]

lista_pokemons = [
    {"_id": 1, "nome": "Pikachu",   "regiao": "Kanto"},
    {"_id": 2, "nome": "Charizard", "regiao": "Kanto"},
    {"_id": 3, "nome": "Starmie",   "regiao": "Kanto"},
    {"_id": 4, "nome": "Eevee",     "regiao": "Kanto"},
    {"_id": 5, "nome": "Lapras",    "regiao": "Kanto"},
    {"_id": 6, "nome": "Gyarados",  "regiao": "Kanto"},
    {"_id": 7, "nome": "Blastoise", "regiao": "Kanto"},
    {"_id": 8, "nome": "Pidgeot",   "regiao": "Kanto"},
]

lista_movimentos = [
    {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico", "pokemon_id": 1},
    {"_id": 102, "nome": "Quick Attack","tipo": "Normal",   "pokemon_id": 1},
    {"_id": 103, "nome": "Iron Tail",   "tipo": "Aço",      "pokemon_id": 1},
    {"_id": 201, "nome": "Flamethrower","tipo": "Fogo",     "pokemon_id": 2},
    {"_id": 202, "nome": "Wing Attack", "tipo": "Voador",   "pokemon_id": 2},
    {"_id": 301, "nome": "Surf",        "tipo": "Água",     "pokemon_id": 3},
    {"_id": 302, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon_id": 3},
    {"_id": 401, "nome": "Quick Attack","tipo": "Normal",   "pokemon_id": 4},
    {"_id": 501, "nome": "Surf",        "tipo": "Água",     "pokemon_id": 5},
    {"_id": 502, "nome": "Ice Beam",    "tipo": "Gelo",     "pokemon_id": 5},
    {"_id": 601, "nome": "Surf",        "tipo": "Água",     "pokemon_id": 6},
    {"_id": 602, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon_id": 6},
    {"_id": 701, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon_id": 7},
    {"_id": 702, "nome": "Ice Beam",    "tipo": "Gelo",     "pokemon_id": 7},
    {"_id": 801, "nome": "Wing Attack", "tipo": "Voador",   "pokemon_id": 8},
]

cliente.drop_database("banco_de_dados")
pokemons.insert_many(lista_pokemons)
movimentos.insert_many(lista_movimentos)

id_pokemon = int(input("Digite o id do Pokémon: "))

cursor = movimentos.find({"pokemon_id": id_pokemon}, projection={"_id": 0, "nome": 1})
nomes = [m["nome"] for m in cursor]
if nomes:
    print(*nomes, sep="\n")
else:
    print("Esse Pokémon não possui movimentos cadastrados.")
