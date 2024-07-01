from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure, OperationFailure

import os
import logging
import urllib.parse
import basic_operations
import aggregations
import custom_type_example


from mongo_utils import get_database_names, list_database_names, user_data

# logging.basicConfig(level=logging.DEBUG)


def run():
    print(f"Running {__name__}.py")
    client = None

    # For each environment get user databases then authenticate to them one by one
    try:
        # Each environment (local, Atlas) has user dictionaries
        for env in ['local']: # user_data.keys():
            print(f"\n*** {env} ***:")

            # For each user show their databases then connect one by one
            for user in user_data[env]['users']:
                print(f"{user} connecting to {user_data[env]['host']}")

                uri = f"mongodb{user_data[env]['prefix']}://{user}:{user_data[env]['users'][user]['password']}"\
                      f"@{user_data[env]['cluster']}/{user_data[env]['postfix']}"
                print('uri:', uri)

                # Connect to host, get databases then close connection
                client = MongoClient(uri)
                databases = client.list_database_names()
                print(f"{user} {env} databases: {databases}")
                client.close()

                databases = ['test']

                # For each databases run the example scripts
                for database in databases:
                    print(f"{user} ** connecting to {env} {database}:")
                    uri = f"mongodb{user_data[env]['prefix']}://{user}:{user_data[env]['users'][user]['password']}"\
                          f"@{user_data[env]['cluster']}/{database}{user_data[env]['postfix']}?authSource=admin"

                    # print('uri:', uri)
                    client = MongoClient(uri)

                    # Verify if the connection is successful
                    print(f"{user} connected to {env} {database} database successfully!")
                    # print(client.server_info())

                    # Now that connected to a database run scripts on it:
                    # basic_operations.run(client, user)  # shows all docs on all databases, very long time
                    # aggregations.run(client, uri)
                    custom_type_example.run(client)

                    print(f"{user} * closing connection to {env} {database}")
                    client.close()
    except ConnectionFailure as cf:
        print(f"MongoDB Connection Error: {cf}")
        # Handle connection failure (e.g., log, retry, etc.)
    except OperationFailure as of:
        print(f"MongoDB Operation Error: {of}")
        # Handle operation failure (e.g., authentication issue, permissions issue, etc.)
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        # Handle other exceptions not specific to MongoDB
    finally:
        if client:
            client.close()  # Close MongoClient instance if it was successfully created
