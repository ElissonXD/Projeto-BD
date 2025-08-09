#um documento embutindo apenas um documento
# movimento 1 - N pokemon_movimento
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

pokemon_movimento = banco['pokemon_movimento']
lista_pokmov = [
    {"_id": 1,  "movimento": {"_id": 1,  "nome": "Thunderbolt",  "tipo": "elétrico"}, "pokemon": {"num_especie": 25,  "id_natureza": 1, "rota": "Viridian Forest",  "regiao": "Kanto", "treinador": 1}},
    {"_id": 2,  "movimento": {"_id": 2,  "nome": "Quick Attack", "tipo": "normal"},  "pokemon": {"num_especie": 25,  "id_natureza": 1, "rota": "Viridian Forest",  "regiao": "Kanto", "treinador": 1}},
    {"_id": 3,  "movimento": {"_id": 3,  "nome": "Flamethrower", "tipo": "fogo"},    "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,               "regiao": "Kanto", "treinador": 1}},
    {"_id": 4,  "movimento": {"_id": 4,  "nome": "Wing Attack",  "tipo": "voador"},  "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,               "regiao": "Kanto", "treinador": 1}},
    {"_id": 5,  "movimento": {"_id": 5,  "nome": "Hydro Pump",   "tipo": "água"},    "pokemon": {"num_especie": 9,   "id_natureza": 1, "rota": None,               "regiao": "Kanto", "treinador": 1}},
    {"_id": 6,  "movimento": {"_id": 6,  "nome": "Vine Whip",    "tipo": "planta"},  "pokemon": {"num_especie": 3,   "id_natureza": 1, "rota": None,               "regiao": "Kanto", "treinador": 1}},
    {"_id": 7,  "movimento": {"_id": 4,  "nome": "Wing Attack",  "tipo": "voador"},  "pokemon": {"num_especie": 18,  "id_natureza": 1, "rota": None,               "regiao": "Kanto", "treinador": 1}},
    {"_id": 8,  "movimento": {"_id": 7,  "nome": "Water Gun",    "tipo": "água"},    "pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands",  "regiao": "Kanto", "treinador": 1}},
    {"_id": 9,  "movimento": {"_id": 8,  "nome": "Psychic",      "tipo": "psíquico"},"pokemon": {"num_especie": 150, "id_natureza": 3, "rota": "Cerulean Cave",    "regiao": "Kanto", "treinador": 0}},
    {"_id": 10, "movimento": {"_id": 9,  "nome": "Earthquake",   "tipo": "terra"},   "pokemon": {"num_especie": 112, "id_natureza": 2, "rota": "Victory Road",     "regiao": "Kanto", "treinador": 0}},
    {"_id": 11, "movimento": {"_id": 10, "nome": "Double Kick",  "tipo": "lutador"}, "pokemon": {"num_especie": 67,  "id_natureza": 1, "rota": None,               "regiao": "Kanto", "treinador": 1}},
    {"_id": 12, "movimento": {"_id": 11, "nome": "Poison Sting", "tipo": "veneno"},  "pokemon": {"num_especie": 15,  "id_natureza": 2, "rota": "Viridian Forest",  "regiao": "Kanto", "treinador": 0}},
    {"_id": 13, "movimento": {"_id": 12, "nome": "Ice Beam",     "tipo": "gelo"},    "pokemon": {"num_especie": 144, "id_natureza": 3, "rota": "Seafoam Islands",  "regiao": "Kanto", "treinador": 0}},
    {"_id": 14, "movimento": {"_id": 13, "nome": "Blizzard",     "tipo": "gelo"},    "pokemon": {"num_especie": 144, "id_natureza": 3, "rota": "Seafoam Islands",  "regiao": "Kanto", "treinador": 0}},
    {"_id": 15, "movimento": {"_id": 14, "nome": "Hyper Beam",   "tipo": "normal"},  "pokemon": {"num_especie": 18,  "id_natureza": 1, "rota": None,               "regiao": "Kanto", "treinador": 1}}
]

cliente.drop_database('banco_de_dados')
pokemon_movimento.insert_many(lista_pokmov)

# Consultar quais movimentos um pokémon tem

num = int(input("Insira o id do movimento: "))

movs = pokemon_movimento.find({"movimento._id": num})
if movs:
    for pokemons in movs:
        print(f'{pokemons["pokemon"]["num_especie"]}, {pokemons["pokemon"]["id_natureza"]}, {pokemons["pokemon"]["rota"]}, {pokemons["pokemon"]["regiao"]}, {pokemons["pokemon"]["treinador"]}')
