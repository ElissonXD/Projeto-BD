# Projeto de Banco de Dados

![pokemon](https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/1200px-International_Pok%C3%A9mon_logo.svg.png)

Este repositório contém o projeto desenvolvido como parte da disciplina de **Banco de Dados**, com o tema **Pokémon**. O objetivo é modelar, implementar e consultar um banco de dados relacional com base em dados do universo Pokémon, aplicando os conceitos aprendidos em sala de aula.
---
### Uso BD relacional
Criação das tabelas
```python
python tabelas.py
```
Povoamento do banco
```python
python povoamento.py
```
Consultas:
```python
python consultas.py
```
---
### Projeto Lógico
![projeto logico](https://github.com/ElissonXD/Projeto-BD/blob/main/Projeto_SQL/Conceitual.png?raw=true)
---
### Entidades Principais
O projeto contem as seguintes entidades:

1. **TREINADOR**
* `id`
* `nome`

2. **ESPECIE**
* `numero`
* `nome`
* `pre_evolucao`
* `tipo_1`
* `tipo_2`

3. **PROFESSOR**
* `id` *(referência a TREINADOR)*
* `area_de_pesquisa`

4. **LIDER**
* `id` *(referência a TREINADOR)*

5. **GINASIO**
* `cidade`
* `nome`
* `tipo`
* `id` *(referência a LIDER)*

6. **POKEMON**
* `indice`
* `numero` *(referência a ESPECIE)*
* `rota`
* `regiao`
* `id` *(referência a TREINADOR)*

7. **MOVIMENTO**
* `nome`
* `tipo`

8. **ITEM**
* `nome`
---
### Consultas implementadas

1. Treinador com mais de 3 pókemons
2. Nome de todos os ginásios com líder e nome do líder
3. Itens que não são recompensas de ginásio
4. Pokémons que evoluem
5. Treinadores que não lutaram contra nenhum ginásio
6. Treinador do pokémon
7. Espécies de todos os pokémons de líderes de ginásio da cidade de Pewter
8. Todas as especies com o mesmo tipo da espécie bulbasaur
9. Todos os itens ganhados em batalhas que também são pré-requisitos de evoluções
---
### Tecnologias Utilizadas
- **SQLite**
- **Python 3**
- **sqlite3**
---
### Integrantes
- César Cavalcanti
- Elisson Oliveira
- Gabriel Maciel
- Guilherme José
- Thawan Ribeiro da Silva
