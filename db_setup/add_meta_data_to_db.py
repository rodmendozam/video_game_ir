from pymongo import MongoClient
import json
import gzip

class MetadataLoader():
    def __init__(self):
        self.conn = MongoClient('mongodb://localhost:27017/')
        self.db = self.conn['review_database']
        self.posts = self.db['meta_data']

    def delete_collection(self):
        self.db.drop_collection('meta_data')

    def insert_collection_into_db(self):
        i = 0
        with open('../output.strict') as data_file:
            for line in data_file:
                j = json.loads(line)
                self.posts.insert(j)
                i += 1
        print('Number of entries modified: ', i)

    def print_info(self):
        print('DB names: ', self.conn.database_names())
        print('Collections names: ', self.db.collection_names())
        print('Top 5 entries: \n')
        for d in self.posts.find()[:5]:
            print(d)

    def fix_unstrict_to_strict_json(self, path):
        f = open("../output.strict", 'w')
        for l in self.parse("../meta_Video_Games.json.gz"):
            f.write(l + '\n')

    def parse(self, path):
        g = gzip.open(path, 'r')
        for l in g:
            yield json.dumps(eval(l))

if __name__ == "__main__":
    meta_connector = MetadataLoader()
    meta_connector.print_info()


    #fix json was in unstrict
    # meta_connector.fix_unstrict_to_strict_json()


    #reload DB -> drop then insert
    # meta_connector.delete_collection()
    # meta_connector.insert_collection_into_db()







