import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")

cliente.drop_database('banco_de_dados')

print("O banco de dados 'banco_de_dados' foi completamente apagado.")