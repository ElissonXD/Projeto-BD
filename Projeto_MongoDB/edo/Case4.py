#um documento embutindo vários documentos
# movimento 1 - N pokemon_movimento
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

pokemon_movimento = banco['pokemon_movimento']

lista_pokmov = [
    {"_id": 1, "movimento": [{ "_id": 1, "nome": "Thunderbolt",   "tipo": "elétrico" }, { "_id": 2, "nome": "Quick Attack",  "tipo": "normal" }], "pokemon": {"num_especie": 25, "id_natureza": 1, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 1}},
    {"_id": 2, "movimento": [{ "_id": 3, "nome": "Flamethrower",  "tipo": "fogo" },     { "_id": 4, "nome": "Wing Attack",   "tipo": "voador" }],  "pokemon": {"num_especie": 6,  "id_natureza": 1, "rota": None, "regiao": "Kanto", "treinador": 1}},
    {"_id": 3, "movimento": [{ "_id": 5, "nome": "Hydro Pump",    "tipo": "água" }],   "pokemon": {"num_especie": 9,  "id_natureza": 1, "rota": None, "regiao": "Kanto", "treinador": 1}},
    {"_id": 4, "movimento": [{ "_id": 6, "nome": "Vine Whip",     "tipo": "planta" }], "pokemon": {"num_especie": 3,  "id_natureza": 1, "rota": None, "regiao": "Kanto", "treinador": 1}},
    {"_id": 5, "movimento": [{ "_id": 4, "nome": "Wing Attack",   "tipo": "voador" }], "pokemon": {"num_especie": 18, "id_natureza": 1, "rota": None, "regiao": "Kanto", "treinador": 1}},
    {"_id": 6, "movimento": [{ "_id": 7, "nome": "Water Gun",     "tipo": "água" }],   "pokemon": {"num_especie": 131,"id_natureza": 1, "rota": "Seafoam Islands", "regiao": "Kanto", "treinador": 1}}
]

cliente.drop_database('banco_de_dados')
pokemon_movimento.insert_many(lista_pokmov)

# Consultar quais movimentos um pokémon tem

num = int(input("Insira o número do pokémon: "))
id_pokemon = int(input("Insira o numero do id do pokémon: "))

for pokmov in pokemon_movimento.find({"pokemon.num_especie": num, "pokemon.id_natureza": id_pokemon}):
    for mov in pokmov['movimento']:
        print(f'{mov['nome']}, {mov['tipo']}')