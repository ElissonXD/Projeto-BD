# PokeMove_Case1.py
# Relacionamento 1:N modelado como: cada documento de "movimento" referencia UM "pokemon"
# Consulta: nomes dos movimentos do Pokémon com nome = <entrada>
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]
movimentos = banco["movimento"]

# Dados de exemplo (AGORA com mais pokémons e movimentos repetidos entre pokémons)
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

# Observação: como cada documento em 'movimento' pertence a 1 pokémon, para haver
# "mesmo movimento" em pokémons diferentes, repetimos o nome em docs distintos.
lista_movimentos = [
    # Pikachu
    {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico", "pokemon_id": 1},
    {"_id": 102, "nome": "Quick Attack","tipo": "Normal",   "pokemon_id": 1},
    {"_id": 103, "nome": "Iron Tail",   "tipo": "Aço",      "pokemon_id": 1},
    # Charizard
    {"_id": 201, "nome": "Flamethrower","tipo": "Fogo",     "pokemon_id": 2},
    {"_id": 202, "nome": "Wing Attack", "tipo": "Voador",   "pokemon_id": 2},
    # Starmie
    {"_id": 301, "nome": "Surf",        "tipo": "Água",     "pokemon_id": 3},
    {"_id": 302, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon_id": 3},
    # Eevee (movimento repetido: Quick Attack)
    {"_id": 401, "nome": "Quick Attack","tipo": "Normal",   "pokemon_id": 4},
    # Lapras (movimento repetido: Surf, Ice Beam)
    {"_id": 501, "nome": "Surf",        "tipo": "Água",     "pokemon_id": 5},
    {"_id": 502, "nome": "Ice Beam",    "tipo": "Gelo",     "pokemon_id": 5},
    # Gyarados (movimento repetido: Surf, Hydro Pump)
    {"_id": 601, "nome": "Surf",        "tipo": "Água",     "pokemon_id": 6},
    {"_id": 602, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon_id": 6},
    # Blastoise (movimento repetido: Hydro Pump, Ice Beam)
    {"_id": 701, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon_id": 7},
    {"_id": 702, "nome": "Ice Beam",    "tipo": "Gelo",     "pokemon_id": 7},
    # Pidgeot (movimento repetido: Wing Attack)
    {"_id": 801, "nome": "Wing Attack", "tipo": "Voador",   "pokemon_id": 8},
]

# Reset do banco e inserção
cliente.drop_database("banco_de_dados")
pokemons.insert_many(lista_pokemons)
movimentos.insert_many(lista_movimentos)

nome_pokemon = input("Digite o nome do Pokémon: ").strip()

poke = pokemons.find_one({"nome": nome_pokemon}, projection={"_id": 1})
if not poke:
    print("Pokémon não encontrado.")
else:
    cursor = movimentos.find({"pokemon_id": poke["_id"]}, projection={"_id": 0, "nome": 1})
    nomes = [m["nome"] for m in cursor]
    if nomes:
        print(*nomes, sep="\n")
    else:
        print("Esse Pokémon não possui movimentos cadastrados.")
