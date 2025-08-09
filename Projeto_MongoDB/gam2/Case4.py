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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "_id": 2,
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "_id": 2,
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "_id": 2,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 4
            }
        ]
    },
    {
        "_id": 10,
        "nome": "Caterpie",
        "tipos": [
            "Inseto"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 11,
        "nome": "Metapod",
        "tipos": [
            "Inseto"
        ],
        "pre_evolucao": 10,
        "pre_requisito": "Level 7",
        "pokemons": []
    },
    {
        "_id": 12,
        "nome": "Butterfree",
        "tipos": [
            "Inseto",
            "Voador"
        ],
        "pre_evolucao": 11,
        "pre_requisito": "Level 10",
        "pokemons": []
    },
    {
        "_id": 13,
        "nome": "Weedle",
        "tipos": [
            "Inseto",
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 14,
        "nome": "Kakuna",
        "tipos": [
            "Inseto",
            "Veneno"
        ],
        "pre_evolucao": 13,
        "pre_requisito": "Level 7",
        "pokemons": []
    },
    {
        "_id": 15,
        "nome": "Beedrill",
        "tipos": [
            "Inseto",
            "Veneno"
        ],
        "pre_evolucao": 14,
        "pre_requisito": "Level 10",
        "pokemons": []
    },
    {
        "_id": 16,
        "nome": "Pidgey",
        "tipos": [
            "Normal",
            "Voador"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 17,
        "nome": "Pidgeotto",
        "tipos": [
            "Normal",
            "Voador"
        ],
        "pre_evolucao": 16,
        "pre_requisito": "Level 18",
        "pokemons": []
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "_id": 2,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 4
            }
        ]
    },
    {
        "_id": 19,
        "nome": "Rattata",
        "tipos": [
            "Normal"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 20,
        "nome": "Raticate",
        "tipos": [
            "Normal"
        ],
        "pre_evolucao": 19,
        "pre_requisito": "Level 20",
        "pokemons": []
    },
    {
        "_id": 21,
        "nome": "Spearow",
        "tipos": [
            "Normal",
            "Voador"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 22,
        "nome": "Fearow",
        "tipos": [
            "Normal",
            "Voador"
        ],
        "pre_evolucao": 21,
        "pre_requisito": "Level 20",
        "pokemons": []
    },
    {
        "_id": 23,
        "nome": "Ekans",
        "tipos": [
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 24,
        "nome": "Arbok",
        "tipos": [
            "Veneno"
        ],
        "pre_evolucao": 23,
        "pre_requisito": "Level 22",
        "pokemons": []
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
                "_id": 1,
                "rota": "Viridian Forest",
                "regiao": "Kanto",
                "treinador": 1
            },
            {
                "_id": 2,
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 8
            }
        ]
    },
    {
        "_id": 27,
        "nome": "Sandshrew",
        "tipos": [
            "Terra"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 28,
        "nome": "Sandslash",
        "tipos": [
            "Terra"
        ],
        "pre_evolucao": 27,
        "pre_requisito": "Level 22",
        "pokemons": []
    },
    {
        "_id": 29,
        "nome": "Nidoran♀",
        "tipos": [
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 30,
        "nome": "Nidorina",
        "tipos": [
            "Veneno"
        ],
        "pre_evolucao": 29,
        "pre_requisito": "Level 16",
        "pokemons": []
    },
    {
        "_id": 31,
        "nome": "Nidoqueen",
        "tipos": [
            "Veneno",
            "Terra"
        ],
        "pre_evolucao": 30,
        "pre_requisito": "Moon Stone",
        "pokemons": []
    },
    {
        "_id": 32,
        "nome": "Nidoran♂",
        "tipos": [
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 33,
        "nome": "Nidorino",
        "tipos": [
            "Veneno"
        ],
        "pre_evolucao": 32,
        "pre_requisito": "Level 16",
        "pokemons": []
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 10
            }
        ]
    },
    {
        "_id": 35,
        "nome": "Clefairy",
        "tipos": [
            "Fada"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 36,
        "nome": "Clefable",
        "tipos": [
            "Fada"
        ],
        "pre_evolucao": 35,
        "pre_requisito": "Moon Stone",
        "pokemons": []
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
                "_id": 1,
                "rota": "Rota 7",
                "regiao": "Kanto",
                "treinador": 3
            }
        ]
    },
    {
        "_id": 38,
        "nome": "Ninetales",
        "tipos": [
            "Fogo"
        ],
        "pre_evolucao": 37,
        "pre_requisito": "Fire Stone",
        "pokemons": []
    },
    {
        "_id": 39,
        "nome": "Jigglypuff",
        "tipos": [
            "Normal",
            "Fada"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 40,
        "nome": "Wigglytuff",
        "tipos": [
            "Normal",
            "Fada"
        ],
        "pre_evolucao": 39,
        "pre_requisito": "Moon Stone",
        "pokemons": []
    },
    {
        "_id": 41,
        "nome": "Zubat",
        "tipos": [
            "Veneno",
            "Voador"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 42,
        "nome": "Golbat",
        "tipos": [
            "Veneno",
            "Voador"
        ],
        "pre_evolucao": 41,
        "pre_requisito": "Level 22",
        "pokemons": []
    },
    {
        "_id": 43,
        "nome": "Oddish",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 44,
        "nome": "Gloom",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": 43,
        "pre_requisito": "Level 21",
        "pokemons": []
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 7
            }
        ]
    },
    {
        "_id": 46,
        "nome": "Paras",
        "tipos": [
            "Inseto",
            "Planta"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 47,
        "nome": "Parasect",
        "tipos": [
            "Inseto",
            "Planta"
        ],
        "pre_evolucao": 46,
        "pre_requisito": "Level 24",
        "pokemons": []
    },
    {
        "_id": 48,
        "nome": "Venonat",
        "tipos": [
            "Inseto",
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
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
                "_id": 1,
                "rota": "Cerulean Cave",
                "regiao": "Kanto",
                "treinador": 9
            }
        ]
    },
    {
        "_id": 50,
        "nome": "Diglett",
        "tipos": [
            "Terra"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 51,
        "nome": "Dugtrio",
        "tipos": [
            "Terra"
        ],
        "pre_evolucao": 50,
        "pre_requisito": "Level 26",
        "pokemons": []
    },
    {
        "_id": 52,
        "nome": "Meowth",
        "tipos": [
            "Normal"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
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
                "_id": 1,
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
                "_id": 1,
                "rota": "Rota 24",
                "regiao": "Kanto",
                "treinador": 2
            }
        ]
    },
    {
        "_id": 55,
        "nome": "Golduck",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": 54,
        "pre_requisito": "Level 33",
        "pokemons": []
    },
    {
        "_id": 56,
        "nome": "Mankey",
        "tipos": [
            "Lutador"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 57,
        "nome": "Primeape",
        "tipos": [
            "Lutador"
        ],
        "pre_evolucao": 56,
        "pre_requisito": "Level 28",
        "pokemons": []
    },
    {
        "_id": 58,
        "nome": "Growlithe",
        "tipos": [
            "Fogo"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 4
            }
        ]
    },
    {
        "_id": 60,
        "nome": "Poliwag",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 61,
        "nome": "Poliwhirl",
        "tipos": [
            "Água"
        ],
        "pre_evolucao": 60,
        "pre_requisito": "Level 25",
        "pokemons": []
    },
    {
        "_id": 62,
        "nome": "Poliwrath",
        "tipos": [
            "Água",
            "Lutador"
        ],
        "pre_evolucao": 61,
        "pre_requisito": "Water Stone",
        "pokemons": []
    },
    {
        "_id": 63,
        "nome": "Abra",
        "tipos": [
            "Psíquico"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 64,
        "nome": "Kadabra",
        "tipos": [
            "Psíquico"
        ],
        "pre_evolucao": 63,
        "pre_requisito": "Level 16",
        "pokemons": []
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 4
            },
            {
                "_id": 2,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 9
            }
        ]
    },
    {
        "_id": 66,
        "nome": "Machop",
        "tipos": [
            "Lutador"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 67,
        "nome": "Machoke",
        "tipos": [
            "Lutador"
        ],
        "pre_evolucao": 66,
        "pre_requisito": "Level 28",
        "pokemons": []
    },
    {
        "_id": 68,
        "nome": "Machamp",
        "tipos": [
            "Lutador"
        ],
        "pre_evolucao": 67,
        "pre_requisito": "Trade",
        "pokemons": []
    },
    {
        "_id": 69,
        "nome": "Bellsprout",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 70,
        "nome": "Weepinbell",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "pre_evolucao": 69,
        "pre_requisito": "Level 21",
        "pokemons": []
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
                "_id": 1,
                "rota": None,
                "regiao": "Kanto",
                "treinador": 7
            }
        ]
    },
    {
        "_id": 72,
        "nome": "Tentacool",
        "tipos": [
            "Água",
            "Veneno"
        ],
        "pre_evolucao": None,
        "pre_requisito": None,
        "pokemons": []
    },
    {
        "_id": 73,
        "nome": "Tentacruel",
        "tipos": [
            "Água",
            "Veneno"
        ],
        "pre_evolucao": 72,
        "pre_requisito": "Level 30",
        "pokemons": []
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
                "_id": 1,
                "rota": "Mt. Moon",
                "regiao": "Kanto",
                "treinador": 3
            }
        ]
    },
    {
        "_id": 75,
        "nome": "Graveler",
        "tipos": [
            "Rocha",
            "Terra"
        ],
        "pre_evolucao": 74,
        "pre_requisito": "Level 25",
        "pokemons": []
    },
    {
        "_id": 76,
        "nome": "Golem",
        "tipos": [
            "Rocha",
            "Terra"
        ],
        "pre_evolucao": 75,
        "pre_requisito": "Trade",
        "pokemons": []
    },
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
