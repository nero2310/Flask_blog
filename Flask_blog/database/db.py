import pymongo
from typing import Dict


class Mongo:
    def __init__(self, database="test", collection="user"):
        """
        Class to work with mongoDB
        :arg database - database you will use
        :arg collection - collection you wii use
        """
        mongo_client = pymongo.MongoClient('localhost', 2717)
        db = mongo_client[database]
        self.collection = db[collection]
        print("Działa")

    def find(self, how_many="one", data_filter=None):
        """:arg how_many how many results should be returned
        :arg data_filter filter data to return
        :return string or list"""
        if data_filter is None:
            data_filter = {}
        if how_many == "one":
            return self.collection.find_one(data_filter)
        elif how_many == "all":
            cursor = self.collection.find(data_filter)
            return [document for document in cursor]


db_obj = Mongo()
print(db_obj.find("all"))
