#um documento referenciando apenas um documento
# movimento 1 - N pokemon_movimento
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

pokemon_movimento = banco['pokemon_movimento']
movimento = banco['movimento']

lista_movimentos = [
    { "_id": 1,  "nome": "Thunderbolt",   "tipo": "elétrico" },
    { "_id": 2,  "nome": "Quick Attack",  "tipo": "normal" },
    { "_id": 3,  "nome": "Flamethrower",  "tipo": "fogo" },
    { "_id": 4,  "nome": "Wing Attack",   "tipo": "voador" },
    { "_id": 5,  "nome": "Hydro Pump",    "tipo": "água" },
    { "_id": 6,  "nome": "Vine Whip",     "tipo": "planta" },
    { "_id": 7,  "nome": "Water Gun",     "tipo": "água" },
    { "_id": 8,  "nome": "Psychic",       "tipo": "psíquico" },
    { "_id": 9,  "nome": "Earthquake",    "tipo": "terra" },
    { "_id": 10, "nome": "Double Kick",   "tipo": "lutador" },
    { "_id": 11, "nome": "Poison Sting",  "tipo": "veneno" },
    { "_id": 12, "nome": "Ice Beam",      "tipo": "gelo" },
    { "_id": 13, "nome": "Blizzard",      "tipo": "gelo" },
    { "_id": 14, "nome": "Hyper Beam",    "tipo": "normal" }
]

lista_pokmov = [
    {"_id": 1,  "movimento": 1,  "pokemon": {"num_especie": 25,  "id_natureza": 1, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 1}},
    {"_id": 2,  "movimento": 2,  "pokemon": {"num_especie": 25,  "id_natureza": 1, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 1}},
    {"_id": 3,  "movimento": 3,  "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 4,  "movimento": 4,  "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 5,  "movimento": 5,  "pokemon": {"num_especie": 9,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 6,  "movimento": 6,  "pokemon": {"num_especie": 3,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 7,  "movimento": 4,  "pokemon": {"num_especie": 18,  "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 8,  "movimento": 7,  "pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}},
    {"_id": 9,  "movimento": 8,  "pokemon": {"num_especie": 150, "id_natureza": 3, "rota": "Cerulean Cave",   "regiao": "Kanto", "treinador": 0}},
    {"_id": 10, "movimento": 9,  "pokemon": {"num_especie": 112, "id_natureza": 2, "rota": "Victory Road",    "regiao": "Kanto", "treinador": 0}},
    {"_id": 11, "movimento": 10, "pokemon": {"num_especie": 67,  "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 12, "movimento": 11, "pokemon": {"num_especie": 15,  "id_natureza": 2, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 0}},
    {"_id": 13, "movimento": 12, "pokemon": {"num_especie": 144, "id_natureza": 3, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 0}},
    {"_id": 14, "movimento": 13, "pokemon": {"num_especie": 144, "id_natureza": 3, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 0}},
    {"_id": 15, "movimento": 14, "pokemon": {"num_especie": 18,  "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}}
]

cliente.drop_database('banco_de_dados')
movimento.insert_many(lista_movimentos)
pokemon_movimento.insert_many(lista_pokmov)

# Consultar quais movimentos um pokémon tem

num = int(input("Insira o número do pokémon: "))
id_pokemon = int(input("Insira o numero do id do pokémon: "))

for pokmov in pokemon_movimento.find({'pokemon.num_especie': num, 'pokemon.id_natureza': id_pokemon}):
    mov_id = pokmov['movimento']
    mov = movimento.find_one({"_id": mov_id})
    print(f'{mov['nome']}, {mov['tipo']}')