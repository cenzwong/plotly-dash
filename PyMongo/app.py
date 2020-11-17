from pymongo import MongoClient
import pprint as pp

URL_Mongo = 'mongodb://'
client = MongoClient(URL_Mongo)

# Accessing Database
print(client.list_database_names())
db_credit = client['credit']

# Collection - application
print(db_credit.list_collection_names())
db_credit_application = db_credit['application']

pp.pprint(db_credit_application.count_documents({}))

documents = db_credit_application.find({"NAME_CONTRACT_TYPE" : "Revolving loans"})
pp.pprint(documents[0])

pp.pprint(db_credit_application.count_documents({"NAME_CONTRACT_TYPE" : "Revolving loans"}))

db_credit_application.distinct("CODE_GENDER")

# Collection - installment
print(db_credit.list_collection_names())
db_credit_installment = db_credit['installment']

documents = db_credit_installment.find({})
pp.pprint(documents)

# Collection - prev_application
print(db_credit.list_collection_names())
db_credit_prev_application = db_credit['prev_application']

documents = db_credit_prev_application.find({})
pp.pprint(documents[0])
pp.pprint(db_credit_prev_application.find_one())




# ## Example
# db = MongoClient(URL_Mongo).aggregation_example
# result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
#                                  {"x": 2, "tags": ["cat"]},
#                                  {"x": 2, "tags": ["mouse", "cat", "dog"]},
#                                  {"x": 3, "tags": []}])
# result.inserted_ids

# from bson.son import SON
# # pipeline = [
# #     {"$unwind": "$tags"},
# #     {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
# #     {"$sort": SON([("count", -1), ("_id", -1)])}
# # ]
# pipeline = [
#     {"$unwind": "$tags"}
#     # {"$group": {"_id": "$tags", "count": {"$sum": 1}}}
# ]
# pp.pprint(list(db.things.aggregate(pipeline)))
# # pp.pprint(db.command('aggregate', 'things', pipeline=pipeline, explain=True))
# temp = db.things.aggregate([{"$unwind": "$tags"}])
# for result in db.things.aggregate([{"$unwind": "$tags"}]):
#     pp.pprint(result)
