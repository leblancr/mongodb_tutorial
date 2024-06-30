from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure, OperationFailure

import os
import urllib.parse


def run():
    """
    user     password    databases
    local:
    rich     reddmon     roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
   
    Atlas:
    rich    9hzGTIA1HjKra6fG    readWriteAnyDatabase@admin
    rkba1   Hiu55xZe0buUedBd    atlasAdmin@admin
    """

    print(f"Running {__name__}.py")

    # User data for connect strings
    envs = {
        'local': {
            'prefix': '',
            'server1': '@localhost:27017/',
            'server2': '',
            'users': {
                'rich': {
                    'password': 'reddmon',
                    'databases': [
                        'admin',
                        'aggregation_example',
                        'config',
                        'local',
                        'sample_mflix',
                        'test_database'
                    ]
                }
            }
        },
        'Atlas': {
            'prefix': '+srv',
            'server1': '@cluster0.yymy7y6.mongodb.net/',
            'server2': '?retryWrites=true&w=majority&appName=Cluster0',
            'users': {
                'rich': {
                    'password': '9hzGTIA1HjKra6fG',
                    'databases': [
                        'admin',
                        'aggregation_example',
                        'config',
                        'local',
                        'sample_mflix',
                        'test_database'
                    ]
                },
                'rkba1': {
                    'password': 'Hiu55xZe0buUedBd',
                    'databases': [
                        'admin',
                        'aggregation_example',
                        'config',
                        'local',
                        'sample_mflix',
                        'test_database'
                    ]
                }
            }
        }
    }

    try:
        # Each environment (local, Atlas) has user dictionaries
        for env in envs.keys():
            # print(f"{env}:")
            
            # For each user dictionary print user
            for user in envs[env]['users']:
                # print(f"{user}:")
                # For each user show the dictionaries they should have access to
                for database in envs[env]['users'][user]['databases']:
                    print(f"{user} connecting to {database}:")
                    prefix = ''

                    # Percent-Escaping
                    # client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
                    # print(f"{env} prefix {envs[env]['prefix']}:")
                    connection_string = "mongodb" + envs[env]['prefix'] + "://" + user + ":" + \
                                        envs[env]['users'][user]['password'] + \
                                        envs[env]['server1'] + database + envs[env]['server2']
                    # print('connection_string:', connection_string)
                    client = MongoClient(connection_string)

                    # if 'localhost' in str(client.host):
                    #     uri = 'localhost'
                    # elif 'atlas' in str(client.host):
                    #     uri = 'atlas'
                    # else:
                    #     print(f"\n*** Unknown host: {client.host} ***")
                    #     return
                    #
                    # print(f"*** Using {uri} client ***")

                    # SCRAM-SHA-256 (RFC 7677)
                    # client = MongoClient('127.0.0.1',
                    #                      username=username,
                    #                      password=password,
                    #                      authSource=database,
                    #                      authMechanism='SCRAM-SHA-256')
                    #


                    # Verify if the connection is successful
                    print(f"{user} connected to {env} {database} database successfully!")
                    # print(client.server_info())

                    # return client
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
        client.close()  # Close MongoClient instance if it was successfully created
        