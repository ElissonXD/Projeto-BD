#um documento embutindo vários documentos
# movimento 1 - N pokemon_movimento
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

movimento = banco['movimento']

lista_movimentos = [
    { "_id": 1,  "nome": "Thunderbolt",   "tipo": "elétrico", 'pokemon_movimento': [
        {'id_pokmov': 1, "pokemon": {"num_especie": 25,  "id_natureza": 1, "rota": "Viridian Forest",  "regiao": "Kanto", "treinador": 1}}
    ]},
    { "_id": 2,  "nome": "Quick Attack",  "tipo": "normal", 'pokemon_movimento': [
        {'id_pokmov': 1, "pokemon": {"num_especie": 25,  "id_natureza": 1, "rota": "Viridian Forest",  "regiao": "Kanto", "treinador": 1}},
        {'id_pokmov': 7, "pokemon": {"num_especie": 133, "id_natureza": 2, "rota": "Celadon City",    "regiao": "Kanto", "treinador": 2}}
    ]},
    { "_id": 3,  "nome": "Flamethrower",  "tipo": "fogo", 'pokemon_movimento': [
        {'id_pokmov': 2, "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}}
    ]},
    { "_id": 4,  "nome": "Wing Attack",   "tipo": "voador", 'pokemon_movimento': [
        {'id_pokmov': 2, "pokemon": {"num_especie": 6,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
        {'id_pokmov': 5, "pokemon": {"num_especie": 18,  "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}}
    ]},
    { "_id": 5,  "nome": "Hydro Pump",    "tipo": "água", 'pokemon_movimento': [
        {'id_pokmov': 3, "pokemon": {"num_especie": 9,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}},
        {'id_pokmov': 8, "pokemon": {"num_especie": 130, "id_natureza": 2, "rota": "Cerulean City",   "regiao": "Kanto", "treinador": 2}}
    ]},
    { "_id": 6,  "nome": "Vine Whip",     "tipo": "planta", 'pokemon_movimento': [
        {'id_pokmov': 4, "pokemon": {"num_especie": 3,   "id_natureza": 1, "rota": None,              "regiao": "Kanto", "treinador": 1}}
    ]},
    { "_id": 7,  "nome": "Water Gun",     "tipo": "água", 'pokemon_movimento': [
        {'id_pokmov': 6, "pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}},
        {'id_pokmov': 9, "pokemon": {"num_especie": 7,   "id_natureza": 2, "rota": "Pallet Town",     "regiao": "Kanto", "treinador": 3}}
    ]},
    { "_id": 8,  "nome": "Earthquake",    "tipo": "terra", 'pokemon_movimento': [
        {'id_pokmov': 10,"pokemon": {"num_especie": 112, "id_natureza": 3, "rota": "Victory Road",    "regiao": "Kanto", "treinador": 4}}
    ]},
    { "_id": 9,  "nome": "Psychic",       "tipo": "psíquico", 'pokemon_movimento': [
        {'id_pokmov': 11,"pokemon": {"num_especie": 65,  "id_natureza": 2, "rota": "Saffron City",    "regiao": "Kanto", "treinador": 3}},
        {'id_pokmov': 12,"pokemon": {"num_especie": 150, "id_natureza": 4, "rota": "Cerulean Cave",   "regiao": "Kanto", "treinador": None}}
    ]},
    { "_id": 10, "nome": "Ice Beam",      "tipo": "gelo", 'pokemon_movimento': [
        {'id_pokmov': 13,"pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}},
        {'id_pokmov': 14,"pokemon": {"num_especie": 124, "id_natureza": 3, "rota": None,              "regiao": "Kanto", "treinador": 4}}
    ]},
    { "_id": 11, "nome": "Hyper Beam",    "tipo": "normal", 'pokemon_movimento': [
        {'id_pokmov': 15,"pokemon": {"num_especie": 149, "id_natureza": 2, "rota": None,              "regiao": "Kanto", "treinador": 5}}
    ]},
    { "_id": 12, "nome": "Double Kick",   "tipo": "lutador", 'pokemon_movimento': [
        {'id_pokmov': 16,"pokemon": {"num_especie": 31,  "id_natureza": 2, "rota": "Safari Zone",     "regiao": "Kanto", "treinador": 3}}
    ]},
    { "_id": 13, "nome": "Poison Sting",  "tipo": "veneno", 'pokemon_movimento': [
        {'id_pokmov': 17,"pokemon": {"num_especie": 15,  "id_natureza": 3, "rota": None,              "regiao": "Kanto", "treinador": 5}}
    ]},
    { "_id": 14, "nome": "Blizzard",      "tipo": "gelo", 'pokemon_movimento': [
        {'id_pokmov': 18,"pokemon": {"num_especie": 144, "id_natureza": 4, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": None}},
        {'id_pokmov': 19,"pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}}
    ]},
    { "_id": 15, "nome": "Surf",          "tipo": "água", 'pokemon_movimento': [
        {'id_pokmov': 20,"pokemon": {"num_especie": 131, "id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}},
        {'id_pokmov': 21,"pokemon": {"num_especie": 9,   "id_natureza": 2, "rota": "Cerulean City",   "regiao": "Kanto", "treinador": 2}},
        {'id_pokmov': 22,"pokemon": {"num_especie": 130, "id_natureza": 3, "rota": None,              "regiao": "Kanto", "treinador": 4}}
    ]}
]


cliente.drop_database('banco_de_dados')
movimento.insert_many(lista_movimentos)

# Consultar quais movimentos um pokémon tem

num = int(input("Insira o número do pokémon: "))
id_pokemon = int(input("Insira o numero do id do pokémon: "))

for movs in movimento.find({"pokemon_movimento.pokemon.num_especie": num, "pokemon_movimento.pokemon.id_natureza": id_pokemon}):
    print(f'{movs['nome']}, {movs['tipo']}')