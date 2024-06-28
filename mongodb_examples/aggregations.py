import datetime
import pprint

from bson import ObjectId
from pymongoexplain import ExplainableCollection

from mongo_utils import get_mongo_client, get_database_names, list_collections, list_database_names


def run(client, uri):
    try:
        db = client.aggregation_example
        # run once to setup data
        # result = db.things.insert_many(
        #     [
        #         {"x": 1, "tags": ["dog", "cat"]},
        #         {"x": 2, "tags": ["cat"]},
        #         {"x": 2, "tags": ["mouse", "cat", "dog"]},
        #         {"x": 3, "tags": []},
        #     ]
        # )

#        print('result.inserted_ids', result.inserted_ids)

        print(f"{uri} databases:")
        list_database_names(client)
        database_names = get_database_names(client)
        
        # Print all databases in the client
        for database_name in ['aggregation_example']:  # database_names:
            print(f"{database_name} database collections:")
            db = client[database_name]
            list_collections(db)  # print all collections in the database
            
            # show documents in each collection
            for collection_name in db.list_collection_names():
                # Count documents in the collection
                document_count = db[collection_name].count_documents({})
                print(f"{collection_name} collection documents ({document_count}):")
                documents = db[collection_name].find()
                # db[collection_name].delete_one({'_id': ObjectId('667c1e0a99581cf6129caa14')})
                # db[collection_name].delete_many({'_id': {'$gte': ObjectId('667c192d28d647539cde3c68'),
                #                                          '$lte': ObjectId('667c192d28d647539cde3c6b')}})

                for document in documents:
                    pprint.pprint(document)

                pipelines = [
                    [{"$unwind": "$tags"}],
                    [{"$unwind": "$tags"},
                     {"$group": {"_id": "$tags"}}],
                    [{"$unwind": "$tags"},
                     {"$group": {"_id": "$tags", "count": {"$sum": 1}}}],
                    [{"$unwind": "$tags"},
                     {"$group": {"_id": "$tags", "count": {"$sum": 1}}}],
                    [{"$unwind": "$tags"},  # creates a new document for each element in the array
                     {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
                     {"$sort": {"count": -1, "_id": -1}}]
                ]

                # run each pipeline
                for i, pipeline in enumerate(pipelines, start=1):
                    print(f"\npipeline {i}:")
                    # pprint.pprint(list(db.things.aggregate(pipeline)))
                    # pprint.pprint(ExplainableCollection(db[collection_name]).aggregate(pipeline))
                    pprint.pprint(db.command('aggregate', 'things', pipeline=pipeline, explain=True))
    except KeyError as e:
        print("Error: ", e)
