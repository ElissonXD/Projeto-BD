#um documento embutindo vários documentos

# |pokemon|-<é>-|especie|

import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

especies = banco['especie']

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
        "pokemons": []
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
        "pokemons": []
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "id_pokemon": 2,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 5
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
        "pokemons": []
    },
    {
        "_id": 5,
        "nome": "Charmeleon",
        "tipos": [
            "Fogo"
        ],
        "pre_evolucao": 4,
        "pre_requisito": "Level 16",
        "pokemons": []
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "id_pokemon": 2,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 6
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
        "pokemons": []
    },
    {
        "_id": 8,
        "nome": "Wartortle",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": 7,
        "pre_requisito": "Level 16",
        "pokemons": []
    },
    {
        "_id": 9,
        "nome": "Blastoise",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": 8,
        "pre_requisito": "Level 36",
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "id_pokemon": 2,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 4
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "id_pokemon": 2,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 4
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": "Viridian Forest",
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "id_pokemon": 2,
                "rota": "Viridian Forest",
                "regiao": "Kanto",
                "treinador": 5
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 8
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 10
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": "Rota 7",
                "regiao": "Kanto",
                "treinador": 3
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 7
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": "Cerulean Cave",
                "regiao": "Kanto",
                "treinador": 9
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 10
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": "Rota 24",
                "regiao": "Kanto",
                "treinador": 2
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 4
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 4
            },
            {
                "id_pokemon": 2,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 9
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 7
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
        "pokemons": [
            {
                "id_pokemon": 1,
                "rota": "Mt. Moon",
                "regiao": "Kanto",
                "treinador": 3
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
        especies.insert_many(lista_especies)
        print("Banco de dados povoado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao povoar o banco: {e}")


def consulta_pokemon_especie():
    # indice (id_natureza) e id de treinadores dos pokemons da especie cuja o id é..
    while True:
        print("\n--- CONSULTA POKEMONS POR ESPÉCIE ---")
        num_especie = input("Digite o id da espécie (ou 'sair' para encerrar): ").strip()
        
        if num_especie.lower() == 'sair':
            break
        
        try:
            num_especie = int(num_especie)

            especie_encontrada = especies.find_one({"_id": num_especie})
            
            if not especie_encontrada:
                print(f"Espécie com id {num_especie} não encontrada")
                continue
            
            print(f"\nEspécie encontrada: {especie_encontrada['nome']} (ID: {num_especie})")
            
            lista_pokemons_encontrados = list(especie_encontrada.get("pokemons", []))
            
            if not lista_pokemons_encontrados:
                print(f"Nenhum pokémon da espécie '{especie_encontrada['nome']}' foi encontrado")
                continue
            
            print(f"\nForam encontrados {len(lista_pokemons_encontrados)} pokémon(s):\n")

            for i, pokemon in enumerate(lista_pokemons_encontrados):
                print(f"{i+1}. ID Natureza: {pokemon['_id']}")
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
