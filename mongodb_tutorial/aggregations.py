import datetime
import os
from pymongo import MongoClient

from mongo_utils import get_mongo_client, get_database_names, list_collections, list_database_names


def run():
    try:
        mongodb_uri = os.environ['MONGODB_URI_LOCAL']
        # client = MongoClient("localhost", 27017)
        client = get_mongo_client(mongodb_uri)
        print('client databases:')
        list_database_names(client)
        
        database_names = get_database_names(client)
        
        for database_name in database_names:
            print('database_name:', database_name)
            if database_name in ['config', 'local']:
                print('* skipping', database_name)
                continue
            print(f"{database_name} collections:")
            db = client[database_name]
            list_collections(db)
            print(f"{database_name} collection names:")
            collection_names = db.list_collection_names()
            print(collection_names)
            
            # show documents in each collection
            for collection_name in collection_names:
                print(f"{collection_name} documents:")
                cursor = db[collection_name].find()
                for document in cursor:
                    print(document)
        # print(f"collection: {collection}")
        # #print(dir(collection))
        # print(f"collection.name: {collection.name}")
        # 
        # for doc in collection.find():
        #     print(doc)
            
        post = {
            "author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.now(tz=datetime.timezone.utc),
        }
        
    except KeyError as e:
        print("Error: ", e)

        
