import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

treinadores = banco['treinador']

lista_treinadores_case_3 =[
    {"_id": 1, "nome": "Ash Ketchum", "pokemon": [1, 2, 3, 4, 5, 6]},
    {"_id": 2, "nome": "Misty", "pokemon": [7, 8, 9]},
    {"_id": 3, "nome": "Brock", "pokemon": [10, 11, 12]},
    {"_id": 4, "nome": "Gary Oak", "pokemon": [13, 14, 15, 16]},
    {"_id": 5, "nome": "Red", "pokemon": [17, 18, 19]},
    {"_id": 6, "nome": "Blue", "pokemon": [20, 21, 22]},
    {"_id": 7, "nome": "Erika", "pokemon": [23, 24, 25]},
    {"_id": 8, "nome": "Lt. Surge", "pokemon": [26, 27, 28]},
    {"_id": 9, "nome": "Sabrina", "pokemon": [29, 30, 31]},
    {"_id": 10, "nome": "Giovanni", "pokemon": [32, 33, 34]}
]

pokemons = banco['pokemon']

lista_pokemons_case_3 = [
    # Pokémon de Ash
    {"_id": 1, "especie": 25, "nome": "Pikachu", "index": 1, "tipo": "Elétrico", "rota": "Viridian Forest", "regiao": "Kanto"},
    {"_id": 2, "especie": 6, "nome": "Charizard", "index": 1, "tipo": "Fogo, Voador", "rota": "Evoluído (Charmander)", "regiao": "Kanto"},
    {"_id": 3, "especie": 9, "nome": "Blastoise", "index": 1, "tipo": "Água", "rota": "Evoluído (Squirtle)", "regiao": "Kanto"},
    {"_id": 4, "especie": 3, "nome": "Venusaur", "index": 1, "tipo": "Grama, Venenoso", "rota": "Evoluído (Bulbasaur)", "regiao": "Kanto"},
    {"_id": 5, "especie": 18, "nome": "Pidgeot", "index": 1, "tipo": "Normal, Voador", "rota": "Rota 1 (Pidgey)", "regiao": "Kanto"},
    {"_id": 6, "especie": 131, "nome": "Lapras", "index": 1, "tipo": "Água, Gelo", "rota": "Silph Co.", "regiao": "Kanto"},
    # Pokémon de Misty
    {"_id": 7, "especie": 121, "nome": "Starmie", "index": 1, "tipo": "Água, Psíquico", "rota": "Seafoam Islands (Staryu)", "regiao": "Kanto"},
    {"_id": 8, "especie": 54, "nome": "Psyduck", "index": 1, "tipo": "Água", "rota": "Rota 24", "regiao": "Kanto"},
    {"_id": 9, "especie": 118, "nome": "Goldeen", "index": 1, "tipo": "Água", "rota": "Rotas 6, 24 (pescando)", "regiao": "Kanto"},
    # Pokémon de Brock
    {"_id": 10, "especie": 95, "nome": "Onix", "index": 1, "tipo": "Pedra, Terrestre", "rota": "Rock Tunnel", "regiao": "Kanto"},
    {"_id": 11, "especie": 74, "nome": "Geodude", "index": 1, "tipo": "Pedra, Terrestre", "rota": "Mt. Moon", "regiao": "Kanto"},
    {"_id": 12, "especie": 37, "nome": "Vulpix", "index": 1, "tipo": "Fogo", "rota": "Rota 7", "regiao": "Kanto"},
    # Pokémon de Gary Oak
    {"_id": 13, "especie": 9, "nome": "Blastoise", "index": 2, "tipo": "Água", "rota": "Evoluído (Squirtle)", "regiao": "Kanto"},
    {"_id": 14, "especie": 59, "nome": "Arcanine", "index": 1, "tipo": "Fogo", "rota": "Evoluído (Growlithe)", "regiao": "Kanto"},
    {"_id": 15, "especie": 65, "nome": "Alakazam", "index": 1, "tipo": "Psíquico", "rota": "Evoluído (Kadabra)", "regiao": "Kanto"},
    {"_id": 16, "especie": 18, "nome": "Pidgeot", "index": 2, "tipo": "Normal, Voador", "rota": "Rota 1 (Pidgey)", "regiao": "Kanto"},
    # Pokémon de Red
    {"_id": 17, "especie": 3, "nome": "Venusaur", "index": 2, "tipo": "Grama, Venenoso", "rota": "Evoluído (Bulbasaur)", "regiao": "Kanto"},
    {"_id": 18, "especie": 25, "nome": "Pikachu", "index": 2, "tipo": "Elétrico", "rota": "Viridian Forest", "regiao": "Kanto"},
    {"_id": 19, "especie": 143, "nome": "Snorlax", "index": 1, "tipo": "Normal", "rota": "Rota 12", "regiao": "Kanto"},
    # Pokémon de Blue
    {"_id": 20, "especie": 6, "nome": "Charizard", "index": 2, "tipo": "Fogo, Voador", "rota": "Evoluído (Charmander)", "regiao": "Kanto"},
    {"_id": 21, "especie": 112, "nome": "Rhydon", "index": 1, "tipo": "Pedra, Terrestre", "rota": "Cerulean Cave", "regiao": "Kanto"},
    {"_id": 22, "especie": 103, "nome": "Exeggutor", "index": 1, "tipo": "Grama, Psíquico", "rota": "Evoluído (Exeggcute)", "regiao": "Kanto"},
    # Pokémon de Erika
    {"_id": 23, "especie": 45, "nome": "Vileplume", "index": 1, "tipo": "Grama, Venenoso", "rota": "Evoluído (Oddish)", "regiao": "Kanto"},
    {"_id": 24, "especie": 114, "nome": "Tangela", "index": 1, "tipo": "Grama", "rota": "Rota 21", "regiao": "Kanto"},
    {"_id": 25, "especie": 71, "nome": "Victreebel", "index": 1, "tipo": "Grama, Venenoso", "rota": "Evoluído (Bellsprout)", "regiao": "Kanto"},
    # Pokémon de Lt. Surge
    {"_id": 26, "especie": 26, "nome": "Raichu", "index": 1, "tipo": "Elétrico", "rota": "Evoluído (Pikachu)", "regiao": "Kanto"},
    {"_id": 27, "especie": 101, "nome": "Electrode", "index": 1, "tipo": "Elétrico", "rota": "Power Plant", "regiao": "Kanto"},
    {"_id": 28, "especie": 82, "nome": "Magneton", "index": 1, "tipo": "Elétrico", "rota": "Power Plant", "regiao": "Kanto"},
    # Pokémon de Sabrina
    {"_id": 29, "especie": 65, "nome": "Alakazam", "index": 2, "tipo": "Psíquico", "rota": "Evoluído (Kadabra)", "regiao": "Kanto"},
    {"_id": 30, "especie": 49, "nome": "Venomoth", "index": 1, "tipo": "Inseto, Venenoso", "rota": "Cerulean Cave", "regiao": "Kanto"},
    {"_id": 31, "especie": 122, "nome": "Mr. Mime", "index": 1, "tipo": "Psíquico", "rota": "Rota 2 (troca)", "regiao": "Kanto"},
    # Pokémon de Giovanni
    {"_id": 32, "especie": 53, "nome": "Persian", "index": 1, "tipo": "Normal", "rota": "Evoluído (Meowth)", "regiao": "Kanto"},
    {"_id": 33, "especie": 34, "nome": "Nidoking", "index": 1, "tipo": "Venenoso, Terrestre", "rota": "Evoluído (Nidorino)", "regiao": "Kanto"},
    {"_id": 34, "especie": 112, "nome": "Rhydon", "index": 2, "tipo": "Pedra, Terrestre", "rota": "Cerulean Cave", "regiao": "Kanto"}
]
