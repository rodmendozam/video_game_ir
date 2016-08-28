# import pymongo
#
#
# from pymongo import MongoClient
#
#
# client = MongoClient('mongodb://localhost:27017/')
# db = client['test-database']
# collection = db['test-collection']
#
#
# import datetime
# post = {"author": "Mike",
#         "text": "My first blog post!",
#          "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
#
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print(post_id)
#
#
# print(client.database_names())


from pymongo import MongoClient
import json

# conn = MongoClient('mongodb://localhost:27017/')
# db = conn['test-collection']
# postings = db.postings_collection
#
# class Posting(object):
#     def __init__(self, link, found=None, expired=None):
#         self.link = link
#         self.found = found
#         self.expired = expired
#
# posting = Posting('objectlink1')
#
# # print(posting.found)
#
# # value = json.dumps(posting, default=lambda x:x.__dict__)
# postings.insert(posting.__dict__)
#
#
# for d in postings.find()[:10]:
#     print(d)



from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test-database']
collection = db['test-collection']

my_json = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": "today"},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": "yesterday"}]

j = json.load(my_json)

print(j)




# print(my_json.__dict__)




























