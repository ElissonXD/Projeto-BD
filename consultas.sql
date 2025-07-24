/* Goup by/Having
    Projetar os treinadores com mais de 3 pokémons
    */

        SELECT P.id_treinador, COUNT(*) AS NUM_POKEMON
        FROM pokemon P
        GROUP BY P.id_treinador
        HAVING COUNT(*) > 3;

/* Junção interna:
    Projetar o nome de todos os ginásios e o nome de seu respectivo líder
     */

        SELECT G.nome AS GINASIO, L.nome AS LIDER
        FROM ginasio G INNER JOIN
            lider L on G.id = L.id

/* Junção Extetna:
    Projetar os itens que não são recompensas de ginásios
    */

        SELECT I.nome 
        FROM item I LEFT OUTER JOIN
            recebe R ON I.nome = R.nome
        WHERE R.nome is NULL;

/* Semi junção:
    Projetar os pokémons que evoluem
    */

        SELECT E.nome 
        FROM especie e
        WHERE EXISTS (
            SELECT E2.numero
            FROM especie E2
            WHERE E.numero = E2.numero
        );

/* Anti-junção:
    Projetar os treinadores que não lutaram contra nenhum ginásio
    */

        SELECT T.nome
        FROM treinador T
        WHERE NOT EXISTS (
            SELECT E.id
            FROM enfrenta E
            WHERE E.id = T.id
        );

/* Subconsulta do tipo escalar:
    Projetar a quantidade de espécies registradas
    */

        SELECT COUNT(*) as total_pokemons
                        FROM especie;

/* Subconsulta do tipo linha:
    Projetar o treinador do pokémon {COLOCAR AQUI ALGUM POKÉMON ALEATÓRIO}
    */

        SELECT *
        FROM treinador T 
        WHERE T.id = (
            SELECT P.id_treinador
            FROM pokemon P
            WHERE P.numero = X AND P.id_pokemon = Y
        );

/* Subconsulta do tipo tabela:
    Projetar as espécies de todos os Pokémons do líder de um ginásio de uma determinada cidade
    */

        SELECT *
        FROM especie E
        WHERE E.numero IN (
            SELECT P.numero
            FROM pokemon P
            WHERE P.id_treinador IN (
                SELECT G.id
                FROM ginasio G 
                WHERE G.cidade = Pewter
            )
        ) 

/* Operação de Conjunto: 
    Selecionar todos os pré-requisitos de evolução que também são itens recebidos de um ginásio
    */

            SELECT E.pre_requisito
            FROM especie e
        INTERSECT
            SELECT R.nome
            FROM recebe R
