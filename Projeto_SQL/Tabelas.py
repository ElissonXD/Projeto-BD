import sqlite3 as sql


conn = sql.connect('banco.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

#TREINADOR
cursor.execute("""
              CREATE TABLE treinador(
              id INTEGER NOT NULL PRIMARY KEY,
              nome VARCHAR(85) NOT NULL
);
""")

#PROFESSOR
cursor.execute("""
                CREATE TABLE professor(
                id INTEGER NOT NULL PRIMARY KEY,
                area_de_pesquisa VARCHAR(50) NOT NULL,
                FOREIGN KEY (id) REFERENCES treinador(id) ON DELETE CASCADE
);
""")

#LIDER
cursor.execute("""
                CREATE TABLE lider(
                id INTEGER NOT NULL PRIMARY KEY,
                FOREIGN KEY (id) REFERENCES treinador(id) ON DELETE CASCADE
);
""")

#GINASIO
cursor.execute("""
               CREATE TABLE ginasio(
               cidade VARCHAR(50) NOT NULL PRIMARY KEY,
               nome VARCHAR(50) NOT NULL,
               tipo VARCHAR(12) NOT NULL,
               id INTEGER UNIQUE,
               FOREIGN KEY (id) REFERENCES lider(id) ON DELETE CASCADE
);
""")

#ENFRENTA
cursor.execute("""
               CREATE TABLE enfrenta(
               cidade VARCHAR(50) NOT NULL,
               id INTEGER NOT NULL,
               data VARCHAR(10) NOT NULL,
               PRIMARY KEY(cidade, id, data),
               FOREIGN KEY (id) REFERENCES treinador(id) ON DELETE CASCADE,
               FOREIGN KEY (cidade) REFERENCES ginasio(cidade) ON DELETE CASCADE
);
""")

#ITEM
cursor.execute("""
              CREATE TABLE item(
              nome VARCHAR(50) NOT NULL PRIMARY KEY
);
""")

#TREINADOR RECEBE ITEM
cursor.execute("""
               CREATE TABLE recebe(
               cidade VARCHAR(50) NOT NULL,
               id INTEGER NOT NULL,
               data VARCHAR(10) NOT NULL,
               nome VARCHAR(50) NOT NULL,
               PRIMARY KEY(cidade, id, data, nome),
               FOREIGN KEY (cidade, id, data) REFERENCES enfrenta(cidade, id, data) ON DELETE CASCADE,
               FOREIGN KEY (nome) REFERENCES item(nome) ON DELETE CASCADE
);
""")

#ESPÉCIE
cursor.execute("""
               CREATE TABLE especie(
               numero INTEGER NOT NULL PRIMARY KEY,
               nome VARCHAR(50) UNIQUE NOT NULL,
               pre_evolucao INTEGER,
               pre_requisito VARCHAR(50),
               tipo1 VARCHAR(12) NOT NULL,
               tipo2 VARCHAR(12),
               FOREIGN KEY (pre_evolucao) REFERENCES especie(numero) ON DELETE CASCADE
);
""")

#POKEMON
cursor.execute("""
               CREATE TABLE pokemon(
               numero INTEGER NOT NULL,
               id_pokemon INTEGER NOT NULL,
               id_treinador INTEGER,
               rota VARCHAR(50),
               regiao VARCHAR(50),
               PRIMARY KEY(numero, id_pokemon),
               FOREIGN KEY (id_treinador) REFERENCES treinador(id) ON DELETE CASCADE,
               FOREIGN KEY (numero) REFERENCES especie(numero) ON DELETE CASCADE
);
""")

#MOVIMENTO
cursor.execute("""
              CREATE TABLE movimento(
              nome VARCHAR(50) NOT NULL PRIMARY KEY,
              tipo VARCHAR(12) NOT NULL
);
""")

#POKEMON TEM MOVIMENTO
cursor.execute("""
               CREATE TABLE tem(
               nome VARCHAR(50) NOT NULL,
               indice INTEGER NOT NULL,
               numero INTEGER NOT NULL,
               PRIMARY KEY(nome, indice, numero),
               FOREIGN KEY (indice, numero) REFERENCES pokemon(id_pokemon, numero) ON DELETE CASCADE,
               FOREIGN KEY (nome) REFERENCES movimento(nome) ON DELETE CASCADE
);
""")

#TREINADOR ENSINA MOVIMENTO A POKEMON
cursor.execute("""
               CREATE TABLE ensina(
               nome VARCHAR(50) NOT NULL,
               id_pokemon INTEGER NOT NULL,
               numero INTEGER NOT NULL,
               id_treinador INTEGER NOT NULL,
               PRIMARY KEY(nome, id_pokemon, numero),
               FOREIGN KEY (id_pokemon, numero) REFERENCES pokemon(id_pokemon, numero) ON DELETE CASCADE,
               FOREIGN KEY (nome) REFERENCES movimento(nome) ON DELETE CASCADE,
               FOREIGN KEY (id_treinador) REFERENCES treinador(id) ON DELETE CASCADE
);
""")
