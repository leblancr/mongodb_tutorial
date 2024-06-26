import datetime
import pprint

from mongo_utils import get_mongo_client, get_database_names, list_collections, list_database_names


def run(client, uri):
    try:
        print(f"{uri} databases:")
        list_database_names(client)
        database_names = get_database_names(client)
        
        # Print all databases in the client
        for database_name in database_names:
            print(f"{database_name} collections:")
            db = client[database_name]
            list_collections(db)
            
            # show documents in each collection
            for collection_name in db.list_collection_names():
                print(f"{collection_name} documents:")
                documents = db[collection_name].find()

                for document in documents:
                    pprint.pprint(document)

        post = {
            "author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.now(tz=datetime.timezone.utc),
        }
        
    except KeyError as e:
        print("Error: ", e)

        
