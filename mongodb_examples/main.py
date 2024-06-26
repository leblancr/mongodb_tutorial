import os

from dotenv import load_dotenv
from mongo_utils import get_mongo_client, list_database_names

import basic_operations
import aggregations


def main():
    load_dotenv()
    
    mongodb_uri_local = os.environ['MONGODB_URI_LOCAL']
    mongodb_uri_atlas = os.environ['MONGODB_URI_ATLAS']
    client_local = get_mongo_client(mongodb_uri_local)
    client_atlas = get_mongo_client(mongodb_uri_atlas)

    clients =[client_local, client_atlas]
    
    for client in clients:
        # print("dir(client):", dir(client))
        #print("client:", client.host)
        
        if 'localhost' in str(client.host):
            uri = 'localhost'
        else:
            uri = 'Atlas'
            
        print(f"\n*** Using {uri} ***")
        
        basic_operations.run(client, uri)
        # aggregations.run(client)
    

if __name__ == '__main__':
    main()
