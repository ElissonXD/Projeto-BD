# um documento com um array de referências para documentos
# Relacionamento 1:N modelado como: cada documento de "pokemon" guarda um ARRAY de _ids de "movimento"
# Consulta: nomes dos movimentos do Pokémon com nome = <entrada>
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]
movimentos = banco["movimento"]

lista_movimentos = [
    {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico"},
    {"_id": 102, "nome": "Quick Attack", "tipo": "Normal"},
    {"_id": 103, "nome": "Iron Tail", "tipo": "Aço"},
    {"_id": 201, "nome": "Flamethrower", "tipo": "Fogo"},
    {"_id": 202, "nome": "Fly", "tipo": "Voador"},
    {"_id": 301, "nome": "Surf", "tipo": "Água"},
    {"_id": 302, "nome": "Hydro Pump", "tipo": "Água"},
]

lista_pokemons = [
    {"_id": 1, "nome": "Pikachu",  "movimentos_refs": [101, 102, 103]},
    {"_id": 2, "nome": "Charizard","movimentos_refs": [201, 202]},
    {"_id": 3, "nome": "Starmie",  "movimentos_refs": [301, 302]},
]

# Reset do banco e inserção
cliente.drop_database("banco_de_dados")
movimentos.insert_many(lista_movimentos)
pokemons.insert_many(lista_pokemons)

nome_pokemon = input("Digite o nome do Pokémon: ").strip()

poke = pokemons.find_one({"nome": nome_pokemon}, projection={"_id": 0, "movimentos_refs": 1})
if not poke:
    print("Pokémon não encontrado.")
else:
    if not poke.get("movimentos_refs"):
        print("Esse Pokémon não possui movimentos cadastrados.")
    else:
        cursor = movimentos.find({"_id": {"$in": poke["movimentos_refs"]}}, projection={"_id": 0, "nome": 1})
        nomes = [m["nome"] for m in cursor]
        print(*nomes, sep="\\n") if nomes else print("Movimentos não encontrados.")
