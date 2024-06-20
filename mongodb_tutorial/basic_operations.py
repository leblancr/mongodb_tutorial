import datetime   # This will be needed later
import os
import bson
from bson import ObjectId

from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime  # Import datetime class from datetime module


def main():
    load_dotenv()  # Load config from a .env file:
    
    try:
        # mongodb_uri = os.environ['MONGODB_URI_LOCAL']
        mongodb_uri = os.environ['MONGODB_URI_ATLAS']
        print(f"mongodb_uri: {mongodb_uri}\n")
    except KeyError as e:
        print("Error: environment variable is not set.", e)
        exit(1)
    
    client = MongoClient(mongodb_uri)  # Connect to  MongoDB cluster
    print('database_names:')
    list_databases(client)
    
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
    print(f'Total Parasite documents in the movies: {document_count}')
    

def list_databases(client):
    # List all the databases in the cluster:
    for db_info in client.list_database_names():
        print(db_info)
    print()  


def list_collections(db):
    # List all the collections in db
    collections = db.list_collection_names()
    for collection in collections:
        print(collection)
    print()  
      

def insert_document(collection, document):
    # Insert a document for the movie 'Parasite':
    insert_result = collection.insert_one(document)
    
    # Save the inserted_id of the document you just created:
    document_id = insert_result.inserted_id
    return document_id
    
    # # Update the document with the correct year:
    # update_result = movies.update_one({ '_id': parasite_id }, {
    #    '$set': {"year": 2019}
    # })
    # 
    # # Print out the updated record to make sure it's correct:
    # pprint(movies.find_one({'_id': ObjectId(parasite_id)}))
    
    # Update *all* the Parasite movie docs to the correct year:
    # update_result = movies.update_many({"title": "Parasite"}, {"$set": {"year": 2019}})
    # movies.delete_one(
    #     {"title": "Parasite",}
    #  )
    


if __name__ == '__main__':
    main()
   