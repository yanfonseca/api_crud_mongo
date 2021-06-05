from pymongo import MongoClient

db = MongoClient(host='localhost', port=27018)

def mongo_client():
    return db['db']['yan']

