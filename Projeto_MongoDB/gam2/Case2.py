#um documento embutindo apenas um documento
 
# |pokemon|-<é>-|especie|

import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

pokemons = banco['pokemon']

lista_pokemons = [
    {
        "_id": {
            "especie": {
                "id_especie": 25,
                "nome": "Pikachu",
                "tipos": ["Elétrico"],
                "pre_evolucao": None,
                "pre_requisito": None
            },
            "id_natureza": 1
        },
        "rota": "Viridian Forest",
        "regiao": "Kanto",
        "treinador": 1
    },
    {
        "_id": {
            "especie": {
                "id_especie": 6,
                "nome": "Charizard",
                "tipos": ["Fogo", "Voador"],
                "pre_evolucao": 5,
                "pre_requisito": "Level 36"
            },
            "id_natureza": 1
        },
        "rota": None,
        "regiao": "Kanto",
        "treinador": 1
    },
    {
        "_id": {
            "especie": {
                "id_especie": 9,
                "nome": "Blastoise",
                "tipos": ["Água"],
                "pre_evolucao": 8,
                "pre_requisito": "Level 36"
            },
            "id_natureza": 1
        },
        "rota": None,
        "regiao": "Kanto",
        "treinador": 1
    },
    {
        "_id": {
            "especie": {
                "id_especie": 3,
                "nome": "Venusaur",
                "tipos": ["Planta", "Veneno"],
                "pre_evolucao": 2,
                "pre_requisito": "Level 32"
            },
            "id_natureza": 1
        },
        "rota": None,
        "regiao": "Kanto",
        "treinador": 1
    },
    {
        "_id": {
            "especie": {
                "id_especie": 18,
                "nome": "Pidgeot",
                "tipos": ["Normal", "Voador"],
                "pre_evolucao": 17,
                "pre_requisito": "Level 36"
            },
            "id_natureza": 1
        },
        "rota": None,
        "regiao": "Kanto",
        "treinador": 1
    },
    {
        "_id": {
            "especie": {
                "id_especie": 131,
                "nome": "Lapras",
                "tipos": ["Água", "Gelo"],
                "pre_evolucao": None,
                "pre_requisito": None
            },
            "id_natureza": 1
        },
        "rota": "Silph Co.",
        "regiao": "Kanto",
        "treinador": 1
    },
    {
        "_id": {
            "especie": {
                "id_especie": 121,
                "nome": "Starmie",
                "tipos": ["Água", "Psíquico"],
                "pre_evolucao": 120,
                "pre_requisito": "Water Stone"
            },
            "id_natureza": 1
        },
        "rota": None,
        "regiao": "Kanto",
        "treinador": 2
    },
    {
        "_id": {
            "especie": {
                "id_especie": 54,
                "nome": "Psyduck",
                "tipos": ["Água"],
                "pre_evolucao": None,
                "pre_requisito": None
            },
            "id_natureza": 1
        },
        "rota": "Rota 24",
        "regiao": "Kanto",
        "treinador": 2
    },
    {
        "_id": {
            "especie": {
                "id_especie": 118,
                "nome": "Goldeen",
                "tipos": ["Água"],
                "pre_evolucao": None,
                "pre_requisito": None
            },
            "id_natureza": 1
        },
        "rota": "Rota 6",
        "regiao": "Kanto",
        "treinador": 2
    },
    {
        "_id": {
            "especie": {
                "id_especie": 95,
                "nome": "Onix",
                "tipos": ["Rocha", "Terra"],
                "pre_evolucao": None,
                "pre_requisito": None
            },
            "id_natureza": 1
        },
        "rota": "Rock Tunnel",
        "regiao": "Kanto",
        "treinador": 3
    },
    {
        "_id": {
            "especie": {
                "id_especie": 74,
                "nome": "Geodude",
                "tipos": ["Rocha", "Terra"],
                "pre_evolucao": None,
                "pre_requisito": None
            },
            "id_natureza": 1
        },
        "rota": "Mt. Moon",
        "regiao": "Kanto",
        "treinador": 3
    },
    {
        "_id": {
            "especie": {
                "id_especie": 37,
                "nome": "Vulpix",
                "tipos": ["Fogo"],
                "pre_evolucao": None,
                "pre_requisito": None
            },
            "id_natureza": 1
        },
        "rota": "Rota 7",
        "regiao": "Kanto",
        "treinador": 3
    },
    {
        "_id": {
            "especie": {
                "id_especie": 9,
                "nome": "Blastoise",
                "tipos": ["Água"],
                "pre_evolucao": 8,
                "pre_requisito": "Level 36"
            },
            "id_natureza": 2
        },
        "rota": None,
        "regiao": "Kanto",
        "treinador": 4
    },
    {
        "_id": {
            "especie": {
                "id_especie": 59,
                "nome": "Arcanine",
                "tipos": ["Fogo"],
                "pre_evolucao": 58,
                "pre_requisito": "Fire Stone"
            },
            "id_natureza": 1
        },
        "rota": None,
        "regiao": "Kanto",
        "treinador": 4
    },
    {
        "_id": {
            "especie": {
                "id_especie": 65,
                "nome": "Alakazam",
                "tipos": ["Psíquico"],
                "pre_evolucao": 64,
                "pre_requisito": "Trade"
            },
            "id_natureza": 1
        },
        "rota": None,
        "regiao": "Kanto",
        "treinador": 4
    }
]


def povoar_banco():
    print("\n--- POVOANDO O BANCO DE DADOS ---")
    try:
        # Apagando dados antigos
        cliente.drop_database('banco_de_dados')
        # Inserindo novos dados
        pokemons.insert_many(lista_pokemons)
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

            lista_pokemons_encontrados = list(pokemons.find({"_id.especie.id_especie": num_especie}))
            
            if not lista_pokemons_encontrados:
                print(f"Nenhum pokémon da espécie com ID {num_especie} foi encontrado")
                continue
            
            nome_especie = lista_pokemons_encontrados[0]["_id"]["especie"]["nome"]
            
            print(f"\nEspécie encontrada: {nome_especie} (ID: {num_especie})")
            
            print(f"\nForam encontrados {len(lista_pokemons_encontrados)} pokémon(s) desta espécie:\n")
            
            for i, pokemon in enumerate(lista_pokemons_encontrados):
                especie_info = pokemon["_id"]["especie"]
                
                print(f"{i+1}. Espécie: {especie_info['nome']} (ID: {especie_info['id_especie']})")
                print(f"   ID Natureza: {pokemon['_id']['id_natureza']}")
                print(f"   Rota: {pokemon['rota'] if pokemon['rota'] else 'Não especificada'}")
                print(f"   Região: {pokemon['regiao']}")
                print(f"   Treinador ID: {pokemon['treinador']}\n")
                    
        
        except Exception as e:
            print(f"Ocorreu um erro na consulta: {e}")
            


if __name__ == "__main__":
    povoar_banco()
    consulta_pokemon_especie()
