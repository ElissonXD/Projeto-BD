import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]

lista_pokemons = [
    {"_id": 1, "nome": "Pikachu", "pokemon_moves": [
        {"movimento": {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico"}},
        {"movimento": {"_id": 102, "nome": "Quick Attack","tipo": "Normal"}},
        {"movimento": {"_id": 103, "nome": "Iron Tail",   "tipo": "Aço"}},
    ]},
    {"_id": 2, "nome": "Charizard", "pokemon_moves": [
        {"movimento": {"_id": 201, "nome": "Flamethrower","tipo": "Fogo"}},
        {"movimento": {"_id": 202, "nome": "Wing Attack", "tipo": "Voador"}},
    ]},
    {"_id": 3, "nome": "Starmie", "pokemon_moves": [
        {"movimento": {"_id": 301, "nome": "Surf",        "tipo": "Água"}},
        {"movimento": {"_id": 302, "nome": "Hydro Pump",  "tipo": "Água"}},
    ]},
    {"_id": 4, "nome": "Eevee", "pokemon_moves": [
        {"movimento": {"_id": 102, "nome": "Quick Attack","tipo": "Normal"}},
    ]},
    {"_id": 5, "nome": "Lapras", "pokemon_moves": [
        {"movimento": {"_id": 301, "nome": "Surf",        "tipo": "Água"}},
        {"movimento": {"_id": 401, "nome": "Ice Beam",    "tipo": "Gelo"}},
    ]},
    {"_id": 6, "nome": "Gyarados", "pokemon_moves": [
        {"movimento": {"_id": 301, "nome": "Surf",        "tipo": "Água"}},
        {"movimento": {"_id": 302, "nome": "Hydro Pump",  "tipo": "Água"}},
    ]},
    {"_id": 7, "nome": "Blastoise", "pokemon_moves": [
        {"movimento": {"_id": 302, "nome": "Hydro Pump",  "tipo": "Água"}},
        {"movimento": {"_id": 401, "nome": "Ice Beam",    "tipo": "Gelo"}},
    ]},
    {"_id": 8, "nome": "Pidgeot", "pokemon_moves": [
        {"movimento": {"_id": 202, "nome": "Wing Attack", "tipo": "Voador"}},
    ]},
]

cliente.drop_database("banco_de_dados")
pokemons.insert_many(lista_pokemons)

nome_pokemon = input("Digite o nome do Pokémon: ").strip()

poke = pokemons.find_one(
    {"nome": nome_pokemon},
    projection={"_id": 0, "pokemon_moves.movimento.nome": 1}
)
if not poke:
    print("Pokémon não encontrado.")
else:
    subdocs = poke.get("pokemon_moves", [])
    if subdocs:
        print(*[pm["movimento"]["nome"] for pm in subdocs], sep="\n")
    else:
        print("Esse Pokémon não possui movimentos cadastrados.")
