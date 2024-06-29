from pymongo import MongoClient
from dotenv import load_dotenv

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
    try:
        # load_dotenv()
    
        # mongodb_uri_local = os.environ['MONGODB_URI_LOCAL']
        # mongodb_uri_atlas = os.environ['MONGODB_URI_ATLAS']
        # client_local = get_mongo_client(mongodb_uri_local)
        # client_atlas = get_mongo_client(mongodb_uri_atlas)
        # clients = [client_local, client_atlas]
        
        users = {
            'local': [
                {
                    'user': 'rich',
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
            ],
            'Atlas': [
                {
                    'user': 'rich',
                    'password': 'reddmon',
                    'databases': [
                        'admin',
                        'aggregation_example',
                        'config',
                        'local',
                        'sample_mflix',
                        'test_database'
                        ]
                },
                {
                    'user': 'rkba1',
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
            ]
        }
        
        # Each environment (local, Atlas) has a list of user dictionaries 
        for env in users.keys():
            print(f"{env} users:")
            
            # For each user dictionary print user
            for user_dict in users[env]:
                print(f"{user_dict['user']} should have access to these databases:")
                
                # For each user show the dictionaries they should have access to
                for database in user_dict['databases']:
                    print(f"  {database}")

                print()
            
            # if 'localhost' in str(client.host):
            #     uri = 'localhost'
            # elif 'atlas' in str(client.host):
            #     uri = 'atlas'
            # else:
            #     print(f"\n*** Unknown host: {client.host} ***")
            #     return
            #     
            # print(f"*** Using {uri} client ***")
            #     
            # 
            # mongodb_uri_local = os.environ['MONGODB_URI_LOCAL']
            # mongodb_uri_atlas = os.environ['MONGODB_URI_ATLAS']
            # 
            # print(f"Running {__name__}.py")
            # # admin
            # # aggregation_example
            # # config
            # # local
            # # sample_mflix
            # # test_database
            # 
            # username = urllib.parse.quote_plus('rich')
            # password = urllib.parse.quote_plus('reddmon')
            # database = 'admin'
            # 
            # # Percent-Escaping
            # # client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
            # client = MongoClient('mongodb://%s:%s@127.0.0.1/%s' % (username, password, database))
            # 
            # # SCRAM-SHA-256 (RFC 7677)
            # # client = MongoClient('127.0.0.1',
            # #                      username=username,
            # #                      password=password,
            # #                      authSource=database,
            # #                      authMechanism='SCRAM-SHA-256')
            # # 
            # # Or through the MongoDB URI:
            # uri = "mongodb://rich:reddmon@localhost:27017/?authSource=test_database&authMechanism=SCRAM-SHA-256"
            # #
            # # client = MongoClient(uri)
            # 
            # # Verify if the connection is successful
            # print(client.server_info())
            # print("Connected to MongoDB successfully!")
            # 
            # return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        