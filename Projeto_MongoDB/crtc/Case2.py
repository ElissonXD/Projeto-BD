#um documento embutindo apenas um documento
import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
banco = cliente['banco_de_dados']

especies = banco['especie']

lista_especies = [
    {
        "_id": 1, 
        "nome": "Bulbasaur", 
        "tipos": ["Planta", "Veneno"], 
        "pre_evolucao": None, 
        "pre_requisito": None
    },
    {
        "_id": 2, 
        "nome": "Ivysaur", 
        "tipos": ["Planta", "Veneno"], 
        "pre_evolucao": {
            "_id": 1, 
            "nome": "Bulbasaur", 
            "tipos": ["Planta", "Veneno"], 
            "pre_evolucao": None, 
            "pre_requisito": None
        }, 
        "pre_requisito": "Nível 16"
    },
    {
        "_id": 3, 
        "nome": "Venusaur", 
        "tipos": ["Planta", "Veneno"], 
        "pre_evolucao": {
            "_id": 2, 
            "nome": "Ivysaur", 
            "tipos": ["Planta", "Veneno"], 
            "pre_evolucao": {
                "_id": 1, 
                "nome": "Bulbasaur", 
                "tipos": ["Planta", "Veneno"], 
                "pre_evolucao": None, 
                "pre_requisito": None
            }, 
            "pre_requisito": "Nível 16"
        }, 
        "pre_requisito": "Nível 36"
    },
    {
        "_id": 4, 
        "nome": "Charmander", 
        "tipos": ["Fogo"], 
        "pre_evolucao": None, 
        "pre_requisito": None
    },
    {
        "_id": 5, 
        "nome": "Charmeleon", 
        "tipos": ["Fogo"], 
        "pre_evolucao": {
            "_id": 4, 
            "nome": "Charmander", 
            "tipos": ["Fogo"], 
            "pre_evolucao": None, 
            "pre_requisito": None
        }, 
        "pre_requisito": "Nível 16"
    },
    {
        "_id": 6, 
        "nome": "Charizard", 
        "tipos": ["Fogo", "Voador"], 
        "pre_evolucao": {
            "_id": 5, 
            "nome": "Charmeleon", 
            "tipos": ["Fogo"], 
            "pre_evolucao": {
                "_id": 4, 
                "nome": "Charmander", 
                "tipos": ["Fogo"], 
                "pre_evolucao": None, 
                "pre_requisito": None
            }, 
            "pre_requisito": "Nível 16"
        }, 
        "pre_requisito": "Nível 36"
    },
    {
        "_id": 7, 
        "nome": "Squirtle", 
        "tipos": ["Água"], 
        "pre_evolucao": None, 
        "pre_requisito": None
    },
    {
        "_id": 8, 
        "nome": "Wartortle", 
        "tipos": ["Água"], 
        "pre_evolucao": {
            "_id": 7, 
            "nome": "Squirtle", 
            "tipos": ["Água"], 
            "pre_evolucao": None, 
            "pre_requisito": None
        }, 
        "pre_requisito": "Nível 16"
    },
    {
        "_id": 9, 
        "nome": "Blastoise", 
        "tipos": ["Água"], 
        "pre_evolucao": {
            "_id": 8, 
            "nome": "Wartortle", 
            "tipos": ["Água"], 
            "pre_evolucao": {
                "_id": 7, 
                "nome": "Squirtle", 
                "tipos": ["Água"], 
                "pre_evolucao": None, 
                "pre_requisito": None
            }, 
            "pre_requisito": "Nível 16"
        }, 
        "pre_requisito": "Nível 36"
    },
    {
        "_id": 133, 
        "nome": "Eevee", 
        "tipos": ["Normal"], 
        "pre_evolucao": None, 
        "pre_requisito": None
    },
    {
        "_id": 134, 
        "nome": "Vaporeon", 
        "tipos": ["Água"], 
        "pre_evolucao": {
            "_id": 133, 
            "nome": "Eevee", 
            "tipos": ["Normal"], 
            "pre_evolucao": None, 
            "pre_requisito": None
        }, 
        "pre_requisito": "Pedra de água"
    },
    {
        "_id": 135, 
        "nome": "Jolteon", 
        "tipos": ["Elétrico"], 
        "pre_evolucao": {
            "_id": 133, 
            "nome": "Eevee", 
            "tipos": ["Normal"], 
            "pre_evolucao": None, 
            "pre_requisito": None
        }, 
        "pre_requisito": "Pedra do trovão"
        },
    {
        "_id": 136, 
        "nome": "Flareon", 
        "tipos": ["Fogo"], 
        "pre_evolucao": {
            "_id": 133, 
            "nome": "Eevee", 
            "tipos": ["Normal"], 
            "pre_evolucao": None, 
            "pre_requisito": None
        }, 
        "pre_requisito": "Pedra de fogo"
    }
]