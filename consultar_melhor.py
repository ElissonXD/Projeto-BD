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

    resposta = input("Deseja consultar tudo? (sim/nao): ").strip().lower()

    if resposta == "sim":
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
        consulta = """
        SELECT t.id, t.nome, p.area_de_pesquisa
        FROM treinador t
        JOIN professor p ON t.id = p.id
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()

        if resultado:
            for linha in resultado:
                print(f"ID: {linha[0]}, Nome: {linha[1]}, Área de pesquisa: {linha[2]}")
        else:
            print("Nenhum professor encontrado com base nos treinadores.")
        print("=" * 40)

    conn.close()


if __name__ == "__main__":
    main()
