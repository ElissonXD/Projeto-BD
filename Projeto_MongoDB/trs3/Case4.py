# Relacionamento 1:N: cada "pokemon" EMBUTE um array de subdocs "movimentos"
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]

lista_pokemons = [
    {"_id": 1, "nome": "Pikachu", "movimentos": [
        {"nome": "Thunderbolt", "tipo": "Elétrico"},
        {"nome": "Quick Attack","tipo": "Normal"},
        {"nome": "Iron Tail",   "tipo": "Aço"},
    ]},
    {"_id": 2, "nome": "Charizard", "movimentos": [
        {"nome": "Flamethrower","tipo": "Fogo"},
        {"nome": "Wing Attack", "tipo": "Voador"},   # Wing Attack repetido em Pidgeot
    ]},
    {"_id": 3, "nome": "Starmie", "movimentos": [
        {"nome": "Surf",        "tipo": "Água"},     # Surf repetido em Lapras e Gyarados
        {"nome": "Hydro Pump",  "tipo": "Água"},     # Hydro Pump repetido em Gyarados e Blastoise
    ]},
    {"_id": 4, "nome": "Eevee", "movimentos": [
        {"nome": "Quick Attack","tipo": "Normal"},   # Quick Attack repetido (Pikachu)
    ]},
    {"_id": 5, "nome": "Lapras", "movimentos": [
        {"nome": "Surf",        "tipo": "Água"},     # repetido
        {"nome": "Ice Beam",    "tipo": "Gelo"},     # repetido (Blastoise)
    ]},
    {"_id": 6, "nome": "Gyarados", "movimentos": [
        {"nome": "Surf",        "tipo": "Água"},     # repetido
        {"nome": "Hydro Pump",  "tipo": "Água"},     # repetido
    ]},
    {"_id": 7, "nome": "Blastoise", "movimentos": [
        {"nome": "Hydro Pump",  "tipo": "Água"},     # repetido
        {"nome": "Ice Beam",    "tipo": "Gelo"},     # repetido
    ]},
    {"_id": 8, "nome": "Pidgeot", "movimentos": [
        {"nome": "Wing Attack", "tipo": "Voador"},   # repetido
    ]},
]

# Reset do banco e inserção
cliente.drop_database("banco_de_dados")
pokemons.insert_many(lista_pokemons)

nome_pokemon = input("Digite o nome do Pokémon: ").strip()

poke = pokemons.find_one({"nome": nome_pokemon}, projection={"_id": 0, "movimentos.nome": 1})
if not poke:
    print("Pokémon não encontrado.")
else:
    movs = poke.get("movimentos", [])
    if movs:
        print(*[m["nome"] for m in movs], sep="\n")
    else:
        print("Esse Pokémon não possui movimentos cadastrados.")
