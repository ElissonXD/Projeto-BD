import sqlite3

def exibir_resultados(nome_tabela, consulta, cursor):
    print(f"\n========== {nome_tabela.upper()} ==========")
    cursor.execute(consulta)
    linhas = cursor.fetchall()

    if linhas:
        for linha in linhas:
            print(linha)
    else:
        print("Nenhum registro encontrado.")
    print("=" * 35)


def main():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    while True:
        resposta = input("\nDeseja consultar tudo? (s/n): ").strip().lower()
        
        if resposta == "sim" or resposta == "s":
            exibir_resultados("Treinador", "SELECT * FROM treinador;", cursor)
            exibir_resultados("Professor", "SELECT * FROM professor;", cursor)
            exibir_resultados("Líder", "SELECT * FROM lider;", cursor)
            exibir_resultados("Ginásio", "SELECT * FROM ginasio;", cursor)
            exibir_resultados("Pokémon", "SELECT * FROM pokemon;", cursor)
            exibir_resultados("Espécie", "SELECT * FROM especie;", cursor)
            exibir_resultados("Movimento", "SELECT * FROM movimento;", cursor)
            exibir_resultados("Tem (pokémon tem movimento)", "SELECT * FROM tem;", cursor)
            exibir_resultados("Ensina (treinador ensina movimento)", "SELECT * FROM ensina;", cursor)
            exibir_resultados("Item", "SELECT * FROM item;", cursor)
            exibir_resultados("Recebe (treinador recebe item)", "SELECT * FROM recebe;", cursor)
            exibir_resultados("Enfrenta (batalhas)", "SELECT * FROM enfrenta;", cursor)
        else:
                print("\n========= CONSULTA PERSONALIZADA =========")
                print("""
num | consulta 
 0  | sair
 1  | Treinador com mais pokemons
 2  | Líder de cada ginásio
 3  | Treinadores que não são professores nem líderes de ginásio
 4  | Treinadores e seus pokemons
 5  | Treinadores que ensinam
 6  | Todos os pokemons que são do tipo água e/ou do tipo fogo
 7  | Quantidade de pokemons existentes
 8  | Pokemons selvagens
 9  | Espécies que podem evoluir\n""")
                
                num = int(input("Numero da consulta: "))
                consulta = ""
                
                match num:
                    case 0:
                        break
                        
                    case 1:  # group by 
                        consulta = """
                        SELECT t.id, t.nome, COUNT(p.id_pokemon) as quantidade_pokemons
                        FROM treinador t
                        LEFT JOIN pokemon p ON t.id = p.id_treinador
                        GROUP BY t.id, t.nome
                        ORDER BY quantidade_pokemons DESC
                        LIMIT 1;
                        """
                        
                    case 2:  # junçao interna
                        consulta = """
                        SELECT g.cidade, g.nome as nome_ginasio, g.tipo, t.nome as nome_lider
                        FROM ginasio g
                        INNER JOIN lider l ON g.id = l.id
                        INNER JOIN treinador t ON l.id = t.id;
                        """
                        
                    case 3:  # junção externa e operação de conjunto
                        consulta = """
                        SELECT t.id, t.nome
                        FROM treinador t
                        WHERE t.id NOT IN (
                            SELECT id FROM professor
                            UNION
                            SELECT id FROM lider
                        );
                        """
                        
                    case 4:  # junção externa
                        consulta = """
                        SELECT t.id, t.nome as nome_treinador, 
                            p.numero, p.id_pokemon, e.nome as nome_especie
                        FROM treinador t
                        LEFT JOIN pokemon p ON t.id = p.id_treinador
                        LEFT JOIN especie e ON p.numero = e.numero
                        ORDER BY t.id;
                        """
                        
                    case 5:  # semi junçao (EXISTS)
                        consulta = """
                        SELECT DISTINCT t.id, t.nome
                        FROM treinador t
                        WHERE EXISTS (
                            SELECT 1
                            FROM ensina en
                            WHERE en.id_treinador = t.id
                        );
                        """
                        
                    case 6:  # operação de conjuntos
                        consulta = """
                        SELECT p.numero, p.id_pokemon, e.nome, e.tipo1, e.tipo2
                        FROM pokemon p
                        INNER JOIN especie e ON p.numero = e.numero
                        WHERE e.tipo1 IN ('Água', 'Fogo')
                        UNION
                        SELECT p.numero, p.id_pokemon, e.nome, e.tipo1, e.tipo2
                        FROM pokemon p
                        INNER JOIN especie e ON p.numero = e.numero
                        WHERE e.tipo2 IN ('Água', 'Fogo');
                        """
                        
                    case 7:  # função escalar
                        consulta = """
                        SELECT COUNT(*) as total_pokemons
                        FROM pokemon;
                        """
                        
                    case 8:  # anti-join (NOT EXISTS)
                        consulta = """
                        SELECT p.numero, p.id_pokemon, e.nome as nome_especie, 
                            p.rota, p.regiao
                        FROM pokemon p
                        INNER JOIN especie e ON p.numero = e.numero
                        WHERE NOT EXISTS (
                            SELECT 1
                            FROM treinador t
                            WHERE t.id = p.id_treinador
                        )
                        AND p.id_treinador IS NULL;
                        """

                    case 9:  # Subconsulta tabela (IN)
                        consulta = """
                    SELECT e1.numero, e1.nome as especie_base, e2.nome as evolucao
                    FROM especie e1
                    INNER JOIN especie e2 ON e1.numero = e2.pre_evolucao
                    WHERE e1.numero IN (
                        SELECT DISTINCT pre_evolucao
                        FROM especie
                        WHERE pre_evolucao IS NOT NULL
                    );
                    """
                        
                    case _:
                        print("Não é uma consulta válida")
                        continue
                
                if consulta.strip():
                    cursor.execute(consulta)
                    resultados = cursor.fetchall()
                    
                    if resultados:
                        print(f"\n========== RESULTADO DA CONSULTA {num} ==========")
                        for linha in resultados:
                            print(linha)
                    else:
                        print("Nenhum registro encontrado.")
                    print("=" * 40)
    
    conn.close()

if __name__ == "__main__":
    main()