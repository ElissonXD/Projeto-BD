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
 1  | Treinador com mais de 3 pókemons
 2  | Nome de todos os ginásios com líder e nome do líder
 3  | Itens que não são recompensas de ginásio
 4  | Pokémons que evoluem
 5  | Treinadores que não lutaram contra nenhum ginásio
 6  | Treinador do pokémon
 7  | Espécies de todos os pokémons de líderes de ginásio da cidade de Pewter
 8  | Todas as especies com o mesmo tipo da espécie bulbasaur
 9  | Todos os itens ganhados em batalhas que também são pré-requisitos de evoluções\n""")
                
                num = int(input("Numero da consulta: "))
                consulta = ""
                
                match num:
                    case 0:
                        break
                        
                    case 1:  # Group By + Having
                        consulta = """
                        SELECT P.id_treinador, COUNT(*) AS NUM_POKEMON
                        FROM pokemon P
                        WHERE P.id_treinador is NOT NULL
                        GROUP BY P.id_treinador
                        HAVING COUNT(*) > 3;
                        """
                        
                    case 2:  # Junção Interna
                        consulta = """
                        SELECT G.nome AS GINASIO, T.nome AS LIDER
                        FROM ginasio G INNER JOIN
                            lider L on G.id = L.id INNER JOIN treinador T on T.id = L.id
                        """
                        
                    case 3:  # Junção Externa
                        consulta = """
                        SELECT I.nome 
                        FROM item I LEFT OUTER JOIN
                            recebe R ON I.nome = R.nome
                        WHERE R.nome is NULL;
                        """
                        
                    case 4:  # Semi Junção
                        consulta = """
                        SELECT E.nome 
                        FROM especie E
                        WHERE EXISTS (
                            SELECT E2.numero
                            FROM especie E2
                            WHERE E.numero = E2.pre_evolucao
                        );
                        """
                        
                    case 5:  # Anti Junção
                        consulta = """
                        SELECT T.nome
                        FROM treinador T
                        WHERE NOT EXISTS (
                            SELECT E.id
                            FROM enfrenta E
                            WHERE E.id = T.id
                        );
                        """
                
                    case 6:  # Subconsulta escalar
                        while True:
                            try:
                                numero_pokemon = int(input("Insira o número do pokémon: "))
                                id_pokemon = int(input("Insira o ID do pokémon: "))
                                consulta = f"""
                                SELECT *
                                FROM treinador T 
                                WHERE T.id = (
                                    SELECT P.id_treinador
                                    FROM pokemon P
                                    WHERE P.numero = {numero_pokemon} AND P.id_pokemon = {id_pokemon}
                                );
                                """
                                break
                            except:
                                print("Entradas inválidas!")
                        
                    case 7:  # Subconsulta Tabela com ESCALAR
                        consulta = """
                        SELECT *
                        FROM especie E
                        WHERE E.numero IN (
                            SELECT P.numero
                            FROM pokemon P
                            WHERE P.id_treinador = (
                                SELECT G.id
                                FROM ginasio G 
                                WHERE G.cidade = 'Pewter'
                            )
                        ) 
                        """

                    case 8: # Subconsulta Linha
                        consulta = """
                        SELECT nome, tipo1, tipo2
                        FROM especie e
                        WHERE (e.tipo1, e.tipo2) = (SELECT e1.tipo1, e1.tipo2
                                                FROM especie e1
                                                WHERE e1.numero = 1) 
                        """


                    case 9: # Operação de Conjunto
                        consulta = """
                        SELECT E.pre_requisito
                        FROM especie e
                    INTERSECT
                        SELECT R.nome
                        FROM recebe R"""

                    
    
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
