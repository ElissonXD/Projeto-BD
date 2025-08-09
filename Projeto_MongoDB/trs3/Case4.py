# um documento embutindo vários documentos
# Relacionamento 1:N modelado como: cada documento de "pokemon" EMBUTE um array de subdocumentos "movimentos"
# Consulta: nomes dos movimentos do Pokémon com nome = <entrada>
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]

lista_pokemons = [
    {"_id": 1, "nome": "Pikachu", "movimentos": [
        {"nome": "Thunderbolt", "tipo": "Elétrico"},
        {"nome": "Quick Attack", "tipo": "Normal"},
        {"nome": "Iron Tail", "tipo": "Aço"},
    ]},
    {"_id": 2, "nome": "Charizard", "movimentos": [
        {"nome": "Flamethrower", "tipo": "Fogo"},
        {"nome": "Fly", "tipo": "Voador"},
    ]},
    {"_id": 3, "nome": "Starmie", "movimentos": [
        {"nome": "Surf", "tipo": "Água"},
        {"nome": "Hydro Pump", "tipo": "Água"},
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
        print(*[m["nome"] for m in movs], sep="\\n")
    else:
        print("Esse Pokémon não possui movimentos cadastrados.")
