import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

pokemons = banco['pokemon']

treinadores = banco['treinador']

especies = banco['especie']



lista_pokemons = [
    # Pokémon de Ash
    {"_id": {"num_especie": 25, "id_natureza": 1}, "rota": "Viridian Forest", "regiao": "Kanto"},
    {"_id": {"num_especie": 6, "id_natureza": 1}, "rota": None, "regiao": "Kanto"},
    {"_id": {"num_especie": 9, "id_natureza": 1}, "rota": None, "regiao": "Kanto"},
    
    # Pokémon de Misty
    {"_id": {"num_especie": 121, "id_natureza": 1}, "rota": None, "regiao": "Kanto"},
    {"_id": {"num_especie": 54, "id_natureza": 1}, "rota": "Rota 24", "regiao": "Kanto"},
    {"_id": {"num_especie": 118, "id_natureza": 1}, "rota": "Rota 6", "regiao": "Kanto"},
    
    # Pokémon de Brock
    {"_id": {"num_especie": 95, "id_natureza": 1}, "rota": "Rock Tunnel", "regiao": "Kanto"},
    {"_id": {"num_especie": 74, "id_natureza": 1}, "rota": "Mt. Moon", "regiao": "Kanto"},
    {"_id": {"num_especie": 37, "id_natureza": 1}, "rota": "Rota 7", "regiao": "Kanto"},
    
    # Pokémon de Gary Oak
    {"_id": {"num_especie": 9, "id_natureza": 2}, "rota": None, "regiao": "Kanto"},
    {"_id": {"num_especie": 59, "id_natureza": 1}, "rota": None, "regiao": "Kanto"},
    {"_id": {"num_especie": 65, "id_natureza": 1}, "rota": None, "regiao": "Kanto"},
    {"_id": {"num_especie": 18, "id_natureza": 2}, "rota": None, "regiao": "Kanto"},
    
    # Pokémon de Red
    {"_id": {"num_especie": 3, "id_natureza": 2}, "rota": None, "regiao": "Kanto"},
    {"_id": {"num_especie": 25, "id_natureza": 2}, "rota": "Viridian Forest", "regiao": "Kanto"},
    {"_id": {"num_especie": 143, "id_natureza": 1}, "rota": "Rota 12", "regiao": "Kanto"},
    
    # Pokémon de Blue
    {"_id": {"num_especie": 6, "id_natureza": 2}, "rota": None, "regiao": "Kanto"},
    {"_id": {"num_especie": 112, "id_natureza": 1}, "rota": "Cerulean Cave", "regiao": "Kanto"},
    {"_id": {"num_especie": 103, "id_natureza": 1}, "rota": None, "regiao": "Kanto"},
]



lista_treinadores =[
    {
        "_id": 1, 
        "nome": "Ash Ketchum", 
        "pokemon_refs": [
            {"num_especie": 25, "id_natureza": 1},
            {"num_especie": 6, "id_natureza": 1},
            {"num_especie": 9, "id_natureza": 1}
        ]
    },
    {
        "_id": 2, 
        "nome": "Misty", 
        "pokemon_refs": [
            {"num_especie": 121, "id_natureza": 1},
            {"num_especie": 54, "id_natureza": 1},
            {"num_especie": 118, "id_natureza": 1}
        ]
    },
    {
        "_id": 3, 
        "nome": "Brock", 
        "pokemon_refs": [
            {"num_especie": 95, "id_natureza": 1},
            {"num_especie": 74, "id_natureza": 1},
            {"num_especie": 37, "id_natureza": 1}
        ]
    },
    {
        "_id": 4, 
        "nome": "Gary Oak", 
        "pokemon_refs": [
            {"num_especie": 9, "id_natureza": 2},
            {"num_especie": 59, "id_natureza": 1},
            {"num_especie": 65, "id_natureza": 1},
            {"num_especie": 18, "id_natureza": 2}
        ]
    },
    {
        "_id": 5, 
        "nome": "Red", 
        "pokemon_refs": [
            {"num_especie": 3, "id_natureza": 2},
            {"num_especie": 25, "id_natureza": 2},
            {"num_especie": 143, "id_natureza": 1}
        ]
    },
    {
        "_id": 6, 
        "nome": "Blue", 
        "pokemon_refs": [
            {"num_especie": 6, "id_natureza": 2},
            {"num_especie": 112, "id_natureza": 1},
            {"num_especie": 103, "id_natureza": 1}
        ]
    }

]



