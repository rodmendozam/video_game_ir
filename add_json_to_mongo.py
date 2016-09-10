from pymongo import MongoClient
import json
import datetime

conn = MongoClient('mongodb://localhost:27017/')

db = conn['review_database']
posts = db['full_collection']
#
i = 0
with open('reviews_Video_Games.json') as data_file:
    for line in data_file:
        j = json.loads(line)
        # print type(j)
        posts.insert(j)
        i += 1
# for d in posts.find()[:10]:
#     print d
print(i)
# db.drop_collection('postings_collection')

print(conn.database_names())