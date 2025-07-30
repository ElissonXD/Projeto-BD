import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

treinadores = banco['treinador']

lista_treinadores_case_3 = [
    {"_id": 1, "nome": "treinador_1", "pokemon":[1]},
    {"_id": 2, "nome": "treinador_2", "pokemon":[2]},
    {"_id": 3, "nome": "treinador_3", "pokemon":[3]},
    {"_id": 4, "nome": "treinador_4", "pokemon":[4]},
    {"_id": 5, "nome": "treinador_5", "pokemon":[5]},
    {"_id": 6, "nome": "treinador_6", "pokemon":[6]},
    {"_id": 7, "nome": "treinador_7", "pokemon":[7]},
    {"_id": 8, "nome": "treinador_8", "pokemon":[8]},
    {"_id": 9, "nome": "treinador_9", "pokemon":[9]},
    {"_id": 10, "nome": "treinador_10", "pokemon":[10]}
    ]

pokemons = banco['pokemon']

lista_pokemons_case_3 =[
    {
    "_id": 1,
    "especie": 25,
    "index": 1,
    "tipo": "eletrico",
    "nome": "Pikachu",
    "rota": "rota 1",
    "regiao": "kanto"
    }
    ,
    {
    "_id": 2,
    "especie": 4,
    "index": 1,
    "tipo": "fogo",
    "nome": "Charmander",
    "rota": "rota 2",
    "regiao": "kanto"
    }
    ,
    {
    "_id": 3,
    "especie": 7,
    "index": 1,
    "tipo": "agua",
    "nome": "Squirtle",
    "rota": "rota 3",
    "regiao": "kanto"
    }
    ,
    {
    "_id": 4,
    "especie": 10,
    "index": 1,
    "tipo": "inseto",
    "nome": "Caterpie",
    "rota": "floresta de viridian",
    "regiao": "kanto" }
    ,
    {
    "_id": 5,
    "especie": 16,
    "index": 1,
    "tipo": "normal, voador",
    "nome": "Pidgey",
    "rota": "rota 5",
    "regiao": "kanto" }
    ,
    {
    "_id": 6,
    "especie": 74,
    "index": 1,
    "tipo": "pedra, terrestre",
    "nome": "Geodude",
    "rota": "mt. moon",
    "regiao": "kanto"}
    ,
    {
    "_id": 7,
    "especie": 63,
    "index": 1,
    "tipo": "psiquico",
    "nome": "Abra",
    "rota": "rota 24",
    "regiao": "kanto" }
    ,
    {
    "_id": 8,
    "especie": 92,
    "index": 1,
    "tipo": "fantasma, venenoso",
    "nome": "Gastly",
    "rota": "pokemon tower",
    "regiao": "kanto"}
    ,
    {
    "_id": 9,
    "especie": 129,
    "index": 1,
    "tipo": "agua",
    "nome": "Magikarp",
    "rota": "vermilion city",
    "regiao": "kanto"}
    ,
    {
    "_id": 10,
    "especie": 143,
    "index": 1,
    "tipo": "normal",
    "nome": "Snorlax",
    "rota": "rota 12",
    "regiao": "kanto"}
    
]


lista_treinadores_case_4 = [
    
  {
    "_id": 1,
    "nome": "treinador_1",
    "pokemon": [
      {
        "_id": 1,
        "especie": 25,
        "index": 1,
        "tipo": "eletrico",
        "nome": "Pikachu",
        "rota": "rota 1",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 2,
    "nome": "treinador_2",
    "pokemon": [
      {
        "_id": 2,
        "especie": 4,
        "index": 1,
        "tipo": "fogo",
        "nome": "Charmander",
        "rota": "rota 2",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 3,
    "nome": "treinador_3",
    "pokemon": [
      {
        "_id": 3,
        "especie": 7,
        "index": 1,
        "tipo": "agua",
        "nome": "Squirtle",
        "rota": "rota 3",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 4,
    "nome": "treinador_4",
    "pokemon": [
      {
        "_id": 4,
        "especie": 10,
        "index": 1,
        "tipo": "inseto",
        "nome": "Caterpie",
        "rota": "floresta de viridian",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 5,
    "nome": "treinador_5",
    "pokemon": [
      {
        "_id": 5,
        "especie": 16,
        "index": 1,
        "tipo": "normal, voador",
        "nome": "Pidgey",
        "rota": "rota 5",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 6,
    "nome": "treinador_6",
    "pokemon": [
      {
        "_id": 6,
        "especie": 74,
        "index": 1,
        "tipo": "pedra, terrestre",
        "nome": "Geodude",
        "rota": "mt. moon",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 7,
    "nome": "treinador_7",
    "pokemon": [
      {
        "_id": 7,
        "especie": 63,
        "index": 1,
        "tipo": "psiquico",
        "nome": "Abra",
        "rota": "rota 24",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 8,
    "nome": "treinador_8",
    "pokemon": [
      {
        "_id": 8,
        "especie": 92,
        "index": 1,
        "tipo": "fantasma, venenoso",
        "nome": "Gastly",
        "rota": "pokemon tower",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 9,
    "nome": "treinador_9",
    "pokemon": [
      {
        "_id": 9,
        "especie": 129,
        "index": 1,
        "tipo": "agua",
        "nome": "Magikarp",
        "rota": "vermilion city",
        "regiao": "kanto"
      }
    ]
  },
  {
    "_id": 10,
    "nome": "treinador_10",
    "pokemon": [
      {
        "_id": 10,
        "especie": 143,
        "index": 1,
        "tipo": "normal",
        "nome": "Snorlax",
        "rota": "rota 12",
        "regiao": "kanto"
      }
    ]
  }
]