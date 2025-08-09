#um documento com um array de referências para documentos
 
# |pokemon|-<é>-|especie|

import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

pokemons = banco['pokemon']
especies = banco['especie']

lista_pokemons = [
    # Pokémon de Ash
    {"_id": {"num_especie": 25, "id_natureza": 1}, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 1},
    {"_id": {"num_especie": 6, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 1},
    {"_id": {"num_especie": 9, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 1},
    {"_id": {"num_especie": 3, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 1},
    {"_id": {"num_especie": 18, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 1},
    {"_id": {"num_especie": 131, "id_natureza": 1}, "rota": "Silph Co.", "regiao": "Kanto", "treinador": 1},
    
    # Pokémon de Misty
    {"_id": {"num_especie": 121, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 2},
    {"_id": {"num_especie": 54, "id_natureza": 1}, "rota": "Rota 24", "regiao": "Kanto", "treinador": 2},
    {"_id": {"num_especie": 118, "id_natureza": 1}, "rota": "Rota 6", "regiao": "Kanto", "treinador": 2},
    
    # Pokémon de Brock
    {"_id": {"num_especie": 95, "id_natureza": 1}, "rota": "Rock Tunnel", "regiao": "Kanto", "treinador": 3},
    {"_id": {"num_especie": 74, "id_natureza": 1}, "rota": "Mt. Moon", "regiao": "Kanto", "treinador": 3},
    {"_id": {"num_especie": 37, "id_natureza": 1}, "rota": "Rota 7", "regiao": "Kanto", "treinador": 3},
    
    # Pokémon de Gary Oak
    {"_id": {"num_especie": 9, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": 4},
    {"_id": {"num_especie": 59, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 4},
    {"_id": {"num_especie": 65, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 4},
    {"_id": {"num_especie": 18, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": 4},

    # Pokémon de Red
    {"_id": {"num_especie": 3, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": 5},
    {"_id": {"num_especie": 25, "id_natureza": 2}, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 5},
    {"_id": {"num_especie": 143, "id_natureza": 1}, "rota": "Rota 12", "regiao": "Kanto", "treinador": 5},
    
    # Pokémon de Blue
    {"_id": {"num_especie": 6, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": 6},
    {"_id": {"num_especie": 112, "id_natureza": 1}, "rota": "Cerulean Cave", "regiao": "Kanto", "treinador": 6},
    {"_id": {"num_especie": 103, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 6},
    
    # Pokémon de Erika
    {"_id": {"num_especie": 45, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 7},
    {"_id": {"num_especie": 114, "id_natureza": 1}, "rota": "Rota 21", "regiao": "Kanto", "treinador": 7},
    {"_id": {"num_especie": 71, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 7},

    # Pokémon de Lt. Surge
    {"_id": {"num_especie": 26, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 8},
    {"_id": {"num_especie": 101, "id_natureza": 1}, "rota": "Power Plant", "regiao": "Kanto", "treinador": 8},
    {"_id": {"num_especie": 82, "id_natureza": 1}, "rota": "Power Plant", "regiao": "Kanto", "treinador": 8},

    # Pokémon de Sabrina
    {"_id": {"num_especie": 65, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": 9},
    {"_id": {"num_especie": 49, "id_natureza": 1}, "rota": "Cerulean Cave", "regiao": "Kanto", "treinador": 9},
    {"_id": {"num_especie": 122, "id_natureza": 1}, "rota": "Rota 2", "regiao": "Kanto", "treinador": 9},

    # Pokémon de Giovanni
    {"_id": {"num_especie": 53, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 10},
    {"_id": {"num_especie": 34, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 10},
    {"_id": {"num_especie": 112, "id_natureza": 2}, "rota": "Cerulean Cave", "regiao": "Kanto", "treinador": 10}
]

lista_especies = [
    {
        "_id": 1,
        "nome": "Bulbasaur",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": []
    },
    {
        "_id": 2,
        "nome": "Ivysaur",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": 1,
        "pre_requisito": "Level 16",
        "pokemons_refs": []
    },
    {
        "_id": 3,
        "nome": "Venusaur",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": 2,
        "pre_requisito": "Level 32",
        "pokemons_refs": [
            {
                "num_especie": 3,
                "id_natureza": 1
            },
            {
                "num_especie": 3,
                "id_natureza": 2
            }
        ]
    },
    {
        "_id": 4,
        "nome": "Charmander",
        "tipos": [
            "Fogo"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": []
    },
    {
        "_id": 5,
        "nome": "Charmeleon",
        "tipos": [
            "Fogo"
        ],
        "pre_evolucao": 4,
        "pre_requisito": "Level 16",
        "pokemons_refs": []
    },
    {
        "_id": 6,
        "nome": "Charizard",
        "tipos": [
            "Fogo",
            "Voador"
        ],
        "pre_evolucao": 5,
        "pre_requisito": "Level 36",
        "pokemons_refs": [
            {
                "num_especie": 6,
                "id_natureza": 1
            },
            {
                "num_especie": 6,
                "id_natureza": 2
            }
        ]
    },
    {
        "_id": 7,
        "nome": "Squirtle",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": []
    },
    {
        "_id": 8,
        "nome": "Wartortle",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": 7,
        "pre_requisito": "Level 16",
        "pokemons_refs": []
    },
    {
        "_id": 9,
        "nome": "Blastoise",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": 8,
        "pre_requisito": "Level 36",
        "pokemons_refs": [
            {
                "num_especie": 9,
                "id_natureza": 1
            },
            {
                "num_especie": 9,
                "id_natureza": 2
            }
        ]
    },
    {
        "_id": 18,
        "nome": "Pidgeot",
        "tipos": [
            "Normal",
            "Voador"
        ],
        "pre_evolucao": 17,
        "pre_requisito": "Level 36",
        "pokemons_refs": [
            {
                "num_especie": 18,
                "id_natureza": 1
            },
            {
                "num_especie": 18,
                "id_natureza": 2
            }
        ]
    },
    {
        "_id": 25,
        "nome": "Pikachu",
        "tipos": [
            "Elétrico"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 25,
                "id_natureza": 1
            },
            {
                "num_especie": 25,
                "id_natureza": 2
            }
        ]
    },
    {
        "_id": 26,
        "nome": "Raichu",
        "tipos": [
            "Elétrico"
        ],
        "pre_evolucao": 25,
        "pre_requisito": "Thunder Stone",
        "pokemons_refs": [
            {
                "num_especie": 26,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 34,
        "nome": "Nidoking",
        "tipos": [
            "Veneno",
            "Terra"
        ],
        "pre_evolucao": 33,
        "pre_requisito": "Moon Stone",
        "pokemons_refs": [
            {
                "num_especie": 34,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 37,
        "nome": "Vulpix",
        "tipos": [
            "Fogo"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 37,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 45,
        "nome": "Vileplume",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": 44,
        "pre_requisito": "Leaf Stone",
        "pokemons_refs": [
            {
                "num_especie": 45,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 49,
        "nome": "Venomoth",
        "tipos": [
            "Inseto",
            "Veneno"
        ],
        "pre_evolucao": 48,
        "pre_requisito": "Level 31",
        "pokemons_refs": [
            {
                "num_especie": 49,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 53,
        "nome": "Persian",
        "tipos": [
            "Normal"
        ],
        "pre_evolucao": 52,
        "pre_requisito": "Level 28",
        "pokemons_refs": [
            {
                "num_especie": 53,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 54,
        "nome": "Psyduck",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 54,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 59,
        "nome": "Arcanine",
        "tipos": [
            "Fogo"
        ],
        "pre_evolucao": 58,
        "pre_requisito": "Fire Stone",
        "pokemons_refs": [
            {
                "num_especie": 59,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 65,
        "nome": "Alakazam",
        "tipos": [
            "Psíquico"
        ],
        "pre_evolucao": 64,
        "pre_requisito": "Trade",
        "pokemons_refs": [
            {
                "num_especie": 65,
                "id_natureza": 1
            },
            {
                "num_especie": 65,
                "id_natureza": 2
            }
        ]
    },
    {
        "_id": 71,
        "nome": "Victreebel",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": 70,
        "pre_requisito": "Leaf Stone",
        "pokemons_refs": [
            {
                "num_especie": 71,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 74,
        "nome": "Geodude",
        "tipos": [
            "Rocha",
            "Terra"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 74,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 82,
        "nome": "Magneton",
        "tipos": [
            "Elétrico",
            "Aço"
        ],
        "pre_evolucao": 81,
        "pre_requisito": "Level 30",
        "pokemons_refs": [
            {
                "num_especie": 82,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 95,
        "nome": "Onix",
        "tipos": [
            "Rocha",
            "Terra"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 95,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 101,
        "nome": "Electrode",
        "tipos": [
            "Elétrico"
        ],
        "pre_evolucao": 100,
        "pre_requisito": "Level 30",
        "pokemons_refs": [
            {
                "num_especie": 101,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 103,
        "nome": "Exeggutor",
        "tipos": [
            "Planta",
            "Psíquico"
        ],
        "pre_evolucao": 102,
        "pre_requisito": "Leaf Stone",
        "pokemons_refs": [
            {
                "num_especie": 103,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 112,
        "nome": "Rhydon",
        "tipos": [
            "Rocha",
            "Terra"
        ],
        "pre_evolucao": 111,
        "pre_requisito": "Level 42",
        "pokemons_refs": [
            {
                "num_especie": 112,
                "id_natureza": 1
            },
            {
                "num_especie": 112,
                "id_natureza": 2
            }
        ]
    },
    {
        "_id": 114,
        "nome": "Tangela",
        "tipos": [
            "Planta"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 114,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 118,
        "nome": "Goldeen",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 118,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 121,
        "nome": "Starmie",
        "tipos": [
            "Água",
            "Psíquico"
        ],
        "pre_evolucao": 120,
        "pre_requisito": "Water Stone",
        "pokemons_refs": [
            {
                "num_especie": 121,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 122,
        "nome": "Mr. Mime",
        "tipos": [
            "Psíquico",
            "Fada"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 122,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 131,
        "nome": "Lapras",
        "tipos": [
            "Água",
            "Gelo"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 131,
                "id_natureza": 1
            }
        ]
    },
    {
        "_id": 143,
        "nome": "Snorlax",
        "tipos": [
            "Normal"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons_refs": [
            {
                "num_especie": 143,
                "id_natureza": 1
            }
        ]
    }
]

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


def consulta_pokemon_especie():
    while True:
        print("\n--- CONSULTA POKEMONS POR ESPÉCIE ---")
        num_especie_input = input("Digite o id da espécie (ou 'sair' para encerrar): ").strip()

        if num_especie_input.lower() == 'sair':
            break

        try:
            num_especie = int(num_especie_input)

            especie_encontrada = especies.find_one({"_id": num_especie})

            if not especie_encontrada:
                print(f"Espécie com id {num_especie} não encontrada.")
                continue

            print(f"\nEspécie encontrada: {especie_encontrada['nome']} (ID: {num_especie})")

            # pega o array de referencias do documento da espécie
            referencias_pokemons = especie_encontrada.get("pokemons_refs", [])

            if not referencias_pokemons:
                print(f"Nenhum pokémon da espécie '{especie_encontrada['nome']}' foi encontrado.")
                continue

            lista_pokemons_encontrados = list(pokemons.find({"_id": {"$in": referencias_pokemons}}))

            print(f"\nForam encontrados {len(lista_pokemons_encontrados)} pokémon(s):\n")

            for i, pokemon in enumerate(lista_pokemons_encontrados):
                print(f"{i+1}. ID Natureza: {pokemon['_id']['id_natureza']}")
                print(f"   Rota: {pokemon.get('rota', 'N/A')}")
                print(f"   Região: {pokemon.get('regiao', 'N/A')}")
                print(f"   Treinador ID: {pokemon.get('treinador', 'N/A')}\n")

        except ValueError:
            print("Por favor, digite um número de ID válido.")
        except Exception as e:
            print(f"Ocorreu um erro na consulta: {e}")


if __name__ == "__main__":
    povoar_banco()
    consulta_pokemon_especie()
