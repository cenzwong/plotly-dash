from pymongo import MongoClient

URL_Mongo = ''
client = MongoClient(URL_Mongo)

# Accessing Database
print(client.list_database_names())
db_credit = client['credit']