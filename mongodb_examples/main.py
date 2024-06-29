import os
import pprint

from mongo_utils import get_mongo_client, list_database_names

import basic_operations
import aggregations
import authentication


def main():
    # Authenticate users the run scripts
    authentication.run()
    # basic_operations.run(client, uri)
    # aggregations.run(client, uri)


if __name__ == '__main__':
    main()
