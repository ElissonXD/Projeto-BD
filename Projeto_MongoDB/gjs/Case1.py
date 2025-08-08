import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

treinadores = banco['treinador']

pokemons = banco['pokemon']

especies = banco['especie']



lista_treinadores =[
    {"_id": 1, "nome": "Ash Ketchum"},
    {"_id": 2, "nome": "Misty"},
    {"_id": 3, "nome": "Brock"},
    {"_id": 4, "nome": "Gary Oak"},
    {"_id": 5, "nome": "Red"},
    {"_id": 6, "nome": "Blue"},
]



lista_pokemons = [
    # Pokémon de Ash
    {"_id": {"num_especie": 25, "id_natureza": 1}, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 1},
    {"_id": {"num_especie": 6, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 1},
    {"_id": {"num_especie": 9, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 1},
    
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

    # Pokémon de Red
    {"_id": {"num_especie": 3, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": 5},
    {"_id": {"num_especie": 25, "id_natureza": 2}, "rota": "Viridian Forest", "regiao": "Kanto", "treinador": 5},
    {"_id": {"num_especie": 143, "id_natureza": 1}, "rota": "Rota 12", "regiao": "Kanto", "treinador": 5},
    
    # Pokémon de Blue
    {"_id": {"num_especie": 6, "id_natureza": 2}, "rota": None, "regiao": "Kanto", "treinador": 6},
    {"_id": {"num_especie": 112, "id_natureza": 1}, "rota": "Cerulean Cave", "regiao": "Kanto", "treinador": 6},
    {"_id": {"num_especie": 103, "id_natureza": 1}, "rota": None, "regiao": "Kanto", "treinador": 6},
    
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

filter_treinador = {"treinador": id_treinador}
cursor_pokemon = pokemons.find(filter_treinador)
cursor_pokemon = list(cursor_pokemon)

if bool(cursor_pokemon):
    print("-" * 20)
    for pokemon_ref in cursor_pokemon:
        especie = especies.find_one({"_id": pokemon_ref["_id"]["num_especie"]})
        if especie:
            print(f"Pokemon: {especie['nome']}, N°_pokedex: {pokemon_ref['_id']['num_especie']}, Id_natureza: {pokemon_ref['_id']['id_natureza']}, Tipos: {', '.join(especie['tipos'])}, ")
    print("-" * 20)
else:
    print(f"Nenhum Pokémon encontrado para o treinador com ID {id_treinador}.")


""" def povoar_banco():
    print("\n--- POVOANDO O BANCO DE DADOS ---")
    try:
        # Apagando dados antigos
        cliente.drop_database('banco_de_dados')
        # Inserindo novos dados
        treinadores.insert_many(lista_treinadores)
        pokemons.insert_many(lista_pokemons)
        especies.insert_many(lista_especies)
        print("Banco de dados povoado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao povoar o banco: {e}")
    
 """
""" def consultar_pokemons():
    while True:
        print("\n--- CONSULTA DE POKÉMON POR TREINADOR ---")
        id_input = input("Digite o ID do treinador (ou 'sair' para voltar ao menu): ")
        
        if id_input.lower() == 'sair':
            break # Sai do loop de consulta
        
        try:
            id_treinador = int(id_input)
            
            filter_treinador = {"treinador": id_treinador}
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
    main() """