# Relacionamento 1:N: cada documento de "movimento" EMBUTE UM "pokemon"
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
movimentos = banco["movimento"]

lista_movimentos = [
    # Pikachu
    {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico", "pokemon": {"_id": 1, "nome": "Pikachu"}},
    {"_id": 102, "nome": "Quick Attack","tipo": "Normal",   "pokemon": {"_id": 1, "nome": "Pikachu"}},
    {"_id": 103, "nome": "Iron Tail",   "tipo": "Aço",      "pokemon": {"_id": 1, "nome": "Pikachu"}},
    # Charizard
    {"_id": 201, "nome": "Flamethrower","tipo": "Fogo",     "pokemon": {"_id": 2, "nome": "Charizard"}},
    {"_id": 202, "nome": "Wing Attack", "tipo": "Voador",   "pokemon": {"_id": 2, "nome": "Charizard"}},
    # Starmie
    {"_id": 301, "nome": "Surf",        "tipo": "Água",     "pokemon": {"_id": 3, "nome": "Starmie"}},
    {"_id": 302, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon": {"_id": 3, "nome": "Starmie"}},
    # Eevee (Quick Attack repetido)
    {"_id": 401, "nome": "Quick Attack","tipo": "Normal",   "pokemon": {"_id": 4, "nome": "Eevee"}},
    # Lapras (Surf, Ice Beam repetidos)
    {"_id": 501, "nome": "Surf",        "tipo": "Água",     "pokemon": {"_id": 5, "nome": "Lapras"}},
    {"_id": 502, "nome": "Ice Beam",    "tipo": "Gelo",     "pokemon": {"_id": 5, "nome": "Lapras"}},
    # Gyarados (Surf, Hydro Pump repetidos)
    {"_id": 601, "nome": "Surf",        "tipo": "Água",     "pokemon": {"_id": 6, "nome": "Gyarados"}},
    {"_id": 602, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon": {"_id": 6, "nome": "Gyarados"}},
    # Blastoise (Hydro Pump, Ice Beam repetidos)
    {"_id": 701, "nome": "Hydro Pump",  "tipo": "Água",     "pokemon": {"_id": 7, "nome": "Blastoise"}},
    {"_id": 702, "nome": "Ice Beam",    "tipo": "Gelo",     "pokemon": {"_id": 7, "nome": "Blastoise"}},
    # Pidgeot (Wing Attack repetido)
    {"_id": 801, "nome": "Wing Attack", "tipo": "Voador",   "pokemon": {"_id": 8, "nome": "Pidgeot"}},
]

# Reset do banco e inserção
cliente.drop_database("banco_de_dados")
movimentos.insert_many(lista_movimentos)

nome_pokemon = input("Digite o nome do Pokémon: ").strip()

cursor = movimentos.find({"pokemon.nome": nome_pokemon}, projection={"_id": 0, "nome": 1})
nomes = [m["nome"] for m in cursor]
if nomes:
    print(*nomes, sep="\n")
else:
    print("Pokémon não encontrado ou sem movimentos cadastrados.")
