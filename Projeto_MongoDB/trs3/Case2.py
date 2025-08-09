# um documento embutindo apenas um documento
# Relacionamento 1:N modelado como: cada documento de "movimento" EMBUTE UM "pokemon"
# (duplica o mínimo necessário do lado "1" para cada "N")
# Consulta: nomes dos movimentos do Pokémon com nome = <entrada>
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente["banco_de_dados"]
movimentos = banco["movimento"]

# Dados de exemplo (cada movimento embute um doc de pokemon)
lista_movimentos = [
    {"_id": 101, "nome": "Thunderbolt", "tipo": "Elétrico", "pokemon": {"_id": 1, "nome": "Pikachu"}},
    {"_id": 102, "nome": "Quick Attack", "tipo": "Normal", "pokemon": {"_id": 1, "nome": "Pikachu"}},
    {"_id": 103, "nome": "Iron Tail", "tipo": "Aço", "pokemon": {"_id": 1, "nome": "Pikachu"}},
    {"_id": 201, "nome": "Flamethrower", "tipo": "Fogo", "pokemon": {"_id": 2, "nome": "Charizard"}},
    {"_id": 202, "nome": "Fly", "tipo": "Voador", "pokemon": {"_id": 2, "nome": "Charizard"}},
    {"_id": 301, "nome": "Surf", "tipo": "Água", "pokemon": {"_id": 3, "nome": "Starmie"}},
    {"_id": 302, "nome": "Hydro Pump", "tipo": "Água", "pokemon": {"_id": 3, "nome": "Starmie"}},
]

# Reset do banco e inserção
cliente.drop_database("banco_de_dados")
movimentos.insert_many(lista_movimentos)

nome_pokemon = input("Digite o nome do Pokémon: ").strip()

cursor = movimentos.find({"pokemon.nome": nome_pokemon}, projection={"_id": 0, "nome": 1})
nomes = [m["nome"] for m in cursor]
if nomes:
    print(*nomes, sep="\\n")
else:
    print("Pokémon não encontrado ou sem movimentos cadastrados.")
