import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
movimentos = banco["movimento"]

lista_movimentos = [
    {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico", "pokemon": {"_id": 1, "nome": "Pikachu"}},
    {"_id": 102, "nome": "Quick Attack","tipo": "Normal",   "pokemon": {"_id": 1, "nome": "Pikachu"}},
    {"_id": 103, "nome": "Iron Tail",   "tipo": "Aço",      "pokemon": {"_id": 1, "nome": "Pikachu"}},
    {"_id": 201, "nome": "Flamethrower","tipo": "Fogo",     "pokemon": {"_id": 2, "nome": "Charizard"}},
    {"_id": 202, "nome": "Wing Attack", "tipo": "Voador",   "pokemon": {"_id": 2, "nome": "Charizard"}},
    {"_id": 301, "nome": "Surf",        "tipo": "Água",     "pokemon": {"_id": 3, "nome": "Starmie"}},
    {"_id": 302, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon": {"_id": 3, "nome": "Starmie"}},
    {"_id": 401, "nome": "Quick Attack","tipo": "Normal",   "pokemon": {"_id": 4, "nome": "Eevee"}},
    {"_id": 501, "nome": "Surf",        "tipo": "Água",     "pokemon": {"_id": 5, "nome": "Lapras"}},
    {"_id": 502, "nome": "Ice Beam",    "tipo": "Gelo",     "pokemon": {"_id": 5, "nome": "Lapras"}},
    {"_id": 601, "nome": "Surf",        "tipo": "Água",     "pokemon": {"_id": 6, "nome": "Gyarados"}},
    {"_id": 602, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon": {"_id": 6, "nome": "Gyarados"}},
    {"_id": 701, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon": {"_id": 7, "nome": "Blastoise"}},
    {"_id": 702, "nome": "Ice Beam",    "tipo": "Gelo",     "pokemon": {"_id": 7, "nome": "Blastoise"}},
    {"_id": 801, "nome": "Wing Attack", "tipo": "Voador",   "pokemon": {"_id": 8, "nome": "Pidgeot"}},
]

cliente.drop_database("banco_de_dados")
movimentos.insert_many(lista_movimentos)

id_pokemon = int(input("Digite o id do Pokémon: "))

cursor = movimentos.find({"pokemon._id": id_pokemon}, projection={"_id": 0, "nome": 1})
nomes = [m["nome"] for m in cursor]
if nomes:
    print(*nomes, sep="\n")
else:
    print("Pokémon não encontrado ou sem movimentos cadastrados.")
