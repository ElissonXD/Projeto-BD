import sqlite3 as sql


conn = sql.connect('banco.db')
cursor = conn.cursor()

resposta = input("consultar tudo?: ")

if resposta == "sim":

    print("===========TREINADOR===========")
    cursor.execute("""
    SELECT * FROM treinador;
    """)

    for linha in cursor.fetchall():
        print(linha)

    print("======================")

    print("===========PROFESSOR===========")
    cursor.execute("""
    SELECT * FROM professor;
    """)

    for linha in cursor.fetchall():
        print(linha)

    print("======================")
else:

    print("============CONSULTA=============")

    cursor.execute("""
    SELECT t.id, t.nome, p.area_de_pesquisa FROM treinador t, professor p WHERE t.id = p.id 
    """)

    
    print(bool(cursor.fetchall()))

    print("======================")