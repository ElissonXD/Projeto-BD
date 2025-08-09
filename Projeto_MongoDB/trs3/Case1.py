# um documento referenciando apenas um documento
# Relacionamento 1:N modelado como: cada documento de "movimento" referencia UM "pokemon"
# Consulta: nomes dos movimentos do Pokémon com nome = <entrada>
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
pokemons = banco["pokemon"]
movimentos = banco["movimento"]

# Dados de exemplo
lista_pokemons = [
    {"_id": 1, "nome": "Pikachu", "regiao": "Kanto"},
    {"_id": 2, "nome": "Charizard", "regiao": "Kanto"},
    {"_id": 3, "nome": "Starmie", "regiao": "Kanto"},
]

lista_movimentos = [
    {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico", "pokemon_id": 1},
    {"_id": 102, "nome": "Quick Attack", "tipo": "Normal", "pokemon_id": 1},
    {"_id": 103, "nome": "Iron Tail", "tipo": "Aço", "pokemon_id": 1},
    {"_id": 201, "nome": "Flamethrower", "tipo": "Fogo", "pokemon_id": 2},
    {"_id": 202, "nome": "Fly", "tipo": "Voador", "pokemon_id": 2},
    {"_id": 301, "nome": "Surf", "tipo": "Água", "pokemon_id": 3},
    {"_id": 302, "nome": "Hydro Pump", "tipo": "Água", "pokemon_id": 3},
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
        print(*nomes, sep="\\n")
    else:
        print("Esse Pokémon não possui movimentos cadastrados.")
