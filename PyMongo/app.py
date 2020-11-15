from pymongo import MongoClient

URL_Mongo = ''
client = MongoClient(URL_Mongo)

# Accessing Database
print(client.list_database_names())
db_credit = client['credit']

db_credit_installment = db_credit['installment']

documents = db_credit_installment.find({})
documents[0]["AMT_PAYMENT"]
# >>3982.05