lista_especies = [
    {"_id": 1, "nome": "Bulbasaur", "tipos": ["Planta", "Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 2, "nome": "Ivysaur", "tipos": ["Planta", "Veneno"], "pre_evolucao": 1, "pre_requisito": "Level 16"},
    {"_id": 3, "nome": "Venusaur", "tipos": ["Planta", "Veneno"], "pre_evolucao": 2, "pre_requisito": "Level 32"},
    {"_id": 4, "nome": "Charmander", "tipos": ["Fogo"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 5, "nome": "Charmeleon", "tipos": ["Fogo"], "pre_evolucao": 4, "pre_requisito": "Level 16"},
    {"_id": 6, "nome": "Charizard", "tipos": ["Fogo", "Voador"], "pre_evolucao": 5, "pre_requisito": "Level 36"},
    {"_id": 7, "nome": "Squirtle", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 8, "nome": "Wartortle", "tipos": ["Água"], "pre_evolucao": 7, "pre_requisito": "Level 16"},
    {"_id": 9, "nome": "Blastoise", "tipos": ["Água"], "pre_evolucao": 8, "pre_requisito": "Level 36"},
    {"_id": 25, "nome": "Pikachu", "tipos": ["Elétrico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 37, "nome": "Vulpix", "tipos": ["Fogo"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 54, "nome": "Psyduck", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 58, "nome": "Growlithe", "tipos": ["Fogo"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 59, "nome": "Arcanine", "tipos": ["Fogo"], "pre_evolucao": 58, "pre_requisito": "Fire Stone"},
    {"_id": 63, "nome": "Abra", "tipos": ["Psíquico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 64, "nome": "Kadabra", "tipos": ["Psíquico"], "pre_evolucao": 63, "pre_requisito": "Level 16"},
    {"_id": 65, "nome": "Alakazam", "tipos": ["Psíquico"], "pre_evolucao": 64, "pre_requisito": "Trade"},
    {"_id": 74, "nome": "Geodude", "tipos": ["Rocha", "Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 95, "nome": "Onix", "tipos": ["Rocha", "Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 102, "nome": "Exeggcute", "tipos": ["Planta", "Psíquico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 103, "nome": "Exeggutor", "tipos": ["Planta", "Psíquico"], "pre_evolucao": 102, "pre_requisito": "Leaf Stone"},
    {"_id": 111, "nome": "Rhyhorn", "tipos": ["Rocha", "Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 112, "nome": "Rhydon", "tipos": ["Rocha", "Terra"], "pre_evolucao": 111, "pre_requisito": "Level 42"},
    {"_id": 118, "nome": "Goldeen", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 120, "nome": "Staryu", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 121, "nome": "Starmie", "tipos": ["Água", "Psíquico"], "pre_evolucao": 120, "pre_requisito": "Water Stone"},
    {"_id": 143, "nome": "Snorlax", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
]




cliente.drop_database('banco_de_dados')
# Inserindo novos dados
treinadores.insert_many(lista_treinadores)
pokemons.insert_many(lista_pokemons)
especies.insert_many(lista_especies)


id_treinador = int(input("coloque o id do treinador: "))

filter_treinador = {"_id": id_treinador}
cursor_treinador = treinadores.find_one(filter_treinador)

if cursor_treinador:
    print("-" * 20)
    for pokemon_ref in cursor_treinador["pokemon_refs"]:
        especie = especies.find_one({"_id": pokemon_ref["num_especie"]})
        pokemon = pokemons.find_one({"_id": pokemon_ref})
        if especie:
            print(f"Pokemon: {especie['nome']}, N°_pokedex: {pokemon_ref['num_especie']}, Id_natureza: {pokemon_ref['id_natureza']}, Tipos: {', '.join(especie['tipos'])}, Rota: {pokemon['rota']}, Regiao: {pokemon['regiao']}")
    print("-" * 20)
else:
    print(f"Nenhum Pokémon encontrado para o treinador com ID {id_treinador}.")
