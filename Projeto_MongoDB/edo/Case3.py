#um documento com um array de referências para documentos
# movimento 1 - N pokemon_movimento
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

pokemon_movimento = banco['pokemon_movimento']
movimento = banco['movimento']

lista_movimentos = [
    { "_id": 1,  "nome": "Thunderbolt",    "tipo": "elétrico", 'pokemon_movimento': [1, 7]},
    { "_id": 2,  "nome": "Quick Attack",   "tipo": "normal",   'pokemon_movimento': [101]},
    { "_id": 3,  "nome": "Flamethrower",   "tipo": "fogo",     'pokemon_movimento': [2]},
    { "_id": 4,  "nome": "Wing Attack",    "tipo": "voador",   'pokemon_movimento': [201, 5]},
    { "_id": 5,  "nome": "Hydro Pump",     "tipo": "água",     'pokemon_movimento': [301, 6]},
    { "_id": 6,  "nome": "Vine Whip",      "tipo": "planta",   'pokemon_movimento': [4]},
    { "_id": 7,  "nome": "Water Gun",      "tipo": "água",     'pokemon_movimento': [601]},
    { "_id": 8,  "nome": "Psychic",        "tipo": "psíquico", 'pokemon_movimento': [8]},
    { "_id": 9,  "nome": "Earthquake",     "tipo": "terra",    'pokemon_movimento': [9, 202]},
    { "_id": 10, "nome": "Double Kick",    "tipo": "lutador",  'pokemon_movimento': [10]},
    { "_id": 11, "nome": "Poison Sting",   "tipo": "veneno",   'pokemon_movimento': [11, 401]},
    { "_id": 12, "nome": "Ice Beam",       "tipo": "gelo",     'pokemon_movimento': [1201, 602]},
    { "_id": 13, "nome": "Blizzard",       "tipo": "gelo",     'pokemon_movimento': [12]},
    { "_id": 14, "nome": "Hyper Beam",     "tipo": "normal",   'pokemon_movimento': [501, 901]},
    { "_id": 15, "nome": "Surf",           "tipo": "água",     'pokemon_movimento': [603, 3]}
]

lista_pokmov = [
    {"_id": 1,   "pokemon": {"num_especie": 25,  "id_natureza": 1, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 1}},
    {"_id": 101, "pokemon": {"num_especie": 25,  "id_natureza": 1, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 1}},
    {"_id": 2,   "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 201, "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 202, "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 3,   "pokemon": {"num_especie": 9,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 301, "pokemon": {"num_especie": 9,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 4,   "pokemon": {"num_especie": 3,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 401, "pokemon": {"num_especie": 3,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 5,   "pokemon": {"num_especie": 18,  "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 501, "pokemon": {"num_especie": 18,  "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 6,   "pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}},
    {"_id": 601, "pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}},
    {"_id": 602, "pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}},
    {"_id": 603, "pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}},
    {"_id": 7,   "pokemon": {"num_especie": 100, "id_natureza": 2, "rota": "Power Plant",     "regiao": "Kanto", "treinador": 0}},
    {"_id": 8,   "pokemon": {"num_especie": 150, "id_natureza": 3, "rota": "Cerulean Cave",   "regiao": "Kanto", "treinador": 0}},
    {"_id": 9,   "pokemon": {"num_especie": 112, "id_natureza": 2, "rota": "Victory Road",    "regiao": "Kanto", "treinador": 0}},
    {"_id": 901, "pokemon": {"num_especie": 112, "id_natureza": 2, "rota": "Victory Road",    "regiao": "Kanto", "treinador": 0}},
    {"_id": 10,  "pokemon": {"num_especie": 67,  "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
    {"_id": 11,  "pokemon": {"num_especie": 15,  "id_natureza": 2, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 0}},
    {"_id": 12,  "pokemon": {"num_especie": 144, "id_natureza": 3, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 0}},
    {"_id": 1201,"pokemon": {"num_especie": 144, "id_natureza": 3, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 0}}
]

cliente.drop_database('banco_de_dados')
movimento.insert_many(lista_movimentos)
pokemon_movimento.insert_many(lista_pokmov)

# Consultar quais movimentos um pokémon tem
num = int(input("Insira o id do movimento: "))

movs = movimento.find_one({"_id": num})
if movs:
    for pokemons in movs['pokemon_movimento']:
        pokemon = pokemon_movimento.find_one({"_id": pokemons})
        if pokemon:
            print(f'{pokemon["pokemon"]["num_especie"]}, {pokemon["pokemon"]["id_natureza"]}, {pokemon["pokemon"]["rota"]}, {pokemon["pokemon"]["regiao"]}, {pokemon["pokemon"]["treinador"]}')
