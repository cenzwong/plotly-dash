from pymongo import MongoClient

URL_Mongo = 'mongodb://msbd5003-mongodb:zsETiWDaAJdqODfOg62miplS9kHMEs5N5xhmgyIzSzEaOKVfMdJp7IUThBqd7obK1OBsnR1n2hHqMdORMCCx6w==@msbd5003-mongodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@msbd5003-mongodb@'
client = MongoClient(URL_Mongo)

# Accessing Database
print(client.list_database_names())
db_credit = client['credit']