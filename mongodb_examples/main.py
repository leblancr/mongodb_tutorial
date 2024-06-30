import os
import pprint

from mongo_utils import get_mongo_client, list_database_names

import authentication


def main():
    # Authenticate users then run scripts there
    authentication.run()


if __name__ == '__main__':
    main()
