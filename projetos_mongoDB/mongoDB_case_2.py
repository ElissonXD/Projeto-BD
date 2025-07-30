import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

pokemons = banco['pokemon']

especies = banco['especie']



lista_pokemons = [
    # Pokémon de Ash
    {"_id": {"num_especie": 25, "id_natureza": 1}, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": {"id_treinador": 1, "nome": "Ash Ketchum"}},
    {"_id": {"num_especie": 6, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 1, "nome": "Ash Ketchum"}},
    {"_id": {"num_especie": 9, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 1, "nome": "Ash Ketchum"}},
    {"_id": {"num_especie": 3, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 1, "nome": "Ash Ketchum"}},
    {"_id": {"num_especie": 18, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 1, "nome": "Ash Ketchum"}},
    {"_id": {"num_especie": 131, "id_natureza": 1}, "rota": "Silph Co.", "regiao": "Kanto", "treinador": {"id_treinador": 1, "nome": "Ash Ketchum"}},
    
    # Pokémon de Misty
    {"_id": {"num_especie": 121, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 2, "nome": "Misty"}},
    {"_id": {"num_especie": 54, "id_natureza": 1}, "rota": "Rota 24", "regiao": "Kanto", "treinador": {"id_treinador": 2, "nome": "Misty"}},
    {"_id": {"num_especie": 118, "id_natureza": 1}, "rota": "Rota 6", "regiao": "Kanto", "treinador": {"id_treinador": 2, "nome": "Misty"}},

    # Pokémon de Brock
    {"_id": {"num_especie": 95, "id_natureza": 1}, "rota": "Rock Tunnel", "regiao": "Kanto", "treinador": {"id_treinador": 3, "nome": "Brock"}},
    {"_id": {"num_especie": 74, "id_natureza": 1}, "rota": "Mt. Moon", "regiao": "Kanto", "treinador": {"id_treinador": 3, "nome": "Brock"}},
    {"_id": {"num_especie": 37, "id_natureza": 1}, "rota": "Rota 7", "regiao": "Kanto", "treinador": {"id_treinador": 3, "nome": "Brock"}},

    # Pokémon de Gary Oak
    {"_id": {"num_especie": 9, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 4, "nome": "Gary Oak"}},
    {"_id": {"num_especie": 59, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 4, "nome": "Gary Oak"}},
    {"_id": {"num_especie": 65, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 4, "nome": "Gary Oak"}},
    {"_id": {"num_especie": 18, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 4, "nome": "Gary Oak"}},

    # Pokémon de Red
    {"_id": {"num_especie": 3, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 5, "nome": "Red"}},
    {"_id": {"num_especie": 25, "id_natureza": 2}, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": {"id_treinador": 5, "nome": "Red"}},
    {"_id": {"num_especie": 143, "id_natureza": 1}, "rota": "Rota 12", "regiao": "Kanto", "treinador": {"id_treinador": 5, "nome": "Red"}},

    # Pokémon de Blue
    {"_id": {"num_especie": 6, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 6, "nome": "Blue"}},
    {"_id": {"num_especie": 112, "id_natureza": 1}, "rota": "Cerulean Cave", "regiao": "Kanto", "treinador": {"id_treinador": 6, "nome": "Blue"}},
    {"_id": {"num_especie": 103, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 6, "nome": "Blue"}},

    # Pokémon de Erika
    {"_id": {"num_especie": 45, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 7, "nome": "Erika"}},
    {"_id": {"num_especie": 114, "id_natureza": 1}, "rota": "Rota 21", "regiao": "Kanto", "treinador": {"id_treinador": 7, "nome": "Erika"}},
    {"_id": {"num_especie": 71, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 7, "nome": "Erika"}},

    # Pokémon de Lt. Surge
    {"_id": {"num_especie": 26, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 8, "nome": "Lt. Surge"}},
    {"_id": {"num_especie": 101, "id_natureza": 1}, "rota": "Power Plant", "regiao": "Kanto", "treinador": {"id_treinador": 8, "nome": "Lt. Surge"}},
    {"_id": {"num_especie": 82, "id_natureza": 1}, "rota": "Power Plant", "regiao": "Kanto", "treinador": {"id_treinador": 8, "nome": "Lt. Surge"}},

    # Pokémon de Sabrina
    {"_id": {"num_especie": 65, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 9, "nome": "Sabrina"}},
    {"_id": {"num_especie": 49, "id_natureza": 1}, "rota": "Cerulean Cave", "regiao": "Kanto", "treinador": {"id_treinador": 9, "nome": "Sabrina"}},
    {"_id": {"num_especie": 122, "id_natureza": 1}, "rota": "Rota 2", "regiao": "Kanto", "treinador": {"id_treinador": 9, "nome": "Sabrina"}},

    # Pokémon de Giovanni
    {"_id": {"num_especie": 53, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 10, "nome": "Giovanni"}},
    {"_id": {"num_especie": 34, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": {"id_treinador": 10, "nome": "Giovanni"}},
    {"_id": {"num_especie": 112, "id_natureza": 2}, "rota": "Cerulean Cave", "regiao": "Kanto", "treinador": {"id_treinador": 10, "nome": "Giovanni"}}
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
    {"_id": 10, "nome": "Caterpie", "tipos": ["Inseto"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 11, "nome": "Metapod", "tipos": ["Inseto"], "pre_evolucao": 10, "pre_requisito": "Level 7"},
    {"_id": 12, "nome": "Butterfree", "tipos": ["Inseto", "Voador"], "pre_evolucao": 11, "pre_requisito": "Level 10"},
    {"_id": 13, "nome": "Weedle", "tipos": ["Inseto", "Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 14, "nome": "Kakuna", "tipos": ["Inseto", "Veneno"], "pre_evolucao": 13, "pre_requisito": "Level 7"},
    {"_id": 15, "nome": "Beedrill", "tipos": ["Inseto", "Veneno"], "pre_evolucao": 14, "pre_requisito": "Level 10"},
    {"_id": 16, "nome": "Pidgey", "tipos": ["Normal", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 17, "nome": "Pidgeotto", "tipos": ["Normal", "Voador"], "pre_evolucao": 16, "pre_requisito": "Level 18"},
    {"_id": 18, "nome": "Pidgeot", "tipos": ["Normal", "Voador"], "pre_evolucao": 17, "pre_requisito": "Level 36"},
    {"_id": 19, "nome": "Rattata", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 20, "nome": "Raticate", "tipos": ["Normal"], "pre_evolucao": 19, "pre_requisito": "Level 20"},
    {"_id": 21, "nome": "Spearow", "tipos": ["Normal", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 22, "nome": "Fearow", "tipos": ["Normal", "Voador"], "pre_evolucao": 21, "pre_requisito": "Level 20"},
    {"_id": 23, "nome": "Ekans", "tipos": ["Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 24, "nome": "Arbok", "tipos": ["Veneno"], "pre_evolucao": 23, "pre_requisito": "Level 22"},
    {"_id": 25, "nome": "Pikachu", "tipos": ["Elétrico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 26, "nome": "Raichu", "tipos": ["Elétrico"], "pre_evolucao": 25, "pre_requisito": "Thunder Stone"},
    {"_id": 27, "nome": "Sandshrew", "tipos": ["Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 28, "nome": "Sandslash", "tipos": ["Terra"], "pre_evolucao": 27, "pre_requisito": "Level 22"},
    {"_id": 29, "nome": "Nidoran♀", "tipos": ["Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 30, "nome": "Nidorina", "tipos": ["Veneno"], "pre_evolucao": 29, "pre_requisito": "Level 16"},
    {"_id": 31, "nome": "Nidoqueen", "tipos": ["Veneno", "Terra"], "pre_evolucao": 30, "pre_requisito": "Moon Stone"},
    {"_id": 32, "nome": "Nidoran♂", "tipos": ["Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 33, "nome": "Nidorino", "tipos": ["Veneno"], "pre_evolucao": 32, "pre_requisito": "Level 16"},
    {"_id": 34, "nome": "Nidoking", "tipos": ["Veneno", "Terra"], "pre_evolucao": 33, "pre_requisito": "Moon Stone"},
    {"_id": 35, "nome": "Clefairy", "tipos": ["Fada"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 36, "nome": "Clefable", "tipos": ["Fada"], "pre_evolucao": 35, "pre_requisito": "Moon Stone"},
    {"_id": 37, "nome": "Vulpix", "tipos": ["Fogo"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 38, "nome": "Ninetales", "tipos": ["Fogo"], "pre_evolucao": 37, "pre_requisito": "Fire Stone"},
    {"_id": 39, "nome": "Jigglypuff", "tipos": ["Normal", "Fada"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 40, "nome": "Wigglytuff", "tipos": ["Normal", "Fada"], "pre_evolucao": 39, "pre_requisito": "Moon Stone"},
    {"_id": 41, "nome": "Zubat", "tipos": ["Veneno", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 42, "nome": "Golbat", "tipos": ["Veneno", "Voador"], "pre_evolucao": 41, "pre_requisito": "Level 22"},
    {"_id": 43, "nome": "Oddish", "tipos": ["Planta", "Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 44, "nome": "Gloom", "tipos": ["Planta", "Veneno"], "pre_evolucao": 43, "pre_requisito": "Level 21"},
    {"_id": 45, "nome": "Vileplume", "tipos": ["Planta", "Veneno"], "pre_evolucao": 44, "pre_requisito": "Leaf Stone"},
    {"_id": 46, "nome": "Paras", "tipos": ["Inseto", "Planta"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 47, "nome": "Parasect", "tipos": ["Inseto", "Planta"], "pre_evolucao": 46, "pre_requisito": "Level 24"},
    {"_id": 48, "nome": "Venonat", "tipos": ["Inseto", "Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 49, "nome": "Venomoth", "tipos": ["Inseto", "Veneno"], "pre_evolucao": 48, "pre_requisito": "Level 31"},
    {"_id": 50, "nome": "Diglett", "tipos": ["Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 51, "nome": "Dugtrio", "tipos": ["Terra"], "pre_evolucao": 50, "pre_requisito": "Level 26"},
    {"_id": 52, "nome": "Meowth", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 53, "nome": "Persian", "tipos": ["Normal"], "pre_evolucao": 52, "pre_requisito": "Level 28"},
    {"_id": 54, "nome": "Psyduck", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 55, "nome": "Golduck", "tipos": ["Água"], "pre_evolucao": 54, "pre_requisito": "Level 33"},
    {"_id": 56, "nome": "Mankey", "tipos": ["Lutador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 57, "nome": "Primeape", "tipos": ["Lutador"], "pre_evolucao": 56, "pre_requisito": "Level 28"},
    {"_id": 58, "nome": "Growlithe", "tipos": ["Fogo"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 59, "nome": "Arcanine", "tipos": ["Fogo"], "pre_evolucao": 58, "pre_requisito": "Fire Stone"},
    {"_id": 60, "nome": "Poliwag", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 61, "nome": "Poliwhirl", "tipos": ["Água"], "pre_evolucao": 60, "pre_requisito": "Level 25"},
    {"_id": 62, "nome": "Poliwrath", "tipos": ["Água", "Lutador"], "pre_evolucao": 61, "pre_requisito": "Water Stone"},
    {"_id": 63, "nome": "Abra", "tipos": ["Psíquico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 64, "nome": "Kadabra", "tipos": ["Psíquico"], "pre_evolucao": 63, "pre_requisito": "Level 16"},
    {"_id": 65, "nome": "Alakazam", "tipos": ["Psíquico"], "pre_evolucao": 64, "pre_requisito": "Trade"},
    {"_id": 66, "nome": "Machop", "tipos": ["Lutador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 67, "nome": "Machoke", "tipos": ["Lutador"], "pre_evolucao": 66, "pre_requisito": "Level 28"},
    {"_id": 68, "nome": "Machamp", "tipos": ["Lutador"], "pre_evolucao": 67, "pre_requisito": "Trade"},
    {"_id": 69, "nome": "Bellsprout", "tipos": ["Planta", "Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 70, "nome": "Weepinbell", "tipos": ["Planta", "Veneno"], "pre_evolucao": 69, "pre_requisito": "Level 21"},
    {"_id": 71, "nome": "Victreebel", "tipos": ["Planta", "Veneno"], "pre_evolucao": 70, "pre_requisito": "Leaf Stone"},
    {"_id": 72, "nome": "Tentacool", "tipos": ["Água", "Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 73, "nome": "Tentacruel", "tipos": ["Água", "Veneno"], "pre_evolucao": 72, "pre_requisito": "Level 30"},
    {"_id": 74, "nome": "Geodude", "tipos": ["Rocha", "Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 75, "nome": "Graveler", "tipos": ["Rocha", "Terra"], "pre_evolucao": 74, "pre_requisito": "Level 25"},
    {"_id": 76, "nome": "Golem", "tipos": ["Rocha", "Terra"], "pre_evolucao": 75, "pre_requisito": "Trade"},
    {"_id": 77, "nome": "Ponyta", "tipos": ["Fogo"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 78, "nome": "Rapidash", "tipos": ["Fogo"], "pre_evolucao": 77, "pre_requisito": "Level 40"},
    {"_id": 79, "nome": "Slowpoke", "tipos": ["Água", "Psíquico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 80, "nome": "Slowbro", "tipos": ["Água", "Psíquico"], "pre_evolucao": 79, "pre_requisito": "Level 37"},
    {"_id": 81, "nome": "Magnemite", "tipos": ["Elétrico", "Aço"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 82, "nome": "Magneton", "tipos": ["Elétrico", "Aço"], "pre_evolucao": 81, "pre_requisito": "Level 30"},
    {"_id": 83, "nome": "Farfetch'd", "tipos": ["Normal", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 84, "nome": "Doduo", "tipos": ["Normal", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 85, "nome": "Dodrio", "tipos": ["Normal", "Voador"], "pre_evolucao": 84, "pre_requisito": "Level 31"},
    {"_id": 86, "nome": "Seel", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 87, "nome": "Dewgong", "tipos": ["Água", "Gelo"], "pre_evolucao": 86, "pre_requisito": "Level 34"},
    {"_id": 88, "nome": "Grimer", "tipos": ["Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 89, "nome": "Muk", "tipos": ["Veneno"], "pre_evolucao": 88, "pre_requisito": "Level 38"},
    {"_id": 90, "nome": "Shellder", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 91, "nome": "Cloyster", "tipos": ["Água", "Gelo"], "pre_evolucao": 90, "pre_requisito": "Water Stone"},
    {"_id": 92, "nome": "Gastly", "tipos": ["Fantasma", "Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 93, "nome": "Haunter", "tipos": ["Fantasma", "Veneno"], "pre_evolucao": 92, "pre_requisito": "Level 25"},
    {"_id": 94, "nome": "Gengar", "tipos": ["Fantasma", "Veneno"], "pre_evolucao": 93, "pre_requisito": "Trade"},
    {"_id": 95, "nome": "Onix", "tipos": ["Rocha", "Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 96, "nome": "Drowzee", "tipos": ["Psíquico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 97, "nome": "Hypno", "tipos": ["Psíquico"], "pre_evolucao": 96, "pre_requisito": "Level 26"},
    {"_id": 98, "nome": "Krabby", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 99, "nome": "Kingler", "tipos": ["Água"], "pre_evolucao": 98, "pre_requisito": "Level 28"},
    {"_id": 100, "nome": "Voltorb", "tipos": ["Elétrico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 101, "nome": "Electrode", "tipos": ["Elétrico"], "pre_evolucao": 100, "pre_requisito": "Level 30"},
    {"_id": 102, "nome": "Exeggcute", "tipos": ["Planta", "Psíquico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 103, "nome": "Exeggutor", "tipos": ["Planta", "Psíquico"], "pre_evolucao": 102, "pre_requisito": "Leaf Stone"},
    {"_id": 104, "nome": "Cubone", "tipos": ["Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 105, "nome": "Marowak", "tipos": ["Terra"], "pre_evolucao": 104, "pre_requisito": "Level 28"},
    {"_id": 106, "nome": "Hitmonlee", "tipos": ["Lutador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 107, "nome": "Hitmonchan", "tipos": ["Lutador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 108, "nome": "Lickitung", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 109, "nome": "Koffing", "tipos": ["Veneno"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 110, "nome": "Weezing", "tipos": ["Veneno"], "pre_evolucao": 109, "pre_requisito": "Level 35"},
    {"_id": 111, "nome": "Rhyhorn", "tipos": ["Rocha", "Terra"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 112, "nome": "Rhydon", "tipos": ["Rocha", "Terra"], "pre_evolucao": 111, "pre_requisito": "Level 42"},
    {"_id": 113, "nome": "Chansey", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 114, "nome": "Tangela", "tipos": ["Planta"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 115, "nome": "Kangaskhan", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 116, "nome": "Horsea", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 117, "nome": "Seadra", "tipos": ["Água"], "pre_evolucao": 116, "pre_requisito": "Level 32"},
    {"_id": 118, "nome": "Goldeen", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 119, "nome": "Seaking", "tipos": ["Água"], "pre_evolucao": 118, "pre_requisito": "Level 33"},
    {"_id": 120, "nome": "Staryu", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 121, "nome": "Starmie", "tipos": ["Água", "Psíquico"], "pre_evolucao": 120, "pre_requisito": "Water Stone"},
    {"_id": 122, "nome": "Mr. Mime", "tipos": ["Psíquico", "Fada"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 123, "nome": "Scyther", "tipos": ["Inseto", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 124, "nome": "Jynx", "tipos": ["Gelo", "Psíquico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 125, "nome": "Electabuzz", "tipos": ["Elétrico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 126, "nome": "Magmar", "tipos": ["Fogo"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 127, "nome": "Pinsir", "tipos": ["Inseto"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 128, "nome": "Tauros", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 129, "nome": "Magikarp", "tipos": ["Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 130, "nome": "Gyarados", "tipos": ["Água", "Voador"], "pre_evolucao": 129, "pre_requisito": "Level 20"},
    {"_id": 131, "nome": "Lapras", "tipos": ["Água", "Gelo"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 132, "nome": "Ditto", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 133, "nome": "Eevee", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 134, "nome": "Vaporeon", "tipos": ["Água"], "pre_evolucao": 133, "pre_requisito": "Water Stone"},
    {"_id": 135, "nome": "Jolteon", "tipos": ["Elétrico"], "pre_evolucao": 133, "pre_requisito": "Thunder Stone"},
    {"_id": 136, "nome": "Flareon", "tipos": ["Fogo"], "pre_evolucao": 133, "pre_requisito": "Fire Stone"},
    {"_id": 137, "nome": "Porygon", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 138, "nome": "Omanyte", "tipos": ["Rocha", "Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 139, "nome": "Omastar", "tipos": ["Rocha", "Água"], "pre_evolucao": 138, "pre_requisito": "Level 40"},
    {"_id": 140, "nome": "Kabuto", "tipos": ["Rocha", "Água"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 141, "nome": "Kabutops", "tipos": ["Rocha", "Água"], "pre_evolucao": 140, "pre_requisito": "Level 40"},
    {"_id": 142, "nome": "Aerodactyl", "tipos": ["Rocha", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 143, "nome": "Snorlax", "tipos": ["Normal"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 144, "nome": "Articuno", "tipos": ["Gelo", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 145, "nome": "Zapdos", "tipos": ["Elétrico", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 146, "nome": "Moltres", "tipos": ["Fogo", "Voador"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 147, "nome": "Dratini", "tipos": ["Dragão"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 148, "nome": "Dragonair", "tipos": ["Dragão"], "pre_evolucao": 147, "pre_requisito": "Level 30"},
    {"_id": 149, "nome": "Dragonite", "tipos": ["Dragão", "Voador"], "pre_evolucao": 148, "pre_requisito": "Level 55"},
    {"_id": 150, "nome": "Mewtwo", "tipos": ["Psíquico"], "pre_evolucao": None, "pre_requisito": None},
    {"_id": 151, "nome": "Mew", "tipos": ["Psíquico"], "pre_evolucao": None, "pre_requisito": None}
]



# pokemons.insert_many(lista_pokemons)
# especies.insert_many(lista_especies)

# treinador_id = int(input("Digite o ID do treinador:"))
# filter_treinador = {"treinador.id_treinador": treinador_id}

# pokemon = pokemons.find(filter_treinador)
# if pokemon:
#     for pokemon_ref in pokemon:
#         especie = especies.find_one({"_id": pokemon_ref["_id"]["num_especie"]})
#         if especie:
#             print(f"Pokemon: {especie['nome']}, N°_pokedex: {pokemon_ref['_id']['num_especie']}, Id_natureza: {pokemon_ref['_id']['id_natureza']}, Tipos: {', '.join(especie['tipos'])}, ")



def povoar_banco():
    print("\n--- POVOANDO O BANCO DE DADOS ---")
    try:
        # Apagando dados antigos
        cliente.drop_database('banco_de_dados')
        # Inserindo novos dados
        pokemons.insert_many(lista_pokemons)
        especies.insert_many(lista_especies)
        print("Banco de dados povoado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao povoar o banco: {e}")
    

def consultar_pokemons():
    while True:
        print("\n--- CONSULTA DE POKÉMON POR TREINADOR ---")
        id_input = input("Digite o ID do treinador (ou 'sair' para voltar ao menu): ")
        
        if id_input.lower() == 'sair':
            break # Sai do loop de consulta
        
        try:
            id_treinador = int(id_input)
            
            # LÓGICA DE CONSULTA (mantida como no seu original)
            filter_treinador = {"treinador.id_treinador": id_treinador}
            cursor_pokemon = pokemons.find(filter_treinador)

            if cursor_pokemon:
                print("-" * 20)
                for pokemon_ref in cursor_pokemon:
                    especie = especies.find_one({"_id": pokemon_ref["_id"]["num_especie"]})
                    if especie:
                        print(f"Pokemon: {especie['nome']}, N°_pokedex: {pokemon_ref['_id']['num_especie']}, Id_natureza: {pokemon_ref['_id']['id_natureza']}, Tipos: {', '.join(especie['tipos'])}, ")
                print("-" * 20)
            else:
                print(f"Nenhum Pokémon encontrado para o treinador com ID {id_treinador}.")
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número de ID ou 'sair'.")
        except Exception as e:
            print(f"Ocorreu um erro durante a consulta: {e}")


def main():
    while True:
        print("\n===== MENU PRINCIPAL DO POKÉDEX =====")
        print("1. Povoar o Banco de Dados")
        print("2. Consultar Pokémon por ID do Treinador")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            povoar_banco()
        elif escolha == '2':
            consultar_pokemons()
        elif escolha == '3':
            print("Saindo do programa. Até mais!")
            break # Sai do loop principal
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()