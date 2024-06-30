import traceback
from datetime import datetime, timezone
import os
import bson
from bson import ObjectId

from pprint import pprint
from datetime import datetime  # Import datetime class from datetime module

from mongo_utils import get_database_names, list_database_names, list_collections


def run(client, user):
    print(f"Running {__name__}.py")

    try:
        # print(f"{user} databases:")
        # list_database_names(client)
        # database_names = get_database_names(client)
        databases = client.list_database_names()
        print(f"database: {databases}")
        db = client['test_database']
        collections = db.list_collection_names()
        print(f"test_database collections: {collections}")

        for collection in collections:
            cursor = db[collection]  # Replace 'test_collection' with your actual collection name

            print(f"cursor: {cursor}")
            print(f"{collection} documents:")
            for document in cursor.find():
                pprint(document)

        # result = collection.delete_one({'_id': ObjectId('667495007d7b236c50a26a14'), 'test_key': 'test_value'})
        # return

        # Print all databases in the client
        for database_name in get_database_names(client):
            print(f"{database_name} collections:")
            db = client[database_name]
            list_collections(db)

            # show documents in each collection
            for collection_name in db.list_collection_names():
                print(f"{collection_name} documents:")
                documents = db[collection_name].find()

                for document in documents:
                    pprint(document)

        post = {
            "author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.now(tz=timezone.utc),
        }

        db = client['sample_mflix']  # Get 'sample_mflix' database
        print(f"{db.name} collections:")
        list_collections(db)

        collection = db['movies']  # Get 'movies' collection

        # Get the document with the title 'Blacksmith Scene':
        title = 'The Great Train Robbery'
        print(f"Find {title}:")
        pprint(collection.find_one({'title': title}))
        print()

        # insert a new document
        document = {
            "title": "Parasite",
            "year": 2020,
            "plot": "A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks. "
            "But their easy life gets complicated when their deception is threatened with exposure.",
            "released": datetime(2020, 2, 7, 0, 0, 0),
         }

        # print('insert document:')
        # document_id = insert_document(collection, document)
        # print(f"_id of inserted document: {document_id}\n")
        #
        # # Look up the document you just created in the collection:
        # print(f"Get document with id: {document_id}\n")
        # print(collection.find_one({'_id': bson.ObjectId(document_id)}))

        # Look up the documents you've created in the collection:
        title = 'Parasite'
        print(f"Get documents with title: {title}\n")
        for doc in collection.find({"title": title}):
            pprint(doc)

        for doc in collection.find({
            'year': {'$lt': 1920},
            'genres': 'Romance'
        }):
            pprint(doc)

        # Update *all* the Parasite movie docs to the correct year:
        update_result = collection.update_many({"title": "Parasite"}, {"$set": {"year": 2019}})

        # collection.delete_one(
        #     {"title": "Parasite"}
        # )

        # Count all documents in the collection
        document_count = collection.count_documents({"title": "Parasite"})

        # Print the count
        print(f"Total Parasite documents in the movies: {document_count}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Traceback:")
        traceback.print_exc()


def insert_document(collection, document):
    # Insert a document for the movie 'Parasite':
    insert_result = collection.insert_one(document)
    
    # Save the inserted_id of the document you just created:
    document_id = insert_result.inserted_id
    return document_id
    