import datetime   # This will be needed later
import os
import bson
from bson import ObjectId

from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime  # Import datetime class from datetime module


def main():
    # Load config from a .env file:
    load_dotenv()
    
    try:
        # mongodb_uri = os.environ['MONGODB_URI_LOCAL']
        mongodb_uri = os.environ['MONGODB_URI_ATLAS']
        print(f"mongodb_uri: {mongodb_uri}\n")
    except KeyError as e:
        print("Error: environment variable is not set.", e)
        exit(1)
    
    # Connect to your MongoDB cluster:
    client = MongoClient(mongodb_uri)
    
    print('database_names:')
    list_databases(client)
    
    # Get a reference to the 'sample_mflix' database:
    db = client['sample_mflix']
    print(f"{db.name} collections:")
    list_collections(db)
    
    # Get a reference to the 'movies' collection:
    collection = db['movies']
    
    # Get the document with the title 'Blacksmith Scene':
    pprint(collection.find_one({'title': 'The Great Train Robbery'}))
    
    document = {
        "title": "Parasite",
        "year": 2020,
        "plot": "A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks. "
        "But their easy life gets complicated when their deception is threatened with exposure.",
        "released": datetime(2020, 2, 7, 0, 0, 0),
     }
    
    document_id = insert_document(collection, document)
    print(f"_id of inserted document: {document_id}")
    
    # Look up the document you just created in the collection:
    print(collection.find_one({'_id': bson.ObjectId(document_id)}))
    

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
    
    # # Look up the documents you've created in the collection:
    # for doc in movies.find({"title": "Parasite"}):
    #     pprint(doc)
    #   
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
    
    # # Count all documents in the collection
    # document_count = movies.count_documents({"title": "Parasite"})
    # 
    # # Print the count
    # print(f'Total documents in the movies: {document_count}')
    # 


if __name__ == '__main__':
    main()
   