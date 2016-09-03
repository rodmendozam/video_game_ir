from pymongo import MongoClient
import json
import datetime
import ast
import re

conn = MongoClient('mongodb://localhost:27017/')

db = conn['review_database']
posts = db['meta_data']

i = 0
with open('output.strict') as data_file:
    for line in data_file:
        j = json.loads(line)
        posts.insert(j)
        i += 1
        break
# # for d in posts.find()[:10]:
# #     print d

print i
# # db.drop_collection('meta_data')
# #
print conn.database_names()
print db.collection_names()
