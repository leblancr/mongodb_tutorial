import os

from dotenv import load_dotenv

import basic_operations
import aggregations


def main():
    load_dotenv()
    
    #basic_operations.run()  # atlas
    aggregations.run()  # local


if __name__ == '__main__':
    main()
