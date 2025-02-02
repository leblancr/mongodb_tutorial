# mongo_utils.py

from dotenv import load_dotenv
import os
from pymongo import MongoClient

# User data for connect strings
user_data = {
    'local': {
       'prefix': '',
       'postfix': '',
       'cluster': 'localhost:27017',
       'host': 'localhost:27017',
       'users': {
           'rich': {
               'password': 'reddmon',
               'databases': []
           }
       }
    },
    'Atlas': {
       'prefix': '+srv',
       'postfix': '?retryWrites=true&w=majority',
       'cluster': 'cluster0.yymy7y6.mongodb.net',
       'host': 'cluster0.yymy7y6.mongodb.net',
       'users': {
           'rich': {
               'password': '9hzGTIA1HjKra6fG',
               'databases': []
           },
           'rkba1': {
               'password': 'Hiu55xZe0buUedBd',
               'databases': []
           }
       }
    }
}


def get_mongo_client(uri):
    """Establishes and returns a MongoClient connection."""
    print(f"Getting client for {uri}")
    return MongoClient(uri)


def get_database_names(client):
    """Return a lists of all databases in the connected MongoDB instance."""
    databases = client.list_database_names()
    return databases


def list_collections(db):
    """Lists all collections in the specified database."""
    collections = db.list_collection_names()
    for collection in collections:
        print(collection)
    print()


def list_database_names(client):
    """Lists all databases in the connected MongoDB instance."""
    databases = client.list_database_names()
    for db in databases:
        print(db)
    print()


def close_client(client):
    """Closes the MongoClient connection."""
    if client:
        print(f"Closing {client}")
        client.close()
        