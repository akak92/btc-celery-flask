import os
from typing import List, Any, Optional

from pymongo import MongoClient
from pymongo.results import UpdateResult, DeleteResult

mongo_uri = os.getenv('MONGO_URI')

class MongoConnection:
    def __init__(self,
                 uri: Optional[str] = mongo_uri if mongo_uri else "mongodb://btcadmin:btcpass@mongo:27017/?authMechanism=DEFAULT",
                 host: str = 'localhost',
                 port: int = 27017,
                 database_name: Optional[str] = "BTC-PRICES",
                 collection: Optional[str] = None):
        try:
            if uri:
                self.client = MongoClient(uri)
            else:
                self.client = MongoClient(host, port)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {str(e)}")

        if database_name:
            self.db = self.client[database_name]
            if collection:
                self.collection = self.db[collection]

    def set_collection(self, collection: str):
        if self.db is not None:
            self.collection = self.db[collection]
        else:
            raise AttributeError("Database must be set before setting collection.")

    def close(self):
        if hasattr(self, 'client'):
            self.client.close()


    def get_registers_with_pagination(self, filter: dict, skip: int = 0, limit: int = 10) -> List[dict]:
        return list(self.collection.find(filter).skip(skip).limit(limit))

