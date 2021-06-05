from api.app.config import mongo_client


async def add(document):
    db = mongo_client()
    db.insert_one(document)

async def search(query):
    db = mongo_client()
    documents = db.find(query)
    return list(documents)

async def delete(id):
    db = mongo_client()
    documents = db.delete_one({"_id": id})

async def update(query: dict, changes:dict):
    db = mongo_client()
    db.update_one(filter=query, update={"$set": changes})
    ret = db.find_one(query)
    return ret