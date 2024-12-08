from pymongo import MongoClient

def create_connection_to_mongo_server(uri, db, collection):
    #Create connection

    client = MongoClient(uri)
    collection = client[db][collection]

    return client, collection
