# from pymongo import MongoClient
# import json
# import re
#
#
# conn = MongoClient('mongodb://localhost:27017/')
#
# db = conn['review_database']
# posts = db['meta_collection']
# #
# i = 0
# # meta_Video_Games.json
# # reviews_Video_Games.json
#
#
# with open('meta_Video_Games.json') as data_file:
#     for line in data_file:
#         # line = line.replace("'", '"')
#         # line = '{\'asin\'s\': \'0078764343\'}'
#
#         line = line.replace("'", '"')
#         # [a-z]"[a-z]
#         line = re.sub('[a-z]"[a-z]', lambda x: x.group(0).replace('"', "'"), line)
#         # line = re.sub('\\\\"', lambda x: x.group(0).replace('\\', ""), line)
#         line = re.sub('\\\\"[a-z]', lambda x: x.group(0).replace('\\"', "'"), line)
#         # line = line.replace("\\", '')
#         # line = re.sub("'[A-Z]", lambda x: x.group(0).replace("'", '"'), line)
#         # line = re.sub("[a-z]'", lambda x: x.group(0).replace("'", '"'), line)
#         # line = re.sub("[A-Z]'", lambda x: x.group(0).replace("'", '"'), line)
#         # line = re.sub("'[0-9]", lambda x: x.group(0).replace("'", '"'), line)
#         # line = re.sub("[0-9]'", lambda x: x.group(0).replace("'", '"'), line)
#         print(line)
#         # break
#         j = json.loads(line)
#         # print type(j)
#         # posts.insert(j)
#         # i += 1
# # for d in posts.find()[:10]:
# #     print d
# # print(i)
# # db.drop_collection('postings_collection')
#
# # print(conn.database_names())
#
# faulty_json = ''


from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import datetime
import ast
import re

conn = MongoClient('mongodb://localhost:27017/')
db = conn['review_database']
posts_meta = db['meta_data']
posts_full_data = db['full_collection']
posts_meta_data = db['meta_data']

#meta_data is the collection for metadata of each game
#full_collection is the data base with all the elemnts

print(posts_full_data.find_one())
print(posts_meta.find_one())

one_post = posts_full_data.find_one({"_id": ObjectId('57cad6c26c3c6b298c9f79ac')})


print('\nLoop over elements: ')
for x in posts_meta_data.find()[:5]:
    print(x)

# print(posts_full_data.find)


print('\nDatabase info: ')
print('Databases: ', conn.database_names())
print('Collections: ', db.collection_names())























